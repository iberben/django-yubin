# -*- coding: utf-8 -*-

from django.conf.urls import include

try:
    # until django 4
    from django.conf.urls import url
except ImportError:
    # from django 4 and above
    from django.urls import re_path as url


urlpatterns = [
    url(r'^yubin/', include('django_yubin.urls')),
]
