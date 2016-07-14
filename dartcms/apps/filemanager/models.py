# coding: utf-8
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.utils.translation import ugettext_lazy as _


class Folder(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            error_messages={'unique': _('Folder with this name is already exists')})
    date_created = models.DateTimeField(auto_now_add=True)


class File(models.Model):
    folder = models.ForeignKey(Folder, related_name='files')
    path = models.FileField(upload_to='uploads/%Y/%m/%d', max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)


@receiver(pre_delete, sender=File)
def files_delete(sender, instance, **kwargs):
    instance.path.delete(False)
