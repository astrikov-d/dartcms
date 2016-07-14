# coding: utf-8
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import (CreateFolderView, DeleteFileView, DeleteFolderView,
                    FileManagerIndexView, GetFilesView, GetTreeView,
                    RenameFolderView, UploadFileView)

urlpatterns = [
    url(r'^$', login_required(FileManagerIndexView.as_view()), name='index'),
    url(r'^get-tree/$', login_required(GetTreeView.as_view()), name='get_tree'),
    url(r'^create-folder/$', login_required(CreateFolderView.as_view()), name='create_folder'),
    url(r'^get-files/$', login_required(GetFilesView.as_view()), name='get_files'),
    url(r'^send-file/$', login_required(UploadFileView.as_view()), name='upload_file'),
    url(r'^rename-folder/$', login_required(RenameFolderView.as_view()), name='rename_folder'),
    url(r'^delete-file/$', login_required(DeleteFileView.as_view()), name='delete_file'),
    url(r'^delete-folder/$', login_required(DeleteFolderView.as_view()), name='delete_folder'),
]
