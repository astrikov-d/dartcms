# coding: utf-8
from django.http.response import Http404
from django.shortcuts import redirect

from dartcms import get_model


class PageMiddleware(object):

    def process_request(self, request):
        PageModule = get_model('pages', 'PageModule')
        Page = get_model('pages', 'Page')

        request_path = request.path.strip('/')
        path_parts = request_path.split('/')

        path = '/' if request_path == '' else '/%s/' % request.path.strip('/')
        module_slug = 'homepage' if path == '/' else path_parts[0]

        try:
            request.page_module = PageModule.objects.get(slug=module_slug)
        except PageModule.DoesNotExist:
            return

        page = None

        try:
            page = Page.objects.get(url=path)
        except Page.DoesNotExist:
            while path_parts:
                path_parts.pop()
                if path_parts:
                    path = '/%s/' % '/'.join(path_parts)
                    try:
                        page = Page.objects.get(url=path)
                        break
                    except Page.DoesNotExist:
                        continue

        if page:
            if page.redirect_url:
                return redirect(page.redirect_url)
            request.page = page
            request.page_children = page.children.filter(is_enabled=True, is_in_menu=True)

    def process_view(self, request, view_func, view_args, view_kwargs):
        namespaces = request.resolver_match.namespaces

        if 'dartcms' in namespaces or 'admin' in namespaces:
            return

        if hasattr(request, 'page_module') and not hasattr(request, 'page'):
            raise Http404
