import json
import time
from datetime import datetime
import urllib

from rest_framework.views import APIView

from apps.report import ReportMap
from apps.search.models import Bairong as BairongModel, AliEnterpriseList, AliEnterpriseData, CheckThree
from hawkeye import Tools
from urllib.parse import urlencode
from apps.report.models import Report as ReportModel
from apps.search.models import Personal as PersonModel
from apps.search.models import Search as SearchModel
from apps.attention.models import Attention as AttentionModel
from hawkeye.Tools import Response, md5
from apps.aliyun.api.gateway.sdk import client
from apps.aliyun.api.gateway.sdk.http import request
from apps.aliyun.api.gateway.sdk.common import constant

"""
百融缓存
"""


class BsApi:
    whole_meal = 'SpecialList_c,ApplyLoan,Location,TelecomCheck,LoanEquipment,RegisterEquipment,SignEquipment,EquipmentCheck,Execution,TelCheck,TrafViol,EduLevel,IdTwo,IdPhoto,FaceComp,FaceRecog,BankFour,Stability_c,Consumption_c,Media_c,AccountchangeMonth,AccountChangeDer,PayConsumption,PayConsumptionDer,AirTravel,SocietyRelation,TelConsumeCTCC_d,TelPeriodCUCC_d,TelStateCUCC_d,PerInvest,scorebank,scoreconsoff,scoreconsoffv2,brcreditpoint,scorepettycashv1,ScoreCust,RuleSpecialList,RuleApplyLoan,RuleAccountChange,RuleScore,RuleExecution,RuleLoan_web,RuleLoan_android,RuleLoan_ios,RuleRegister_web,RuleRegister_android,RuleRegister_ios,RuleLog_web,RuleLog_android,RuleLog_ios'
    token = None
    host = 'api.100credit.cn'

    def get_token(self):
        url = '/bankServer2/user/login.action?userName=jindingcf&password=jindingcf&apiCode=3000164'
        statu, headers, response = Tools.post(self.host, url, connect='https')
        return response.get('tokenid', None)
    def three(self,data):
        if self.token is None:
            self.token = self.get_token()
        if self.token is None:
            return None

        ##缓存

        url = '/HainaApi/data/getData.action'
        cell=data['cell']
        id=data['id']
        name=data['name']

        start=cell[0:3]
        if start in ['134','135','136','137','138','139','150','151','152','157','158','159','178','182','183','184','187','188']:
            meal='MobileThree'
        elif start in ['133','153','177','180','181','189']: #电信
            meal='TelecomThree'
        elif start in ['130','131','132','155','156','176','185','186']: #联通
            meal='UnicomThree'
        else :
            return False
        data={'id':id,'name':name,'cell':cell,'meal':meal}
        search_data=json.dumps(data, ensure_ascii=False, sort_keys=True)

        three = CheckThree.objects.exclude(code='').filter(search=search_data).first()
        if three is not None:
            return three.code

        statu, headers, result = self.post(url, data)
        if result is not None:
            try:
                if isinstance(result,str):
                    _result=json.loads(result.replace("'",'"'))
                else:_result=result
                code=_result['product']['result']
                CheckThree.objects.create(
                    result=result,
                    phone=cell,
                    search=search_data,
                    meal=meal,
                    code=code
                )
                return code
                ####
                # 0:查无此号或手机号非实名认证
                # 1:均一致
                # 2:均不一致
                # 4:姓名手机号一致，姓名身份证号不一致
                # 1001:请求参数格式错误
                # 1002:接口验证信息无效（ip地址不在白名单、token无效等）
                # 2001:没有可用余额、没有可用次数
                # 2002:没有可用时间
                # 2005:请求超时
                # 9999:系统错误
                ####
            except:
                pass
        return '-1'

    def search(self, uid, unicode, _data, package, flag=None,refresh=False):
        if flag is None:
            package = ''.join(['p_', package])
        else:
            package = ''.join(['e_', package])
        bairong=None
        if not refresh:
            bairong = BairongModel.objects.filter(unicode=unicode, type=package).first()
        if bairong is None:
            if self.token is None:
                self.token = self.get_token()
            if self.token is None:
                return None

            data = _data.copy()
            if package == 'p_bank':
                url = '/bankServer2/data/terData.action'
                data['meal'] = self.whole_meal
                data['cell'] = [data['cell']]
            elif package == 'p_haina':
                url = '/HainaApi/data/getData.action'
                data['meal'] = 'PerInvest'
            elif package == 'aird1':
                url = '/HainaApi/data/getData.action'
                data['meal'] = 'AirTravel_d1'
            elif package == 'airh1':
                url = '/HainaApi/data/getData.action'
                data['meal'] = 'AirTravel_h1'
            elif package == 'e_BizInfo':  # 基本信息
                url = '/HainaApi/data/getData.action'
                data['meal'] = 'BizInfo'
                data['id'] = '110101199002021234'
                data['cell'] = '18800011111'
                data['name'] = '张三'
            elif package == 'e_BizInvest_q':
                url = '/HainaApi/data/getData.action'
                data['meal'] = 'BizInvest_q'
                data['id'] = '110101199002021234'
                data['cell'] = '18800011111'
                data['name'] = '张三'
            elif package == 'e_BizExecution':
                url = '/HainaApi/data/getData.action'
                data['meal'] = 'BizExecution'
                data['id'] = '110101199002021234'
                data['cell'] = '18800011111'
                data['name'] = '张三'
            elif package == 'e_BizRelationship_q':
                url = '/HainaApi/data/getData.action'
                data['meal'] = 'BizRelationship_q'
                data['id'] = '110101199002021234'
                data['cell'] = '18800011111'
                data['name'] = '张三'
                data['KeyNo'] = ''
                data['searchKey'] = ''
                # data['biz_workfor']
                # unset(data['biz_workfor'])
            else:
                return None

            statu, headers, result =self.post( url, data)
            if result is None:
                return {}
            else:
                BairongModel.objects.create(uid=uid, unicode=unicode, data=data, type=package,
                                            swift_number=result.get('swift_number', ''), metadata=json.dumps(result))
        else:
            result = json.loads(bairong.metadata)
        return result

    def post(self,url,data):
        if isinstance(data, dict):
            data = json.dumps(data, sort_keys=True, ensure_ascii=False)
            data = data.replace(' ', '')

        checkcode = md5(''.join([data, md5(''.join(['3000164', self.token]))]))
        post_data = urllib.parse.urlencode(
            {'apiCode':      3000164, 'tokenid': self.token,
             'interCommand': 1000, 'jsonData': data,
             'checkCode':    checkcode
             })
        return Tools.post(self.host, url, post_data,
                                            headers={'Content-Type': 'application/x-www-form-urlencoded'},
                                            connect='https')


