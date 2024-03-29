from __future__ import unicode_literals
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
settings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


application = Cling(get_wsgi_application())