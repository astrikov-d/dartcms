# coding: utf-8
import os

from django.conf import settings
from django.http import Http404
from django.utils import formats
from django.views.generic import TemplateView

from dartcms.views import JSONView

from .forms import FolderForm
from .models import File, Folder


class FileManagerIndexView(TemplateView):
    template_name = 'dartcms/apps/filemanager/index.html'


class GetTreeView(JSONView):
    def get_data(self, context):
        response = []

        for folder in Folder.objects.all().order_by('name'):
            response.append({
                'id': folder.id,
                'text': folder.name,
                'iconCls': 'icon-folder'
            })
        return response


class CreateFolderView(JSONView):
    def get_data(self, context):
        folder_form = FolderForm(self.request.POST)
        if folder_form.is_valid():
            folder_form.save()
            response = {'result': True}

        else:
            response = {
                'result': False,
                'errors': folder_form.errors
            }
        return response


class GetFilesView(JSONView):
    def get_data(self, context):
        try:
            folder = Folder.objects.get(pk=self.request.GET.get('folder_id'))
            response = []
            for f in folder.files.all().order_by('-date_created'):
                response.append({
                    'id': f.id,
                    'name': os.path.basename(f.path.name),
                    'path': settings.MEDIA_URL + f.path.name,
                    'date_created': formats.date_format(f.date_created, "SHORT_DATETIME_FORMAT")
                })
            return response
        except Folder.DoesNotExist:
            raise Http404


class UploadFileView(JSONView):
    def get_data(self, context):
        try:
            folder_id = int(self.request.POST.get('folder_id'))
            folder = Folder.objects.get(id=folder_id)
            for f in self.request.FILES.getlist('files'):
                File(folder=folder, path=f).save()

            return {'result': True}
        except Folder.DoesNotExist:
            raise Http404


class RenameFolderView(JSONView):
    def get_data(self, context):
        try:
            folder = Folder.objects.get(pk=self.request.GET.get('folder_id'))
            folder_form = FolderForm(self.request.POST, instance=folder)
            if folder_form.is_valid():
                folder_form.save()
                response = {'result': 'success'}
            else:
                response = {
                    'result': 'error',
                    'errors': folder_form.errors
                }
            return response
        except Folder.DoesNotExist:
            raise Http404


class DeleteFolderView(JSONView):
    def get_data(self, context):
        try:
            Folder.objects.get(pk=self.request.GET.get('folder_id')).delete()
            return {'result': 'success'}
        except Folder.DoesNotExist:
            raise Http404


class DeleteFileView(JSONView):
    def get_data(self, context):
        try:
            File.objects.get(pk=self.request.GET.get('file_id'), folder_id=self.request.GET.get('folder_id')).delete()
            return {'result': 'success'}
        except Folder.DoesNotExist:
            raise Http404
