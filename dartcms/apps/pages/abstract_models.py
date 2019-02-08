# coding: utf-8
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language
from mptt.models import MPTTModel, TreeForeignKey

from dartcms.apps.users.models import UserGroup
from dartcms.utils.fields import RteField


class PageModule(models.Model):
    class Meta:
        app_label = 'pages'
        ordering = ['name']
        verbose_name_plural = _('modules')
        verbose_name = _('module')

    def __unicode__(self):
        return self.name

    slug = models.SlugField(unique=True, verbose_name=_('Slug'))
    name = models.CharField(max_length=64, verbose_name=_('Name'))
    related_model = models.CharField(verbose_name=_('Related Model'), null=True, default=None, max_length=32,
                                     blank=True)
    is_enabled = models.BooleanField(default=True, verbose_name=_('Is Enabled'))


SECURITY_TYPE_CHOICES = (
    ('DEFAULT', _('Editable for all users')),
    ('BY_PARENT', _('Based on the parent page')),
    ('GROUPS_ONLY', _('Editable for specific groups')),
)


class AbstractPage(MPTTModel):
    """
    Base page model. In common cases, you should not re-declare this class, since it have all necessary features.
    It holds base information about site's pages - urls, names, functional features, parents and childrens etc.
    """

    class Meta:
        app_label = 'pages'
        abstract = True
        ordering = ['sort']
        verbose_name = _('page')
        verbose_name_plural = _('pages')
        unique_together = ['module', 'slug']

    def __unicode__(self):
        return self.title

    @property
    def full_path(self):
        """
        Constructs breadcrumbs-like page name.
        """
        parent = self.parent
        page_names = [self.title]
        while parent:
            page_names.append(parent.title)
            parent = parent.parent
        return ' / '.join(reversed(page_names))

    parent = TreeForeignKey('self', null=True, related_name='children', verbose_name=_('Parent Page'), blank=True)

    title = models.CharField(max_length=255, verbose_name=_('Title'), help_text=_('Shows inside the title tag'))
    header = models.CharField(max_length=255, verbose_name=_('Page Header'))

    menu_name = models.CharField(max_length=255, default='', verbose_name=_('Menu name'))
    redirect_url = models.CharField(max_length=255, blank=True, default='', verbose_name=_('URL for Redirect'))

    slug = models.SlugField(default='', verbose_name=_('URL'), blank=True)
    url = models.CharField(max_length=512, unique=True)

    sort = models.IntegerField(default=1)

    module = models.ForeignKey('pages.PageModule', verbose_name=_('Module'),
                               related_name='%(app_label)s_%(class)s_related')
    module_params = models.CharField(max_length=128, blank=True, null=True, default=None,
                                     verbose_name=_('Module parameters'))

    before_content = RteField(default='', blank=True, verbose_name=_('Before Content'))
    after_content = RteField(default='', blank=True, verbose_name=_('After Content'))

    seo_keywords = models.TextField(default='', blank=True, verbose_name=_('Keywords (meta keywords)'))
    seo_description = models.TextField(default='', blank=True, verbose_name=_('Description (meta description)'))

    ad_section = models.ForeignKey('ads.AdSection', verbose_name=_('Ads'), null=True, blank=True,
                                   related_name='%(app_label)s_%(class)s_related')

    security_type = models.CharField(max_length=16, verbose_name=_('Security type'), choices=SECURITY_TYPE_CHOICES,
                                     default='BY_PARENT')
    user_groups = models.ManyToManyField(UserGroup, verbose_name=_('User groups'))

    is_enabled = models.BooleanField(default=True, verbose_name=_('Is Enabled'))
    is_in_menu = models.BooleanField(default=True, verbose_name=_('Show in Menu'))

    date_created = models.DateTimeField(auto_now_add=True)

    def get_security_type(self):
        if self.security_type == 'BY_PARENT' and self.parent:
            parent = self.parent
            while parent:
                if parent.security_type == 'BY_PARENT':
                    parent = parent.parent
                else:
                    break
            return parent.security_type
        else:
            return self.security_type

    def delete(self):
        if not self.parent:
            pass
        else:
            return super(AbstractPage, self).delete()

    @property
    def menu_url(self):
        lang = get_language()
        prefix = '' if lang == settings.LANGUAGE_CODE else '/%s' % lang
        return self.redirect_url if self.redirect_url else prefix + self.url

    @property
    def page_url(self):
        if not self.parent:
            return '/'
        return '/%s/%s/' % (self.module.slug, self.slug)

    def serializable_object(self):
        obj = {
            'pk': self.pk,
            'parent_id': self.parent_id,
            'title': self.title,
            'module': str(self.module),
            'url': self.url,
            'children': []
        }
        for child in self.get_children():
            obj['children'].append(child.serializable_object())
        return obj
