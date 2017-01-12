from django.db import models


# 搜索记录 insert
class Search(models.Model):
    report_id = models.IntegerField() #报告id
    uid = models.IntegerField() #用户id
    type = models.CharField(max_length=10)  # personal | enterprise
    expire_in = models.IntegerField(default='7200') #过期时间
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = u'search'

class CheckThree(models.Model):
    search=models.CharField(max_length=256) #搜索序列
    phone=models.CharField(max_length=15) #手机
    meal=models.CharField(max_length=15) #套餐
    result=models.TextField()
    code=models.CharField(max_length=10,default='')
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = u'checkthree'

# 百融缓存 select,insert
class Bairong(models.Model):
    uid = models.IntegerField()  # 创建的用户
    unicode = models.CharField(max_length=32)  # 查询数据  md5 码
    data = models.TextField()  # 查询数据
    swift_number = models.CharField(max_length=64)  # 交换码
    type = models.CharField(max_length=20)  # 类型
    metadata = models.TextField()  # 源数据
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = u'bairong'


# 个人数据分析结果
class Personal(models.Model):
    unicode = models.CharField(max_length=32)  # 查询数据  md5 码
    report_id = models.IntegerField() #报告id
    idcard = models.CharField(max_length=20)  # 身份证
    cell = models.CharField(max_length=15)  # 手机
    name = models.CharField(max_length=20)  # 姓名
    tel = models.CharField(max_length=11)  # 座机
    mail = models.CharField(max_length=32)  # 邮箱
    bank_id = models.CharField(max_length=32)  # 银行卡
    flag = models.CharField(max_length=32)  # 类型
    metadata = models.TextField()  # 源数据
    formateddata = models.TextField()  # 格式化数据
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = u'personal'

class AliEnterpriseList(models.Model):
    unicode=models.CharField(max_length=32) #搜索标记
    comp=models.CharField(max_length=128) #查询内容
    content=models.TextField() #数据

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = u'ali_enterprise_list'


class AliEnterpriseData(models.Model):
    unicode = models.CharField(max_length=32)  # 搜索标记
    comp = models.CharField(max_length=128)  # 查询内容

    base = models.TextField()  # 企业全息画像_基本信息
    profile = models.TextField()  # 企业全息画像
    relation = models.TextField()  # 企业关系网络
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = u'ali_enterprise_data'