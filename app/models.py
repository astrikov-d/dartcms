# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

import datetime
import string
from pytils.translit import slugify
import watson

from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.db.models import F
from django.utils.translation import get_language
from django.conf import settings

from lib.utils.hash import random_string


class CMSModuleGroup(models.Model):
    class Meta:
        verbose_name_plural = "Группы модулей CMS"
        verbose_name = "Группа модулей CMS"
        ordering = ['sort']

    def __unicode__(self):
        return self.name

    slug = models.SlugField(unique=True, verbose_name="Идентификатор")
    name = models.CharField(max_length=64, verbose_name="Название")
    fa = models.SlugField(verbose_name="FontAwesome class")
    sort = models.IntegerField(default=1, verbose_name="Сортировка")
    description = models.TextField(default='', verbose_name="Описание", blank=True)


class CMSModule(models.Model):
    class Meta:
        verbose_name_plural = "Модули CMS"
        verbose_name = "Модуль CMS"
        ordering = ['group', 'sort']

    def __unicode__(self):
        return self.group.name + " / " + self.name

    group = models.ForeignKey(CMSModuleGroup, to_field='slug', verbose_name="Группа", related_name="cmsmodules")
    name = models.CharField(max_length=64, verbose_name="Название")
    sort = models.IntegerField(default=1, verbose_name="Сортировка")
    description = models.TextField(default='', verbose_name="Описание", blank=True)
    slug = models.SlugField(unique=True, verbose_name="Идентификатор")
    is_enabled = models.BooleanField(default=True, verbose_name="Включен")


class Folder(models.Model):
    class Meta:
        verbose_name = "папка"
        verbose_name_plural = "папки"
        ordering = ['name']
        unique_together = ('name',)

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name='Название')
    date_created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())


class File(models.Model):
    folder = models.ForeignKey(Folder)
    path = models.FileField(upload_to="uploads/%Y/%m/%d")
    date_created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())


@receiver(pre_delete, sender=File)
def files_delete(sender, instance, **kwargs):
    """
    On file delete, we should also delete the file.
    """
    instance.path.delete(False)


class SiteSettings(models.Model):
    site_title = models.CharField(
        max_length=255,
        default="",
        verbose_name="Название сайта",
    )
    site_description = models.TextField(
        verbose_name="Описание сайта"
    )
    footer_content = models.TextField(default="", verbose_name="Содержимое футера")


class AdvPlace(models.Model):
    """
    Place for advertisement.
    """

    class Meta:
        verbose_name = "рекламное место"
        verbose_name_plural = "рекламные места"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name=u'Название')
    slug = models.SlugField(unique=True)
    is_enabled = models.BooleanField(default=True, verbose_name=u'Включено')


class AdvSection(models.Model):
    """
    Section for advertisement. For example, homepage, or feeds page.
    """

    class Meta:
        verbose_name = "рекламный раздел"
        verbose_name_plural = "рекламные разделы"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name=u'Название')
    is_enabled = models.BooleanField(default=True, verbose_name=u'Включено')


class Adv(models.Model):
    """
    Advertisement settings.
    """

    class Meta:
        verbose_name = "рекламный баннер"
        verbose_name_plural = "рекламные баннеры"
        ordering = ['name']

    date_from = models.DateTimeField(default=datetime.date.today(), verbose_name=u'Дата начала размещения')
    date_to = models.DateTimeField(
        default=datetime.date.today() + datetime.timedelta(days=30),
        verbose_name=u'Дата окончания размещения')
    name = models.CharField(max_length=255, verbose_name=u'Заголовок')
    title = models.TextField(default='', blank=True, verbose_name=u'Текст')
    link = models.URLField(default='', blank=True, verbose_name=u'Ссылка')
    code = models.TextField(default='', blank=True, verbose_name=u'Код баннера')
    bg = models.CharField(default='', blank=True, max_length=255, verbose_name=u'Цвет фона')
    place = models.ForeignKey(AdvPlace, verbose_name=u'Место размещения')
    section = models.ManyToManyField(AdvSection, verbose_name=u'Раздел')
    picture = models.FileField(upload_to="b/%Y/%m/%d", null=True, blank=True, verbose_name=u'Изображение')
    is_enabled = models.BooleanField(default=True, verbose_name=u'Включено')
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)


