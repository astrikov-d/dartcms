DartCMS Modules configuration
=============================

You can specify custom runtime configuration for DartCMS modules.
We are using field `config` inside `modules.Module` model to define it. It holds JSON structure.

At the moment, only basic configuration is supported:

.. code-block:: javascript

    {
        "model": "my_app.ModelClass",
        "form": {
            "fields": ["name", "date_created"],
            "form_class": "my_app.MyFormClass"
        }
    }

`model` and `form_class` values must be specified in format `<app_label>.<class_name>`. Here we are assuming, that
modules with your models are named as `models` and modules with forms are named as `forms`. But you can redefine it
with settings `MODELS_MODULE_NAME` and `FORMS_MODULE_NAME`. For more information, please look inside
`dartcms.utils.loading` module.


Tiny modules management
=======================

From time to time, you need to manage some tiny model. It's overhead to create url scheme for such config.
We are lazy, so we are providing you mechanism of Dictionaries.
You can create `modules.Module` instance with `dict-` prefix in slug field. Then, your request in DartCMS will be
handled by special module named `dicts`. Use runtime configuration here to setup model class.