# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class FeedbackConfig(AppConfig):
    name = 'dartcms.apps.feedback'
    verbose_name = _('Feedback')
