"""
WSGI config for my_django18_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""



from django.core.wsgi import get_wsgi_application
from django.conf import settings

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_django18_project.settings")

application = get_wsgi_application()

if not settings.DEBUG:
	try:
		from dj_static import Cling
		application = Cling(get_wsgi_application())
	except:
		pass
