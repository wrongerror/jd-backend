from django.conf.urls import url
from apps.search import views
"""
未使用
"""
urlpatterns=[
    url(r'^index',views.index),
]