class PageModule(models.Model):
    """
    Page module. I.e. feeds, homepage, catalog etc.
    """

    class Meta:
        ordering = ['id']
        verbose_name_plural = u"Функциональные модули"
        verbose_name = u"Функциональный модуль"

    def __unicode__(self):
        return self.name

    slug = models.SlugField(unique=True, verbose_name=u"Идентификатор")
    name = models.CharField(max_length=64, verbose_name=u"Название")
    is_enabled = models.BooleanField(default=True, verbose_name=u"Включен")


class Page(models.Model):
    """
    Page class.
    """

    class Meta:
        ordering = ['sort']
        verbose_name = "страница"
        verbose_name_plural = "страницы"
        unique_together = ['module', 'slug']

    def __unicode__(self):
        page = self
        parent = page.parent
        page_names = [page.title]
        while parent:
            page_names.append(parent.title)
            parent = parent.parent
        return string.join(reversed(page_names), " / ")

    parent = models.ForeignKey("self", null=True, related_name='children', verbose_name="Родительская страница")
    title = models.CharField(max_length=255, verbose_name=u'Название (отображается в title)')
    header = models.CharField(max_length=255, verbose_name=u'Заголовок на странице')
    menu_name = models.CharField(max_length=255, default='', verbose_name=u'Название пункта меню')
    menu_url = models.CharField(max_length=255, blank=True, default='', verbose_name=u'Прямой url c пункта меню')
    slug = models.SlugField(default='', verbose_name=u'Имя для URL')
    url = models.CharField(max_length=512)
    sort = models.IntegerField(default=1)
    module = models.ForeignKey(PageModule, verbose_name=u"Функциональный модуль")
    module_params = models.CharField(max_length=128, blank=True, null=True, default=None,
                                     verbose_name=u'Параметры модуля')
    before_content = models.TextField(default='', blank=True, verbose_name=u'Содержимое до контента')
    after_content = models.TextField(default='', blank=True, verbose_name=u'Содержимое после контента')
    date_created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)
    date_changed = models.DateTimeField(auto_now=True, default=datetime.datetime.now)
    keywords = models.TextField(default='', blank=True, verbose_name=u'Ключевые слова (meta keywords)')
    description = models.TextField(default='', blank=True, verbose_name=u'Описание (meta description)')
    adv_section = models.ForeignKey(AdvSection, verbose_name=u'Реклама')
    is_enabled = models.BooleanField(default=True, verbose_name=u'Включена')
    is_in_menu = models.BooleanField(default=True, verbose_name=u'Показывать в меню')
    is_locked = models.BooleanField(default=False, verbose_name=u'Только для авторизованных пользователей')

    def get_menu_url(self):
        if self.menu_url:
            return self.menu_url

        url = self.url

        lang = get_language()
        if lang == settings.LANGUAGE_CODE:
            prefix = ''
        else:
            prefix = '/' + lang

        if self.menu_url != '':
            return prefix + self.menu_url
        return prefix + url

    def delete(self, using=None):
        Page.objects.filter(parent=self.parent, sort__gt=self.sort).update(sort=F('sort') - 1)
        super(Page, self).delete(using=None)

    def get_page_url(self):

        if self.module.slug == 'pagemap':
            return u"/page/%s/" % self.slug
        if self.module.slug == 'feeds':
            return u"/feeds/%s/" % self.slug

        return u"/%s/" % self.module.slug

    def save(self, *args, **kwargs):

        self.url = self.get_page_url()

        # Form page sort
        current_level_pages = Page.objects.filter(parent=self.parent)

        if not current_level_pages:
            self.sort = 1

        if not self.id or self.sort == 0:
            from django.db.models import Max

            max_sort = current_level_pages.aggregate(Max('sort'))
            if max_sort['sort__max']:
                self.sort = max_sort['sort__max'] + 1
            else:
                self.sort = 1
        else:
            page_cache = Page.objects.get(pk=self.id)

            if page_cache.parent == self.parent:
                if int(page_cache.sort) < int(self.sort):
                    self.sort -= 1
                    current_level_pages.filter(sort__gt=page_cache.sort, sort__lte=self.sort).update(sort=F('sort') - 1)
                else:
                    current_level_pages.filter(sort__gte=self.sort, sort__lt=page_cache.sort).update(sort=F('sort') + 1)
            else:
                current_level_pages.filter(sort__gte=self.sort).update(sort=F('sort') + 1)
                Page.objects.filter(parent=page_cache.parent, sort__gt=page_cache.sort).update(sort=F('sort') - 1)

        super(Page, self).save(*args, **kwargs)

        childes = self.children.all()
        if childes:
            for child in childes:
                child.save()


