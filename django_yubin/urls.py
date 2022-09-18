from django_yubin.views import MailHealthCheckView
try:
    # until django 4
    from django.conf.urls import url
except ImportError:
    # from django 4 and above
    from django.urls import re_path as url


urlpatterns = [
    url(r'^health$', MailHealthCheckView.as_view(), name='yubin_health'),
]
