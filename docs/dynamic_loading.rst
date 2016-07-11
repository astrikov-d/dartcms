Dynamic Models Loading
======================

DartCMS package contains some useful apps, like news, feedback, shop etc. If you plan to redeclare these apps,
you can load models from these apps via `get_model` function:

.. code-block:: python

    from dartcms.core.loading import get_model

    Page = get_model('pages', 'Page')


First argument of this function - label of application. Second - name of model class.
This function checks if you have registered app named `pages` and then, if you have, returns you model `Page`.