"""
阿里企业接口
"""


class AliEnterprise:
    host = 'http://ei-api.data.aliyun.com'
    appKey = '23464631'
    appSecret = b'f027e328aa3a164f07009163b3963cda'
    token = 'efed1180814011e693d43566a98054ea'

    @staticmethod
    def get_postdata(compname):
        return {"compName": compname, "token": AliEnterprise.token}

    @staticmethod
    def post(url, compname, host=None):
        if host is None:
            host = AliEnterprise.host
        cli = client.DefaultClient(app_key=AliEnterprise.appKey, app_secret=AliEnterprise.appSecret)
        req_post = request.Request(host=host, protocol=constant.HTTP, url=url, method="POST", time_out=30000)
        body = AliEnterprise.get_postdata(compname)
        req_post.set_body(body)
        req_post.set_content_type(constant.CONTENT_TYPE_FORM)
        return cli.execute(req_post)

    ###企业全息画像_模糊查询
    @staticmethod
    def get_complete_by_name(compname):
        url = '/getCompleteByName'
        return AliEnterprise.post(url, compname)

    ###企业全息画像_基本信息
    @staticmethod
    def get_progile_by_name(compname):
        url = '/getProfileByName'
        return AliEnterprise.post(url, compname)

    ###企业全息画像
    @staticmethod
    def profile(compname):
        url = '/enterprise/profile'
        return AliEnterprise.post(url, compname)

    ###企业关系网络
    @staticmethod
    def relation(compname):
        url = '/getRelation'
        host = 'http://ei-relation.data.aliyun.com'
        return AliEnterprise.post(url, compname, host)


