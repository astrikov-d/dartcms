# -*- coding: utf-8 -*-

from app.models import Page, PageModule
from lib.views.adm.generic import SortableTreeGridView
from lib.views.generic import AjaxRequestView


class PagemapView(SortableTreeGridView):
    model = Page
    template_name = "adm/pagemap/sortable_tree_grid.html"
    page_header = u"Структура сайта"
    grid_columns = (
        ('title', u"Название"),
    )

    def get_queryset(self):
        return Page.objects.filter(parent_id=1)


class PageModuleLoadParamsView(AjaxRequestView):
    def get_response(self, request, *args, **kwargs):
        module = PageModule.objects.get(id=request.GET.get('selected_module', 0))

        def get_news_feeds():
            from app.models import Feed
            return Feed.objects.all().extra(select={'label': 'name', 'value': 'id'})

        switch = {
            'feeds': get_news_feeds(),
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

