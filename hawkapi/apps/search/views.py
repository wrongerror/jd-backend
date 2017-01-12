from rest_framework import viewsets
from rest_framework.decorators import list_route
from apps.report.views import Search
from hawkeye.Tools import Response


class SearchViewSet(viewsets.ViewSet):
    """
    搜索个人报告
    url=/search/personal
    post={
          "name":"",
          "tel":"", #座机
          "bank_id":"", #银行卡
          "mail":"",
          "cell":"13881900441", #手机
          "id":"510922199003141852", #身份证

    }
    """
    @list_route(['POST'])
    def personal(self, request):
        id = request.data.get('id')  # 身份证
        assert id, Response.get_require('id')
        name = request.data.get('name')  # 姓名
        assert name, Response.get_require('name')
        cell = request.data.get('cell')  # 电话
        assert cell, Response.get_require('cell')

        # 其它信息,包括座机、银行卡、邮箱
        tel, bank_id, mail = (
            request.data.get('tel', ''),
            request.data.get('bank_id', ''),
            request.data.get('mail', '')
        )

        # 获取用户id
        uid = request.user.id
        # 返回搜索报告
        return Search.personal(uid, {'id': id, 'name': name, 'cell': cell, 'tel': tel, 'bank_id': bank_id, 'mail': mail})

    """
    搜索企业报告【废弃】
    url=/search/enterprise
    post={
        "biz_workfor":"" #公司名称
    }
    """

    @list_route(['POST'])
    def enterprise_old(self, request):
        biz_workfor = request.data.get('biz_workfor')
        assert biz_workfor, Response.get_require('biz_workfor')

        #获取用户id
        uid = request.user.id
        #返回搜索报告
        return Search.enterprise(uid, {'biz_workfor': biz_workfor})

    """
    搜索企业报告
    url=/search/enterprise
    post={
        "compName":""
    }
    """
    @list_route(['POST'])
    def enterprise(self,request):
        compName=request.data.get('compName')
        assert compName,Response.get_require('compName')

        # 获取用户id
        uid = request.user.id
        # 返回搜索列表
        return Search.enterprise_list_ali(uid, {'compName': compName})

