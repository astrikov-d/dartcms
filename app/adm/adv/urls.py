# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'


from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^adv/', include('app.adm.adv.adv.urls'), name='adv'),
    url(r'^adv-places/', include('app.adm.adv.advplace.urls'), name='advplace'),
    url(r'^adv-sections/', include('app.adm.adv.advsection.urls'), name='advsection'),
)