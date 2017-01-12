from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from apps.search.views import SearchViewSet
from rest_framework_jwt.views import obtain_jwt_token
from apps.user.views import SignUpView
from apps.report.views import AliEnterpriseRelation, AliEnterpriseBase, AliEnterpriseProfile,PersonalProfile

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'search', SearchViewSet, base_name='search')

urlpatterns = [
    #搜索
    url('', include(router.urls)),
    #关注
    url(r'^attention/',include('apps.attention.urls')),
    #管理员
    url(r'^users/', include('rest_framework.urls', namespace='rest_framework')),
    #验证
    url(r'^sign_in', obtain_jwt_token),
    url(r'^sign_up', csrf_exempt(SignUpView.as_view())),
    #详情
    url(r'^report/', include('apps.report.urls')), #已废弃企业详情部分

    #新的ali企业报告详情
    url(r'^enterprise/profile', AliEnterpriseProfile.as_view()),
    url(r'^enterprise/relation', AliEnterpriseRelation.as_view()),
    url(r'^enterprise/base', AliEnterpriseBase.as_view()),

    #新的个人报告详情
    url(r'^personal/profile',PersonalProfile.as_view()),
]

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)