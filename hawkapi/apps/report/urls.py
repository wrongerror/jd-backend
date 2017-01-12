from __future__ import unicode_literals

from django.conf.urls import url
from apps.report.views import Details

urlpatterns = [
    #报告详情
    url(r'^(?P<id>\d+)/(?P<meal>.*)$', Details.as_view()),
]