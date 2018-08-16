import pytest
import json
from TEST.API.login import *
from TEST.API.WhiteCode import *

'''
create 2018.08.08
author guoyue
白名单的测试用例：查看、新增、删除
'''

data = [{
    'type':'siji',
    'url': 'http://cms.qafc.ops.com',
    'whiteList': ['19800011122']
    },
    {
    'type':'tubobo',
    'url': 'http://cms.qafc.ops.com',
    'whiteList': ['1999000333']

    }]

class TestWhitecode(object):

    @pytest.mark.parametrize('data',data)
    def test_addWhitecode(self,data):#必须先执行
        print('测试%s账号的白名单' %data['type'])

        whitecode = WhiteCode(host=data['url'],type=data['type'])
        result=whitecode.add_whitecode(whiteList=data['whiteList'])
        assert result.status_code==200 , '请求发送失败'

        res = whitecode.all_whitecode().json()
        whitelist = res['resultData']['whiteList']
        assert data['whiteList'][0] in whitelist, '新增白名单电话号码失败'

    @pytest.mark.parametrize('data', data)
    def test_removeWhitecode(self,data):
        print('测试%s账号的白名单' % data['type'])

        whitecode=WhiteCode(host=data['url'])
        result=whitecode.remove_whitecode(data['whiteList'])
        assert result.status_code==200 , '请求发送失败'

        res=whitecode.all_whitecode().json()
        whitelist = res['resultData']['whiteList']
        assert data['whiteList'][0] not in whitelist,'删除白名单电话号码失败'












