# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from views import FilemanagerIndexView, FilemanagerCreateFolderView, \
    FilemanagerFolderListView, FilemanagerFileListView, FilemanagerSendFileView, \
    FilemanagerRenameFolderView, FilemanagerRemoveFolderView, FilemanagerRemoveFileView

urlpatterns = patterns('',
    url(r'^$', login_required(FilemanagerIndexView.as_view()), name='index'),
    url(r'^create-folder/$', login_required(FilemanagerCreateFolderView.as_view()), name='create_folder'),
    url(r'^get-folders/$', login_required(FilemanagerFolderListView.as_view()), name='folders_list'),
    url(r'^get-files/$', login_required(FilemanagerFileListView.as_view()), name='files_list'),
    url(r'^send-file/$', login_required(FilemanagerSendFileView.as_view()), name='send_file'),
    url(r'^rename-folder/$', login_required(FilemanagerRenameFolderView.as_view()), name='rename_folder'),
    url(r'^remove-folder/$', login_required(FilemanagerRemoveFolderView.as_view()), name='remove_folder'),
    url(r'^remove-file/$', login_required(FilemanagerRemoveFileView.as_view()), name='remove_file'),
)