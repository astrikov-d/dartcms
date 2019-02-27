from dartcms.apps.users.models import UserGroup
from dartcms.utils.config import DartCMSConfig
from django.forms.models import modelform_factory

app_name = 'groups'

config = DartCMSConfig({
    'model': UserGroup,
    'grid': {
        'grid_columns': [
            {'field': 'name', 'width': '100%'},
        ]
    },
    'form': {
        'form_class': modelform_factory(model=UserGroup, exclude=['users'])
    }
})

urlpatterns = config.get_urls()
