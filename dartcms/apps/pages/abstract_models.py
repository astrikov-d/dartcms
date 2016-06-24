# coding: utf-8
from django.conf import settings
from django.db import models
from django.db.models import F, Max
from django.db.models.signals import post_save, pre_delete, pre_save
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language

from dartcms.apps.adv.models import AdvSection

from .models import PageModule


class AbstractPage(models.Model):
    class Meta:
        abstract = True
        ordering = ['sort']
        verbose_name = _('page')
        verbose_name_plural = _('pages')
        unique_together = ['module', 'slug']

    def __unicode__(self):
        parent = self.parent
        page_names = [self.title]
        while parent:
            page_names.append(parent.title)
            parent = parent.parent
        return ' / '.join(reversed(page_names))

    parent = models.ForeignKey('self', null=True, related_name='children', verbose_name=_('Parent Page'))

    title = models.CharField(max_length=255, verbose_name=_('Title'), help_text=_('Shows inside the title tag'))
    header = models.CharField(max_length=255, verbose_name=_('Page Header'))

    menu_name = models.CharField(max_length=255, default='', verbose_name=_('Menu name'))
    menu_url = models.CharField(max_length=255, blank=True, default='', verbose_name=_('URL for Redirect'))
    slug = models.SlugField(default='', verbose_name=_('URL'))
    url = models.CharField(max_length=512)

    sort = models.IntegerField(default=1)

    module = models.ForeignKey(PageModule, verbose_name=_('Module'))
    module_params = models.CharField(max_length=128, blank=True, null=True, default=None,
                                     verbose_name=_('Module parameters'))

    before_content = models.TextField(default='', blank=True, verbose_name=_('Before Content'))
    after_content = models.TextField(default='', blank=True, verbose_name=_('After Content'))

    seo_keywords = models.TextField(default='', blank=True, verbose_name=_('Keywords (meta keywords)'))
    seo_description = models.TextField(default='', blank=True, verbose_name=_('Description (meta description)'))

    adv_section = models.ForeignKey(AdvSection, verbose_name=_('Ads'))

    is_enabled = models.BooleanField(default=True, verbose_name=_('Is Enabled'))
    is_in_menu = models.BooleanField(default=True, verbose_name=_('Show in Menu'))

    date_created = models.DateTimeField(auto_now_add=True)

    def get_menu_url(self):
        lang = get_language()
        prefix = '' if lang == settings.LANGUAGE_CODE else '/%s' % lang
        return prefix + self.menu_url if self.menu_url else prefix + self.url

    def get_page_url(self):

        if self.module.slug == 'pagemap':
            return '/page/%s/' % self.slug
        if self.module.slug == 'feeds':
            return '/feeds/%s/' % self.slug
        if self.module.slug == 'feedback':
            return '/feedback/%s/' % self.slug

        return '/%s/' % self.module.slug


def pre_save_handler(sender, **kwargs):
    instance = kwargs.get('instance')
    if instance:
        instance.url = instance.get_page_url()

        current_level_pages = sender.objects.filter(parent=instance.parent)

        if not current_level_pages.exists():
            instance.sort = 1

        if not instance.id or instance.sort == 0:
            max_sort = current_level_pages.aggregate(Max('sort'))
            instance.sort = max_sort['sort__max'] + 1 if max_sort['sort_max'] else 1
        else:
            page_cache = sender.objects.get(pk=instance.id)

            if page_cache.parent == instance.parent:
                if int(page_cache.sort) < int(instance.sort):
                    instance.sort -= 1
                    current_level_pages.filter(sort__gt=page_cache.sort, sort__lte=instance.sort).update(
                        sort=F('sort') - 1)
                else:
                    current_level_pages.filter(sort__gte=instance.sort, sort__lt=page_cache.sort).update(
                        sort=F('sort') + 1)
            else:
                current_level_pages.filter(sort__gte=instance.sort).update(sort=F('sort') + 1)
                sender.objects.filter(parent=page_cache.parent, sort__gt=page_cache.sort).update(sort=F('sort') - 1)


def post_save_handler(**kwargs):
    instance = kwargs.get('instance')
    if instance:
        children = instance.children.all()
        if children:
            for child in instance.children.all():
                child.save()


def pre_delete_handler(sender, **kwargs):
    instance = kwargs.get('instance')
    if instance:
        sender.objects.filter(parent=instance.parent, sort__gt=instance.sort).update(sort=F('sort') - 1)


pre_save.connect(pre_save_handler, sender=AbstractPage)
post_save.connect(post_save_handler, sender=AbstractPage)
pre_delete.connect(pre_delete_handler, sender=AbstractPage)