class FeedType(models.Model):
    class Meta:
        verbose_name = "Тип ленты"
        verbose_name_plural = "Типы лент"

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name="Название типа")
    slug = models.SlugField(verbose_name="Идентификатор")


class Feed(models.Model):
    class Meta:
        verbose_name = "категория новостей"
        verbose_name_plural = "категории новостей"
        ordering = ['name']
        unique_together = ['type', 'slug']

    def __unicode__(self):
        return self.name

    type = models.ForeignKey(FeedType, verbose_name="Тип", related_name="feeds")
    name = models.CharField(max_length=255, verbose_name="Название категории")
    slug = models.SlugField(verbose_name="Имя для URL")


class FeedItem(models.Model):
    class Meta:
        verbose_name = "запись ленты"
        verbose_name_plural = "записи ленты"
        ordering = ['-date_published']

    @property
    def search_content_type(self):
        return self.feed.type.slug

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        while True:
            try:
                FeedItem.objects.get(slug=self.slug)
                self.slug = u"%s-%s" % (self.slug, datetime.datetime.today().strftime("%Y%m%d%H%M%S"))
            except FeedItem.DoesNotExist:
                break
        super(FeedItem, self).save()

    feed = models.ForeignKey(Feed, verbose_name="Лента")
    name = models.CharField(max_length=1024, verbose_name="Заголовок")
    slug = models.SlugField(unique=True, verbose_name="Текстовый идентификатор")
    short_text = models.TextField(verbose_name="Анонс")
    full_text = models.TextField(verbose_name="Полный текст")
    picture = models.ImageField(verbose_name="Изображение", upload_to="feeds/%Y/%m/%d")
    seo_keywords = models.TextField(
        verbose_name="Ключевые слова (SEO)",
        help_text="Не рекомендуется использовать более 255 символов",
        blank=True
    )
    seo_description = models.TextField(
        verbose_name="Описание (SEO)",
        help_text="Не рекомендуется использовать более 1024 символов",
        blank=True
    )
    is_visible = models.BooleanField(default=True, verbose_name="Отображать на сайте")
    date_published = models.DateTimeField(default=datetime.datetime.now, verbose_name="Дата публикации")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

watson.register(FeedItem)


class ProjectType(models.Model):
    class Meta:
        verbose_name = "тип проекта"
        verbose_name_plural = "типы проектов"
        ordering = ['name']

    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(verbose_name="Идентификатор")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")


class Project(models.Model):
    class Meta:
        verbose_name = "проект"
        verbose_name_plural = "проекты"
        ordering = ['-date_published']

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        while True:
            try:
                Project.objects.get(slug=self.slug)
                self.slug = u"%s-%s" % (self.slug, datetime.datetime.today().strftime("%Y%m%d%H%M%S"))
            except Project.DoesNotExist:
                break
        super(Project, self).save()

    project_type = models.ForeignKey(ProjectType, related_name='projects')
    name = models.CharField(max_length=1024, verbose_name="Заголовок")
    url = models.URLField(verbose_name="URL")
    slug = models.SlugField(unique=True, verbose_name="Текстовый идентификатор")
    short_text = models.TextField(verbose_name="Анонс")
    full_text = models.TextField(verbose_name="Полный текст")
    picture = models.ImageField(verbose_name="Изображение", upload_to="feeds/%Y/%m/%d")
    page_preview_picture = models.ImageField(verbose_name="Изображение для фона", upload_to="feeds/%Y/%m/%d")
    seo_keywords = models.TextField(
        verbose_name="Ключевые слова (SEO)",
        help_text="Не рекомендуется использовать более 255 символов",
        blank=True
    )
    seo_description = models.TextField(
        verbose_name="Описание (SEO)",
        help_text="Не рекомендуется использовать более 1024 символов",
        blank=True
    )
    is_visible = models.BooleanField(default=True, verbose_name="Отображать на сайте")
    date_published = models.DateTimeField(default=datetime.datetime.now, verbose_name="Дата публикации")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
