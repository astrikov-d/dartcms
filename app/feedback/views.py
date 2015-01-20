# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.views.generic import CreateView, TemplateView
from django.http import Http404
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from models import FeedbackType, FeedbackMessage
from app.pagemap.models import Page
from forms import FeedbackForm


class FeedbackIndexView(CreateView):
    template_name = "site/feedback/index.html"
    form_class = FeedbackForm

    def get_context_data(self, **kwargs):
        try:
            page = Page.objects.get(slug=self.kwargs['page_slug'], module__slug = 'feedback')
        except Page.DoesNotExist:
            raise Http404
        return super(FeedbackIndexView, self).get_context_data(**kwargs)

    def get_success_url(self):
        page_slug = self.request.page.slug
        return reverse_lazy("feedback:success", kwargs={'page_slug': page_slug})

    def form_valid(self, form):
        obj = form.save(commit=False)
        page = Page.objects.get(slug=self.kwargs['page_slug'], module__slug = 'feedback')
        obj.feedback_type_id = page.module_params
        obj.save()
        return redirect(self.get_success_url())


class FeedbackSuccessView(TemplateView):
    template_name = "site/feedback/sucess.html"