class Search:
    """
    获取个人报告
    """

    @staticmethod
    def personal(uid, data):
        bank_flag = {
            'flag_specialList_c':      '',  # 特殊名单核查数据
            'flag_applyLoan':          '',  # 多次申请核查数据
            'flag_location':           '',  # 地址信息核对数据
            'flag_loanequipment':      '',  # 设备借款信息数据
            'flag_registerequipment':  '',  # 注册设备信息数据
            'flag_signequipment':      '',  # 登录设备信息数据
            'flag_execution':          '',  # 法院被执行人数据
            'flag_stability_c':        '',  # 稳定性评估数据
            'flag_consumption_c':      '',  # 商品消费评估数据
            'flag_media_c':            '',  # 媒体阅览评估数据
            'flag_accountChangeMonth': '',  # 月度收支等级评估数据
            'flag_payConsumption':     '',  # 支付消费评估数据
            'flag_airTravel':          '',  # 航旅行为评估数据
            'flag_societyrelation':    '',  # 社交关系评估数据
            'flag_score':              '',  # base  百融评分数据
            'flag_equipmentcheck':     ''  # 设备信息核查数据
        }
        haina_flag = {
            'flag_perinvest': '',  # 个人对外投资数据
        }
        air_d1_flag={
            'flag_airtravel_d1':''
        }
        air_h1_flag={
            'flag_airtravel_h1':''
        }
        # 获取数组交集
        def array_intersect_key(_data, keys):
            newdict = {}
            for x in _data:
                if x in keys:
                    newdict[x] = _data[x]
            return newdict

        def save_haina(data, hainas):
            pass

        #存储航旅记录
        def save_air(_data,air,_type):
            try:
                PersonModel.objects.bulk_create(
                    unicode=_data['unicode'],
                    flag=_type,
                    formateddata=json.dumps(air,ensure_ascii=False),
                    report_id=_data['report_id']
                )
            except:pass

        # 存储bank接口
        def save_bank(_data, bank):
            create = []

            # 评分 basic
            flag_base = array_intersect_key(bank, ReportMap.flag_base)
            if len(flag_base) > 0:
                create.append(PersonModel(
                    unicode=_data['unicode'],
                    flag='score',
                    formateddata=json.dumps(flag_base),
                    report_id=_data['report_id']
                ))

            # 申请记录 applyloan:多次申请 speciallist_c:特殊名单
            flag_apply = array_intersect_key(bank, ReportMap.flag_apply)
            if len(flag_apply) > 0:
                create.append(PersonModel(
                    unicode=_data['unicode'],
                    flag='apply',
                    formateddata=json.dumps(flag_apply),
                    report_id=_data['report_id']
                ))

            # 行为评估 behavior
            flag_behavior = array_intersect_key(bank, ReportMap.flag_behavior)
            if len(flag_behavior) > 0:
                create.append(PersonModel(
                    unicode=_data['unicode'],
                    flag='behavior',
                    formateddata=json.dumps(flag_behavior),
                    report_id=_data['report_id']
                ))

            # 消费评估
            flag_consume = array_intersect_key(bank, ReportMap.flag_consume)
            if len(flag_consume) > 0:
                create.append(PersonModel(
                    unicode=_data['unicode'],
                    flag='consume',
                    formateddata=json.dumps(flag_consume),
                    report_id=_data['report_id']
                ))

            if len(create) > 0:
                PersonModel.objects.bulk_create(create)

        # 重新存储bank接口
        def resave_bank(_data, bank):
            create = []
            time_now = datetime.now()
            # 评分  basic
            # if bank == null: return
            flag_base = array_intersect_key(bank, ReportMap.flag_base)
            if len(flag_base) > 0:
                r = PersonModel.where(unicode=_data['unicode'], flag='score').first()
                if r is None:
                    create.append(PersonModel(
                        unicode=_data['unicode'],
                        flag='score',
                        formateddata=json.dumps(flag_base),
                        created_at=time_now,
                        report_id=_data['report_id']
                    ))
                else:
                    r.formateddata = json.dumps(flag_base)
                    r.updated_at = time_now
                    r.save()
            # 申请记录 applyloan:多次申请 speciallist_c:特殊名单
            flag_apply = array_intersect_key(bank, ReportMap.flag_apply)
            if len(flag_apply) > 0:
                r = PersonModel.where('unicode', _data['unicode']).where('flag', 'apply').first()
                if r is None:
                    create.append(PersonModel(
                        unicode=_data['unicode'],
                        flag='apply',
                        formateddata=json.dumps(flag_apply),
                        created_at=time_now,
                        updated_at=time_now,
                        report_id=_data['report_id']
                    ))
                else:
                    r.formateddata = json.dumps(flag_apply)
                    r.updated_at = time_now
                    r.save()
            # 行为评估 behavior
            flag_behavior = array_intersect_key(bank, ReportMap.flag_behavior)
            if len(flag_behavior) > 0:
                r = PersonModel.where('unicode', _data['unicode']).where('flag', 'behavior').first()
                if r is None:
                    create.append(PersonModel(
                        unicode=_data['unicode'],
                        flag='behavior',
                        formateddata=json.dumps(flag_behavior),
                        created_at=time_now,
                        updated_at=time_now, report_id=_data['report_id']
                    ))
                else:
                    r.formateddata = json.dumps(flag_behavior)
                    r.updated_at = time_now
                    r.save()
            # 消费评估
            flag_consume = array_intersect_key(bank, ReportMap.flag_consume)
            if len(flag_consume) > 0:
                r = PersonModel.where(unicode=_data['unicode'], flag='consume').first()
                if r is None:
                    create.append(PersonModel(
                        unicode=_data['unicode'],
                        flag='consume',
                        formateddata=json.dumps(flag_consume),
                        created_at=time_now,
                        updated_at=time_now,
                        report_id=_data['report_id']
                    ))
                else:
                    r.formateddata = json.dumps(flag_consume)
                    r.updated_at = time_now
                    r.save()
            if create is not None:
                PersonModel.insert(create)

        # 响应应接口
        def init(data):
            # 封装md5
            new_data={'id':data['id'],'name':data['name'],'cell':data['cell']}
            if data.get('mail') != '':
                new_data['mail']=data['mail']
            if data.get('tel') != '':
                new_data['tel'] = data['tel']
            if data.get('bank_id') != '':
                new_data['bank_id'] = data['bank_id']
            data=new_data

            data_str = json.dumps(data,ensure_ascii=False,sort_keys=True)
            data_str=data_str.replace(' ','')

            unicode_data = md5(data_str)

            bsapi = BsApi()
            # 验证三要素
            three = bsapi.three(data)
            if three is None:  # 获取失败
                return Response(6001)

            # if three is not '1':
            #     return Response({'result_three': three})

            # 查询本地报告
            report = ReportModel.objects.filter(unicode=unicode_data).first()
            if report is None:
                # 在线获取报告
                banks = bsapi.search(uid, unicode_data, data, 'bank')
                count = 0
                for f in banks:  # 计算查询结果数量
                    if f in bank_flag and banks[f] is '1':
                        count += 1
                # 海纳接口
                hainas = bsapi.search(uid, unicode_data, data, 'haina')
                for f in hainas:  # 获取获取结果数量
                    if f in haina_flag and f is not None and hainas[f] is not None:
                        count += 1
                ###新航旅接口
                AirTravel_d1=bsapi.search(uid,unicode_data,data,'aird1')
                AirTravel_h1=bsapi.search(uid,unicode_data,data,'airh1')

                data['unicode'] = unicode_data

                # 保存报告
                if count != 0:
                    report = ReportModel.objects.create(
                        unicode=unicode_data,
                        data=data_str,
                        count=count,
                        type='personal',
                        times=1
                    )
                    report_id = report.id
                    data['report_id'] = report_id
                    save_bank(data, banks)  # 存储bank
                    save_haina(data, hainas)  # 存储haina
                    save_air(data,AirTravel_d1,'aird1')
                    save_air(data,AirTravel_h1,'airh1')
                else:
                    report_id = 0

            else:
                report_id = report.id
                if time.mktime(report.created_at.timetuple()) < time.mktime(
                        time.strptime('2016-08-14', '%Y-%m-%d')):  # 在这个时间后的数据实施更新缓存
                    report.created_at = datetime.now()
                    banks = BsApi.search(uid, unicode_data, data, 'bank')
                    hainas = BsApi.search(uid, unicode_data, data, 'haina')
                    data['unicode'] = unicode_data
                    data['report_id'] = report_id
                    resave_bank(data, banks)  # 更新缓存
                count = report.count
                report.times += 1
                report.save()

            # 创建搜索记录
            SearchModel.objects.create(
                report_id=report_id,
                uid=uid,
                type='personal',
                expire_in=7200
            )
            return Response({'count': count, 'id': report_id,'result_three':three})

        return init(data)
        # bsapi = BsApi()
        # return Response(bsapi.get_token())

    """
    获取企业报告【废弃】
    """

    @staticmethod
    def enterprise(uid, data):
        # 查询本地报告
        data_str = json.dumps(data, sort_keys=True, ensure_ascii=False).replace(' ', '')
        unicode_data = md5(data_str)
        report = ReportModel.objects.filter(unicode=unicode_data).first()

        if report is None:
            # 在线抓取报告
            # 基本信息
            bsapi = BsApi()
            BizInfo = bsapi.search(uid, unicode_data, data, 'BizInfo', True)
            if BizInfo is None:
                return Response(6001)

            # 对外投资
            BizInvest_q = bsapi.search(uid, unicode_data, data, 'BizInvest_q', True)
            # 企业不良信息
            BizExecution = bsapi.search(uid, unicode_data, data, 'BizExecution', True)
            count = 0

            # 处理搜索后的数量
            if 'flag' in BizInfo and 'flag_bizinfo' in BizInfo['flag'] and 'product' in BizInfo \
                    and 'data' in BizInfo['product'] and 'result' in BizInfo['product']['data']:
                count += 1
            if 'flag' in BizInvest_q and 'flag_bizinvest_q' in BizInvest_q['flag'] \
                    and 'product' in BizInvest_q and BizInvest_q['product'].get('Status') is '200':
                count += 1
            if 'flag' in BizExecution and 'flag_bizexecution' in BizExecution['flag'] \
                    and 'product' in BizExecution and 'totalNum' in BizExecution['product']:
                count = count + BizExecution['product']['totalNum']

            data['unicode'] = unicode_data

            # 保存 报告
            if count != 0:
                report = ReportModel.objects.create(
                    unicode=unicode_data,
                    data=data_str,
                    count=count,
                    type='enterprise',
                    times=1
                )
                report_id = report.id
                data['report_id'] = report_id

            else:
                report_id = 0
        else:
            report_id = report.id
            count = report.count
            report.times += 1
            report.save()

        # 创建搜索记录
        SearchModel.objects.create(
            report_id=report_id,
            uid=uid,
            type='enterprise',
            expire_in=7200
        )
        return Response({'count': count, 'id': report_id})

    """企业模糊查询（阿里）"""

    @staticmethod
    def enterprise_list_ali(uid, data):
        compName = data['compName']
        uniq = md5(compName)  # 查询码
        try:
            alienterprise, created = AliEnterpriseList.objects.get_or_create(unicode=uniq)
            if created or alienterprise.content is None:  # 在线获取
                statuCode, headers, data = AliEnterprise.get_complete_by_name(compName)
                if statuCode is 200:
                    if not data is None:
                        if isinstance(data, bytes): data = data.decode("utf-8")
                        alienterprise.content = data
                        alienterprise.comp = compName
                        alienterprise.save()
                else:
                    return Response(6101)

            else:  # 查询本地报告
                data = alienterprise.content
        except Exception:
            return Response(6101)
        return Response(json.loads(data))


