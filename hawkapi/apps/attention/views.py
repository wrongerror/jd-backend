from rest_framework.views import APIView
from apps.attention.models import Attention as AttentionModel
from apps.attention.serializers import AttentionSerializer
from hawkeye.Tools import Response
from apps.search.models import Search as SearchModel
from apps.report.models import Report as ReportModel


class List(APIView):
    # 关注列表
    def get(self, request):
        uid = request.user.id
        attentions = AttentionModel.objects.filter(uid=uid,deleted_at=None).order_by('-updated_at').all()
        if len(attentions) > 0:
            serializer = AttentionSerializer(attentions, many=True)
            data = serializer.data
        else:
            data = []
        return Response(data)

#关注
class Attention(APIView):
    """
    关注
    url=/attention/{report_id}
    put方法
    """
    def put(self, request, pk):
        pk = int(pk)
        uid = request.user.id
        attention = AttentionModel.objects.filter(uid=uid, report_id=pk).first()
        if attention is None: #创建关注
            search = SearchModel.objects.filter(uid=uid, report_id=pk).first()
            if search is None:
                return Response(4101)
            report = ReportModel.objects.get(id=pk)
            attention=AttentionModel.objects.create(
                report_id=report.id,
                uid=uid,
                type=report.type,
                details=report.data
            )
        else:#查询到之前关注过标记为关注
            attention.restore()

        return Response({'report_id':attention.report_id,'details':attention.details,'type':attention.type})

    """
    取消关注
    url=/attention/{report_id}
    delete
    """
    def delete(self, request, pk):
        pk = int(pk)
        uid = request.user.id
        attention = AttentionModel.objects.filter(uid=uid, report_id=pk).first()
        if attention is None:
            return Response(4101)
        attention.delete() #取消标记关注
        return Response({'report_id':attention.report_id,'type':attention.type})