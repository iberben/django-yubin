from django.contrib import admin
from django.conf.urls import include

try:
    # until django 4
    from django.conf.urls import url
except ImportError:
    # from django 4 and above
    from django.urls import re_path as url

from .views import IndexView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^yubin/', include('django_yubin.urls')),
    url(r'^admin/', admin.site.urls),
]
