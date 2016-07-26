# coding: utf-8
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FeedbackConfig(AppConfig):
    name = 'dartcms.apps.feedback'
    verbose_name = _('Feedback')
