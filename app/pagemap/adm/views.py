# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

from app.pagemap.models import Page, PageModule

from lib.views.adm.generic import SortableTreeGridView, InsertObjectView, DeleteObjectView
from lib.views.generic import AjaxRequestView


class PagemapView(SortableTreeGridView):
    model = Page
    template_name = "adm/pagemap/sortable_tree_grid.html"
    page_header = _(u"Site Structure")
    grid_columns = (
        ('title', _(u"Name")),
    )

    def get_queryset(self):
        return Page.objects.filter(parent_id=1)


class PageModuleLoadParamsView(AjaxRequestView):
    def get_response(self, request, *args, **kwargs):
        module = PageModule.objects.get(id=request.GET.get('selected_module', 0))

        def get_news_feeds():
            from app.feeds.models import Feed
            return Feed.objects.all().extra(select={'label': 'name', 'value': 'id'})

        def get_feedback_types():
            from app.feedback.models import FeedbackType
            return FeedbackType.objects.filter(is_enable=True).extra(select={'label': 'name', 'value': 'id'})

        switch = {
            'feeds': get_news_feeds(),
            'feedback': get_feedback_types()
        }
        data = []

        if module.slug not in switch:
            return {
                'result': 'success',
                'data': []
            }

        page_pk = request.GET.get('pk', "")
        if page_pk != "":
            page = Page.objects.get(id=request.GET.get('pk', 0))
        else:
            page = None

        for item in switch[module.slug]:
            if page is not None and page.module == module and str(page.module_params) == str(item.value):
                data.append({'label': item.label, 'value': item.value, 'selected': True})
            else:
                data.append({'label': item.label, 'value': item.value})
        return {
            'result': 'success',
            'data': data
        }


class PageDeleteView(DeleteObjectView):
    template_name = "adm/pagemap/delete.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PageDeleteView, self).get_context_data()
        if int(self.kwargs['pk']) == 1:
            context.update({
                'is_homepage': True
            })
        return context


class PageInsertObjectView(InsertObjectView):
    def get_initial(self):
        initial = super(PageInsertObjectView, self).get_initial()
        initial.update({'parent': self.kwargs.get('parent')})
        return initial