import os, sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../conf')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.dev.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
