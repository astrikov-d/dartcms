Generic Views
=============

DartCMS admin panel is based on few generic views. You will use them in your apps as base for their management tools.
Basically, these views are implementing CRUD features for your apps.


Views Configuration
-------------------

As configuration mechanism in the DartCMS, we will use simple class named `DartCMSConfig`.
It's placed into `dartcms.utils.config` package. Here is it's implementation:

.. code-block:: python

    class DartCMSConfig(object):
        config = {}

        def __init__(self, config):
            self.config = config

        @property
        def base(self):
            return {
                ...
            }

        @property
        def grid(self):
            config = self.base
            config.update(self.config['grid'])
            return config

        @property
        def form(self):
            config = self.base
            config.update(self.config['form'])
            return config

As you can see, it's pretty simple. You can pass some `dict` to its constructor and then access grid and form confiration
via `grid` and `form` properties of resulted object. In the next examples, you'll see how to do it.


dartcms.views.GridView
----------------------

This view is inherited from `django.views.generic.ListView` and implements functionality for datagrids.
`dartcms.views.GridView` class includes some configuration options:


.. code-block:: python

    class GridView(AdminMixin, ListView):
        ...
        grid_columns = (
            ('name', _('Title'), 'string', '70%'),
            ('date_created', _('Date created'), 'datetime', '30%'),
        )
        grid_actions = ()

`grid_columns` property determines which fields from your model will be rendered as datagrid columns. This property
must be a tuple, which contains items with column configuration:

- Model's field name
- Column name
- Data type. Possible values: 'string', 'datetime', 'time', 'date', 'boolean', 'image'
- Width in percents

`grid_actions` property determines which actions can be done with each row. Default actions are:

- Insert
- Update
- Delete

By defining this property, you can add some additional actions to your datatable.

This property must be a tuple, which contains items with action configuration:

.. code-block:: python

    'grid_actions': (
        ('change-password', _('Change Password'), 'edit'),
    )

This example contains one additional action to change password.

First element if tuple is URL for redirect after user click on action button. In the example, user will be redirected to
URL like `/<module_slug>/change-password/<row_pk>/`. Of course, you should define this URL in your app URL scheme:

.. code-block:: python

    from django.conf.urls import url
    from django.contrib.auth.models import User
    from django.utils.translation import ugettext_lazy as _

    from dartcms.utils.config import DartCMSConfig
    from dartcms.views import DeleteObjectView, GridView
    from forms import UserForm
    from views import ChangePasswordView, CMSUserInsertView, CMSUserUpdateView

    config = DartCMSConfig({
        'model': User,
        'grid': {
            'grid_columns': (
                ('username', _('Username'), 'string', '60%'),
                ('last_login', _('Last Login'), 'datetime', '20%'),
                ('is_staff', _('Staff'), 'boolean', '10%'),
                ('is_active', _('Active'), 'boolean', '10%'),
            ),
            'grid_actions': (
                ('change-password', _('Change Password'), 'edit'),
            )
        },
        'form': {
            'form_class': UserForm
        }
    })

    urlpatterns = [
        url(r'^$', GridView.as_view(**config.grid), name='index'),
        ...
        url(r'^change-password/(?P<pk>\d+)/$', ChangePasswordView.as_view(), name='change_password'),
    ]



This code snippet illustrates how DartCMS app named `users` works with this custom grid action. As you can see, we have
pretty simple config here: we are passing `model` keyword argument (because our `GridView` is inherited from
Django's `ListView`).


dartcms.views.InsertObjectView
------------------------------

This view implements insert features for your model. It's inherited from `django.views.generic.CreateView` and can be
configured in a same way:

.. code-block:: python

    ...

    config = DartCMSConfig({
        'model': User,
        ...
        'form': {
            'form_class': UserForm
        }
    })

    urlpatterns = [
        url(r'^insert/$', CMSUserInsertView.as_view(**config.form), name='insert'),
    ]


dartcms.views.UpdateObjectView
------------------------------

This view implements update features for your model. It's inherited from `django.views.generic.UpdateView` and can be
configured in a same way:

.. code-block:: python

    ...

    config = DartCMSConfig({
        'model': User,
        ...
        'form': {
            'form_class': UserForm
        }
    })

    urlpatterns = [
        url(r'^update/(?P<pk>\d+)/$', CMSUserUpdateView.as_view(**config.form), name='update'),
    ]


dartcms.views.DeleteObjectView
------------------------------

This view implements delete features for your model. It's inherited from `django.views.generic.DeleteView` and can be
configured in this way:

.. code-block:: python

    ...

    config = DartCMSConfig({
        'model': User,
    })

    urlpatterns = [
        url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
    ]

Note, that here we do not need form configuration, so we will pass only base config here - `model` keyword argument.


dartcms.views.JSONView
----------------------

This is pretty simple view to render response as JSON. Nothing special here. Example:

.. code-block:: python

    from dartcms.views import JSONView


    class MyView(JSONView):
        def get_data(self, context):
            return {
                'result': True,
                'data': {'foo': 'bar'}
            }


Working with Inlines
--------------------

If you want to add related models creation into your forms, you can use special views:
`dartcms.views.InsertObjectWithInlinesView` and `dartcms.views.UpdateObjectWithInlinesView`.

These views are based on the Django Extra Views package, so you
can find full documentation here - https://github.com/AndrewIngram/django-extra-views.