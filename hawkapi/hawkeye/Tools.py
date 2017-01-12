from __future__ import unicode_literals
import hashlib
import ssl

from django.template.response import SimpleTemplateResponse
from django.utils import six

from rest_framework.serializers import json
#post 请求封装
def post(host, url, post_data=None, headers=None, connect=None):
    if headers is None:
        headers = {}
    return _do_request(host,url,post_data,headers,connect=connect)
def get(host, url, headers=None, connect=None):
    if headers is None:
        headers = {}
    return _do_request(host,url,None,headers,'GET',connect)

def _do_request(host, url, post_data=None, headers=None, method='POST', connect=None):
    import http.client

    if headers is None:
        headers = {}
    __connection=None
    try:
        if connect is not None:
            context = ssl._create_unverified_context()
            __connection = http.client.HTTPSConnection(host,context=context)
        else:
            __connection = http.client.HTTPConnection(host)
        __connection.connect()
        __connection.request(method=method, url=url, body=post_data,headers=headers,)
        response = __connection.getresponse()
        result=response.read()
        try:
            if isinstance(result,bytes):result=result.decode()
            if isinstance(result,str):result=json.loads(result)
        except:pass
        if not isinstance(result,dict):
            result={}
        return response.status, response.getheaders(), result
    except Exception as e:
        return None, None, {}
    finally:
        try:
            if __connection is not None:
                __connection.close()
        except:
            pass

def md5(string):
    b= string.encode('utf-8')
    return hashlib.md5(b).hexdigest()

"""
服务器状态响应封装
"""
class Response(SimpleTemplateResponse):
    @staticmethod
    def get_require(name):
        s = ['["', name, '"] is required']
        return ''.join(s)

    _errmsgs = {
        0:    'OK',
        201:  'created success',
        401:  'invalid_credentials',
        404:  'not found',
        400:  'bad request',
        500:  'internal error',
        # for search
        2001: 'search type not support',
        # for users
        4001: 'user is exists',
        4002: 'user is not exists',
        4003: 'account or password not match',
        # right to access
        4101: 'permission denied',
        # 百融Api
        6001: 'get bai rong token id failed',
        #阿里企业接口
        6101:'get complist failed'
    }
    data = None
    errcode = 0
    status = 200

    def getmsg(self, code):
        msg = self._errmsgs[code]
        if msg is None:
            msg = ''
        return msg

    def __init__(self, data=None, errcode=0, status=200, headers=None):
        super(Response, self).__init__(None, status=status)
        if isinstance(data, int):
            self.data = None
            self.errcode = data
        else:
            self.data = data
            self.errcode = errcode
        self.status = status

        self.template_name = None
        self.exception = False
        self.content_type = None

        if headers:
            for name, value in six.iteritems(headers):
                self[name] = value

    @property
    def rendered_content(self):
        # renderer = getattr(self, 'accepted_renderer', None)
        # accepted_media_type = getattr(self, 'accepted_media_type', None)
        # context = getattr(self, 'renderer_context', None)
        #
        # assert renderer, ".accepted_renderer not set on Response"
        # assert accepted_media_type, ".accepted_media_type not set on Response"
        # assert context, ".renderer_context not set on Response"
        # context['response'] = self
        #
        # media_type = renderer.media_type
        # charset = renderer.charset
        # content_type = self.content_type
        #
        # if content_type is None and charset is not None:
        #     content_type = "{0}; charset={1}".format(media_type, charset)
        # elif content_type is None:
        #     content_type = media_type
        self['Content-Type'] = 'application/json'

        # ret = renderer.render(self.data, accepted_media_type, context)
        # if isinstance(ret, six.text_type):
        #     assert charset, (
        #         'renderer returned unicode, and did not specify '
        #         'a charset value.'
        #     )
        #     return bytes(ret.encode(charset))
        #
        # if not ret:
        #     del self['Content-Type']

        if self.errcode is not None:
            if self.status is 200:
                msg = self._errmsgs[self.errcode]
            else:
                msg = self._errmsgs[self.status]
            if self.status is not 200:
                self.errcode = self.status
            meta = {
                'errcode':     self.errcode,
                'errmsg':      msg,
                'status_code': self.status
            }
        else:
            meta = None
        if meta is not None and self.data is not None:
            ret = {
                'data': self.data,
                'meta': meta
            }
        elif self.data is not None:
            ret = {
                'data': self.data
            }
        else:
            ret = {
                "meta": meta
            }
        return json.dumps(ret,ensure_ascii=False)

    @property
    def status_text(self):
        return self.getmsg[self.status]

    def __getstate__(self):
        state = super(Response, self).__getstate__()
        for key in (
                'accepted_renderer', 'renderer_context', 'resolver_match',
                'client', 'request', 'json', 'wsgi_request'
        ):
            if key in state:
                del state[key]
        state['_closable_objects'] = []
        return state