from django.db import models


# 报告列表
class Report(models.Model):
    unicode = models.CharField(max_length=32)  # 查询数据  md5(data)
    data = models.TextField(default='')  # a json 查询数据
    count = models.IntegerField(default=0)
    type = models.CharField(max_length=10)  # personal | enterprise
    times = models.IntegerField(default=0)  # 搜索次数
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = u'report'