"""
阿里接口获取企业报告详情
url=/enterprise/profile
post={
    "compName":""
}
"""
class AliEnterpriseProfile(APIView):
    def getprofile(self, compname):
        statuCode, headers, profile = AliEnterprise.profile(compname)  # 全息画像
        if isinstance(profile, bytes): profile = profile.decode("utf-8")
        if statuCode is 200:
            return profile
        else:
            return ''

    def post(self, request):
        compName = request.data.get('compName')
        uniq = md5(compName)  # 查询码

        alienterprise, created = AliEnterpriseData.objects.get_or_create(unicode=uniq)

        if created:  ##网上获取数据
            profile = alienterprise.profile = self.getprofile(compName)
            alienterprise.comp = compName
            alienterprise.save()

        else:
            profile = alienterprise.profile

            if isinstance(profile, bytes): profile = profile.decode("utf-8")

            if profile is '':
                profile = alienterprise.profile = self.getprofile(compName)
                alienterprise.save()
            if alienterprise.comp == '':
                alienterprise.comp = compName
                alienterprise.save()

        try:
            if not profile is '':
                profile = json.loads(profile)
            else:
                profile = {}
        except Exception:
            pass

        uid = request.user.id
        report, created = ReportModel.objects.get_or_create(unicode=uniq)
        basic=''
        try:
            basic=profile['data']['BASIC'][0]['ITEM'][0]
            basic = json.dumps(basic,ensure_ascii=False)
        except:pass

        if created:
            report.type = 'enterprise'
            report.uid = uid
            report.data=basic
        else:
            report.data = basic
            report.times+=1

        report.save()

        isattention = False
        report_id=report.id
        if AttentionModel.objects.filter(uid=uid, report_id=report_id, type='enterprise',deleted_at=None).exists():
            isattention = True

        ###存储搜索记录
        SearchModel.objects.create(
            report_id=report_id,
            uid=uid,
            type='enterprise',
            expire_in=7200
        )

        return Response({'report_id':report_id,'profile': profile,'isattention': isattention})

