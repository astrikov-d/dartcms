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