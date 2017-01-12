from datetime import datetime
from django.db import models

# 关注列表
class Attention(models.Model):
    report_id = models.IntegerField()
    uid = models.IntegerField(default=0)
    type = models.CharField(max_length=10)  # personal | enterprise
    details = models.TextField(default='')  # name, cell...
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True,null=True)  # 标记删除/已取消关注

    class Meta:
        db_table = u'attention'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = datetime.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()