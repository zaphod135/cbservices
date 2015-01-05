"""
WSGI config for chuck project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
path = '/var/www/cbservices/chuck/'

if path not in sys.path:
          sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chuck.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
