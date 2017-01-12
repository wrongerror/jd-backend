from __future__ import unicode_literals

from django.conf.urls import url
from apps.attention.views import Attention, List

urlpatterns = [
    #关注列表 attention/list
    url(r'^list$', List.as_view()),
    url(r'^(?P<pk>\d+)$', Attention.as_view()),
]