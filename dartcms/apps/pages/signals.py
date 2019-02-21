import random

from pytils.translit import slugify
from django.db.models import F, Max


def pre_save_handler(sender, **kwargs):
    """
    Sorting pages while saving.
    """
    instance = kwargs.get('instance')
    if instance:
        if instance.slug == '':
            slug = slugify(instance.title)
            try:
                sender.objects.get(module=instance.module, slug=slug)
                instance.slug = slug + '-%s' % round(random.random() * 1000)
            except sender.DoesNotExist:
                instance.slug = slug

        instance.url = instance.page_url

        current_level_pages = sender.objects.filter(parent=instance.parent)

        if not current_level_pages.exists():
            instance.sort = 1

        if not instance.id or instance.sort == 0:
            max_sort = current_level_pages.aggregate(Max('sort'))
            s = max_sort.get('sort_max')
            instance.sort = s + 1 if s else 1
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
