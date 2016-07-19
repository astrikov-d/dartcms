Forking Applications
====================

Of course you'll want to write your own custom application and manage it with DartCMS.
You have two options to do that:

1. Use existing DartCMS app with small changes.
2. Write app from scratch and manage it with DartCMS.

Changing existing applications
------------------------------

In your `settings.py` file you have something like that:

.. code-block:: python

    from dartcms import get_dartcms_core_apps

    ...

    INSTALLED_APPS = [
        ...
    ] + get_dartcms_core_apps()

You can pass optional parameter `replacements` to `get_dartcms_core_apps` function:

.. code-block:: python

    INSTALLED_APPS = [
        ...
    ] + get_dartcms_core_apps(replacements=['app.feeds'])


This will replace DartCMS's app named `feeds` with your app `app.feeds`.


You can re-declare DartCMS `feeds` app's models in your `app.feeds.models` module like that:

.. code-block:: python

    # app: custom_app

    from django.db import models

    import dartcms

    from dartcms.apps.feeds.models import AbstractFeedItem


    __all__ = ['FeedItem']
    __all__.extend(dartcms.discover_models('feeds', __all__))


    class FeedItem(AbstractFeedItem):
        custom_field = models.CharField(max_length=255)


By doing this, you'll replace DartCMS `FeedItem` model with your own. And DartCMS will manage this model.

By calling `dartcms.discover_models('feeds', __all__)` function, you'll append non-declared models from
DartCMS to your application.


Writing application from scratch
--------------------------------

If you need some application that do not exist in DartCMS, you can write your own and point DartCMS to it.

1. Create application with such structure:

.. code-block:: bash

    --<app_name>
        --__init__.py
        --models.py
        --urls.py

2. Write some code in `models.py`:

.. code-block:: python

    # models.py

    from django.db import models


    class TinyModel(models.Model):
        foo = models.CharField(max_length=255)
        bar = models.DateTimeField()


3. Create url scheme:

.. code-block:: python

    # urls.py

    from django.conf.urls import url, include
    from django.forms import modelform_factory

    from dartcms.utils.config import DartCMSConfig
    from dartcms.views import GridView, UpdateObjectView, DeleteObjectView, InsertObjectView
    from .models import TinyModel

    config = DartCMSConfig({
        'model': TinyModel,
        'grid': {
            'grid_columns': [
                # Keys 'label', 'type' are optional here.
                {'field': 'foo', 'label': _('Foo'), 'type': 'string', 'width': '70%'},
                {'field': 'bar', 'label': _('Bar'), 'type': 'datetime', 'width': '30%'},
            ],
        },
        'form': {
            'form_class': modelform_factory(TinyModel, exclude=[]),
        }
    })

    urlpatterns = [
        url(r'^$', GridView.as_view(**config.grid), name='index'),
        url(r'^insert/$', InsertObjectView.as_view(**config.form), name='insert'),
        url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**config.form), name='update'),
        url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
    ]


4. Add `DARTCMS_ADDITIONAL_APPS_URLPATTERNS` setting to your `settings.py` file:

.. code-block:: python

    DARTCMS_ADDITIONAL_APPS_URLPATTERNS = [
        ('some-url', '<app_name>.urls', '<app_name>'),
    ]

This setting must be a list containing tuples. Tuple elements:

- First: some url to navigate DartCMS user to your application management (without slashes).
- Second: path to your application's url scheme.
- Third: namespace of your application.

In the DartCMS core this setting is used in this way:

.. code-block:: python

    additional_apps = getattr(settings, 'DARTCMS_ADDITIONAL_APPS_URLPATTERNS', [])

    if additional_apps:
        additional_patterns = []
        for app in additional_apps:
            additional_patterns.append(url(r'^%s/' % app[0], include(app[1], namespace=app[2])))

        urlpatterns += additional_patterns

5. Add new DartCMS module with Django admin and set it's slug as url of your application (first param in each tuple).
6. Navigate your browser to DartCMS and you'll see your application in the left navigation menu.
