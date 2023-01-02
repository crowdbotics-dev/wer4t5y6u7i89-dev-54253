"""
WSGI config for wer4t5y6u7i89_dev_54253 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wer4t5y6u7i89_dev_54253.settings')

application = get_wsgi_application()
