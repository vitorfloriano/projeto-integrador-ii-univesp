"""
ASGI config for PI_2 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Update this line to match the new structure
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto-integrador-ii.settings')

application = get_asgi_application()