"""
阿里云
企业基础信息
"""
class AliEnterpriseBase(APIView):
    def getbase(self, compname):
        statuCode, headers, base = AliEnterprise.get_progile_by_name(compname)  # 基本信息
        if isinstance(base, bytes): base = base.decode("utf-8")
        if statuCode is 200:
            return base
        else:
            return ""

    def post(self, request):
        compName = request.data.get('compName')
        uniq = md5(compName)  # 查询码

        alienterprise, created = AliEnterpriseData.objects.get_or_create(unicode=uniq)

        if created:  ##网上获取数据
            base = alienterprise.base = self.getbase(compName)
            alienterprise.save()
        else:
            base = alienterprise.base

            if isinstance(base, bytes): base = base.decode("utf-8")

            if base is '':
                base = alienterprise.base = self.getbase(compName)
                alienterprise.save()

        try:
            if not base is '': base = json.loads(base)
        except Exception:
            pass
        return Response({'base': base})


"""
阿里云
企业关系图
post={
    "compName":""
}
"""


class AliEnterpriseRelation(APIView):
    def getrelation(self, compname):
        statuCode, headers, relation = AliEnterprise.relation(compname)  # 关系网络
        if isinstance(relation, bytes): relation = relation.decode("utf-8")
        if statuCode is 200:
            return relation
        else:
            return ''

    def post(self, request):
        compName = request.data.get('compName')
        uniq = md5(compName)  # 查询码

        alienterprise, created = AliEnterpriseData.objects.get_or_create(unicode=uniq)

        if created:  ##网上获取数据
            relation = alienterprise.relation = self.getrelation(compName)
            alienterprise.save()
        else:
            relation = alienterprise.relation

            if isinstance(relation, bytes): relation = relation.decode("utf-8")

            if relation is '':
                relation = alienterprise.relation = self.getrelation(compName)
                alienterprise.save()

        try:
            if not relation is '': relation = json.loads(relation)
        except Exception:
            pass
        return Response({'relation': relation})


