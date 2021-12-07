"""
WSGI config for courseraExtension project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

import site
import sys
# add the hellodjango project path into the sys.path
sys.path.append('C:/Users/mattt/CourseProject/courseraExtension')

# add the virtualenv site-packages path to the sys.path
sys.path.append('C:/Users/mattt/CourseProject/courseraExtension/myenv/lib/python3.5/site-packages')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'courseraExtension.settings')

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
# application = get_wsgi_application()
