"""
WSGI config for PI_2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Update this line to match the new structure
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto-integrador-ii.settings')

application = get_wsgi_application()