"""
百融用户报告详情接口
url=/personal/profile
post={
    'id':''
}
"""


class PersonalProfile(APIView):
    #总览
    def get_score(self,id):
        report = PersonModel.objects.filter(report_id=id, flag='score').first()
        if report is None:
            return {}
        arr = json.loads(report.formateddata)
        unicode = report.unicode
        ##aird1
        if arr.get('aird1') is None:
            r=PersonModel.objects.filter(report_id=id,flag='aird1').first()
            if r and r.score:
                arr['aird1']=1
            else:
                arr['aird1']=0

        if arr.get('count-apply') is not None:
            r = PersonModel.objects.filter(report_id=id, flag='apply').first()
            if r is not None:
                d = json.loads(r.formateddata)
                arr['count-apply'] = len(d)
            else:
                arr['count-apply'] = 0
        else:
            arr['count-apply'] = 0

        r = PersonModel.objects.filter(report_id=id, flag='behavior').first()
        if r is not None:
            d = json.loads(r.formateddata)
            arr['count-behavior'] = len(d)
        else:
            arr['count-behavior'] = 0

        r = PersonModel.objects.filter(report_id=id, flag='consume').first()
        if r is not None:
            d = json.loads(r.formateddata)
            arr['count-consume'] = len(d)
        else:
            arr['count-consume'] = 0

        r = BairongModel.objects.filter(unicode=unicode, type='p_haina').first()
        if r is not None:
            count = 0
            d = json.loads(r.metadata)
            if d.get('product') is not None:
                for key in d['product']:
                    if key not in ['ORDERLIST', 'orderNo', 'costTime']:
                        p = d['product'][key]
                        if isinstance(p, list):
                            count += len(p)
            arr['count-invest'] = count
        else:
            arr['count-invest'] = 0

        arr['count-law'] = 0

        report.formateddata = json.dumps(arr)
        report.save()
        return arr

    def _get_others(self,id,meal):
        report = PersonModel.objects.filter(report_id=id, flag=meal).first()
        if report is None:
            return {}
        return json.loads(report.formateddata)

    def _get_haina(self,uid,unicode):
        bairong = BairongModel.objects.filter(unicode=unicode, type='p_haina').first()
        if bairong is None:
            return {}
        data=json.loads(bairong.metadata)
        try:
            search_data=json.loads(bairong.data)
        except:
            report=ReportModel.objects.filter(unicode=unicode).first()
            try:
                search_data = json.loads(report.data)
            except:
                return None,data

        if data['code']=='600006':
            #重新尝试获取海纳接口
            bsapi=BsApi()
            data=bsapi.search(uid, unicode, search_data, 'haina',refresh=True)
        return search_data,data

    # 存储航旅记录
    def save_air(self,_data, air, _type):
        try:
            PersonModel.objects.bulk_create(
                unicode=_data['unicode'],
                flag=_type,
                formateddata=json.dumps(air, ensure_ascii=False),
                report_id=_data['report_id']
            )
        except:
            pass

    def post(self, request):
        report_id = request.data.get('id')
        assert report_id, 'request report id'
        uid = request.user.id

        report=ReportModel.objects.get(id=report_id)
        if not report:return Response([])
        #基础信息
        base=report.data
        if isinstance(base,str):base=json.loads(base)
        #总览
        score=self.get_score(report_id)
        #申请记录,特殊名单
        apply=self._get_others(report_id,'apply')
        #航旅记录，媒体阅览，社交关系
        behavior=self._get_others(report_id,'behavior')
        #月度收支，商品消费，银行支付
        consume=self._get_others(report_id,'consume')
        #投资公司，司法执行，行政处罚，刑事记录
        search_data,haina=self._get_haina(uid,report.unicode)
        #航旅记录
        aird1=self._get_others(report_id,'aird1')
        airh1=self._get_others(report_id,'airh1')

        if aird1=={} and search_data:#获取航旅信息
            bsapi = BsApi()
            AirTravel_d1 = bsapi.search(uid, report.unicode, search_data, 'aird1')
            AirTravel_h1 = bsapi.search(uid, report.unicode, search_data, 'airh1')
            search_data['unicode'] = report.unicode
            self.save_air(search_data, AirTravel_d1, 'aird1')
            self.save_air(search_data, AirTravel_h1, 'airh1')

        isattention=False
        if AttentionModel.objects.filter(uid=uid,report_id=report_id,type='personal',deleted_at=None).exists():
            isattention=True
        return Response(
            {
                'report_id': report_id,
                'isattention':isattention,
                'base':base,
                'score':score,
                'apply':apply,
                'behavior':behavior,
                'consume':consume,
                'haina':haina,
                'aird1':aird1,
                'airh1':airh1,
            }
        )


