# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'


from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^adv/', include('app.adv.adm.adv.urls'), name='adv'),
    url(r'^adv-places/', include('app.adv.adm.advplace.urls'), name='advplace'),
    url(r'^adv-sections/', include('app.adv.adm.advsection.urls'), name='advsection'),
)