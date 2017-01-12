import hashlib
from django.utils.encoding import force_bytes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from hawkeye.Tools import Response
from apps.user.models import Users as UserInfo


"""
注册接口
"""
class SignUpView(APIView):
    permission_classes = (AllowAny,)

    """
    post={
        "account":"", #账户
        "password":"e10adc3949ba59abbe56e057f20f883e",   #md5 加密
        "name":"", #姓名
        "avatar":"", #头像
    }
    """
    def post(self, request):
        account = request.data.get('account', None)
        password = request.data.get('password', None)
        name = request.data.get('name', None)
        avatar = request.data.get('avatar', None)

        assert account, 'account is required'
        assert password, 'password is required'
        assert name, 'name is required'
        if avatar is None:
            avatar = ''

        user, created = UserInfo.objects.get_or_create(account=account)
        if created:#创建用户
            user.password = hashlib.md5(force_bytes(password)).hexdigest()
            user.name = name
            user.avatar = avatar

            user.save()

            #获取token
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response({
                'token':  token,
                'name':   name,
                'avatar': avatar
            })
        else:#用户已存在
            return Response(None, 4001)