"""
获取个人报告详情【废弃】
url=/report/{report_id}/{meal}
get方法
personal meal:score/invest/law/apply/behavior/consume
enterprise meal:BizInfo/BizInvest_q/BizRelationship_q/BizExecution
"""
class Details(APIView):
    def get(self, request, id, meal):
        uid = request.user.id
        if AttentionModel.objects.filter(uid=uid, report_id=id).first() is None:
            if SearchModel.objects.filter(uid=uid, report_id=id).first() is None:
                return Response(4101)  # 未查询到该用户有搜索过产品就没法访问详情

        # 企业相关信息查询
        if meal in ['BizInfo', 'BizInvest_q', 'BizRelationship_q', 'BizExecution']:
            report = ReportModel.objects.filter(id=int(id)).first()
            if report is None:
                return Response([])

            unicode = report.unicode
            bairong = BairongModel.objects.filter(unicode=unicode, type=''.join(['e_', meal])).first()
            if bairong is None:
                # 网上获取数据
                if 'BizRelationship_q' == meal:
                    data = report.data
                    BizRelationship_q = BsApi.search(uid, unicode, json.loads(data), 'BizRelationship_q', True)
                    if BizRelationship_q is None:
                        return Response(0)
                    else:
                        return Response(BizRelationship_q)

                return Response(0)
            return Response(json.loads(bairong.metadata))

        elif meal in ['law', 'invest']:  # 法务信息、投资信息
            # personal  haina
            report = ReportModel.objects.filter(id=int(id)).first()
            if report is None:
                return Response(0)

            unicode = report.unicode
            bairong = BairongModel.objects.filter(unicode=unicode, type='p_haina').first()
            if bairong is None:
                return Response(0)
            return Response(json.loads(bairong.metadata))

        elif meal in ['score']:  # 首页的分数信息
            report = PersonModel.objects.filter(report_id=id, flag=meal).first()
            if report is None:
                return Response(0)
            arr = json.loads(report.formateddata)
            unicode = report.unicode
            if arr.get('count-apply') is not None:
                r = PersonModel.objects.filter(report_id=id, flag='apply').first()
                if r is not None:
                    d = json.loads(r.formateddata)
                    arr['count-apply'] = len(d)
                else:
                    arr['count-apply'] = 0
            else:
                arr['count-apply'] = 0

            r = PersonModel.objects.filter(report_id=id, flag='behavior').first()
            if r is not None:
                d = json.loads(r.formateddata)
                arr['count-behavior'] = len(d)
            else:
                arr['count-behavior'] = 0

            r = PersonModel.objects.filter(report_id=id, flag='consume').first()
            if r is not None:
                d = json.loads(r.formateddata)
                arr['count-consume'] = len(d)
            else:
                arr['count-consume'] = 0

            r = BairongModel.objects.filter(unicode=unicode, type='p_haina').first()
            if r is not None:
                count = 0
                d = json.loads(r.metadata)
                if d.get('product') is not None:
                    for key in d['product']:
                        if key not in ['ORDERLIST', 'orderNo', 'costTime']:
                            p = d['product'][key]
                            if isinstance(p, list):
                                count += len(p)
                arr['count-invest'] = count
            else:
                arr['count-invest'] = 0

            arr['count-law'] = 0

            report.formateddata = json.dumps(arr)
            report.save()
            return Response(arr)
        else:  # 其它通用接口
            report = PersonModel.objects.filter(report_id=id, flag=meal).first()
            if report is not None:
                return Response(0)
            return Response(json.loads(report.formateddata))