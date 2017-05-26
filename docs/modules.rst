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
        },
        "grid": {
            "grid_columns":[
                {
                    "field": "name",
                    "label": "Name",
                    "width": "50%"
                },
                {
                    "field": "date_created",
                    "label": "Date created",
                    "type": "DATETIME",
                    "width": "50%"
                }
            ],
            "search":[
                "name",
                "date_created"
            ],
            "additional_grid_actions": [
                {
                    "url": "some-action", "label": _("Some action"), "icon": "edit",
                    "required_permissions": "__all__"
                }
            ],
            "model_properties": ["some_calculated_property"]
        }
    }

`model` and `form_class` values must be specified in format `<app_label>.<class_name>`. Here we are assuming, that
modules with your models are named as `models` and modules with forms are named as `forms`. But you can redefine it
with settings `MODELS_MODULE_NAME` and `FORMS_MODULE_NAME`. For more information, please look inside
`dartcms.utils.loading` module.

If you want to specify some additional grid action (button) at grid page, you should add `additional_grid_actions`
option into settings. This option should be a `list` of `dicts`. Each `dict` represents grid action. It can contain
these params:
- `url`. Url for redirect from base grid page.
- `label`. Label for the button.
- `icon`. Icon for the button.
- `required_permissions`. Permissions, required to show button. Can be a single string `__all__` if action requires all
permissions from user (insert, update and delete). Or a list, for example `['insert', 'update']`.

Tiny modules management
=======================

From time to time, you need to manage some tiny model. It's overhead to create url scheme for such config.
We are lazy, so we are providing you mechanism of Dictionaries.
You can create `modules.Module` instance with `dict-` prefix in slug field. Then, your request in DartCMS will be
handled by special module named `dicts`. Use runtime configuration here to setup model class.