# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

import os

from django.views.generic import TemplateView
from django.http import Http404

from app.cms.models import Folder, File

from lib.views.generic import AjaxRequestView
from lib.utils.forms import get_list_of_errors

from forms import FolderForm, FileUploadForm


class FilemanagerIndexView(TemplateView):
    template_name = "adm/filemanager/index.html"

    def get_context_data(self, **kwargs):
        context_data = super(FilemanagerIndexView, self).get_context_data(**kwargs)
        context_data.update({
            'folders': Folder.objects.all(),
            'file_upload_form': FileUploadForm
        })
        return context_data


class FilemanagerFolderListView(AjaxRequestView):
    def get_response(self, request, *args, **kwargs):
        folders = Folder.objects.all()
        return [{'name': folder.name, 'pk': folder.pk} for folder in folders]


class FilemanagerCreateFolderView(AjaxRequestView):
    def get_response(self, request, *args, **kwargs):
        form = FolderForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return {
                'result': 'success'
            }
        else:
            return {
                'result': 'error',
                'errors': get_list_of_errors(form)
            }


class FilemanagerFileListView(AjaxRequestView):
    def get_response(self, request, *args, **kwargs):
        try:
            folder = Folder.objects.get(pk=request.GET.get('folder_id', 0))
        except Folder.DoesNotExist:
            raise Http404

        files = File.objects.filter(folder=folder)
        return [{
                    'name': os.path.basename(f.path.name),
                    'path': f.path.name,
                    'pk': f.pk
                } for f in files]


class FilemanagerSendFileView(AjaxRequestView):
    def get_response(self, request, *args, **kwargs):
        try:
            folder = Folder.objects.get(pk=request.POST.get('selected_folder_id', 0))
        except Folder.DoesNotExist:
            raise Http404
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.folder = folder
            file.save()
            return {
                'result': 'success'
            }
        else:
            return {
                'result': 'error'
            }


class FilemanagerRenameFolderView(AjaxRequestView):
    def get_response(self, request, *args, **kwargs):
        try:
            folder = Folder.objects.get(pk=request.POST.get('folder_id', 0))
        except Folder.DoesNotExist:
            raise Http404

        form = FolderForm(request.POST, request=request, instance=folder)
        if form.is_valid():
            form.save()
            return {
                'result': 'success'
            }
        else:
            return {
                'result': 'error',
                'errors': get_list_of_errors(form)
            }


class FilemanagerRemoveFolderView(AjaxRequestView):
    def get_response(self, request, *args, **kwargs):
        try:
            folder = Folder.objects.get(pk=request.POST.get('folder_id', 0))
        except Folder.DoesNotExist:
            raise Http404

        folder.delete()
        return {
            'result': 'success'
        }


class FilemanagerRemoveFileView(AjaxRequestView):
    def get_response(self, request, *args, **kwargs):
        try:
            file = File.objects.get(pk=request.POST.get('file_id', 0))
        except File.DoesNotExist:
            raise Http404

        file.delete()
        return {
            'result': 'success'
        }
