Available configuration
=======================

.. code-block:: python

    DARTCMS_ADDITIONAL_APPS_URLPATTERNS = []

Use setting `DARTCMS_ADDITIONAL_APPS_URLPATTERNS` to declare your additional apps. This setting should be iterable and
contain tuples with three parameters: application package name, path to application admin url scheme and application
URL slug.

Example:

.. code-block:: python

    DARTCMS_ADDITIONAL_APPS_URLPATTERNS = [
        ('awesome_app', 'app.awesome_app.admin_urls', 'awesome_app'),
        ('another_app', 'app.another_app.admin_urls', 'another_app'),
    ]


.. code-block:: python

    DARTCMS_TINYMCE_SETTINGS = {}

Use setting `DARTCMS_TINYMCE_SETTINGS` to declare additional custom options for TinyMCE. It should be dictionary with
custom options:

Example:

.. code-block:: python

    DARTCMS_TINYMCE_SETTINGS = {
        'content_css': '/static/css/style.css',
        'body_class': 'static-page-content'
    }

