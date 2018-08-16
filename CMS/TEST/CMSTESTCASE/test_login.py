#coding=utf-8
import pytest
from TEST.API.login import Login

'''
created 2018.07.25
author guoyue
登录cms系统
'''
class TestLogin(object):
    url = 'http://cms.qafc.ops.com'
    # data必须是list
    data01 = [
        {'password': 'siji123', 'username': 'siji'},
        {'password': 'xiansheng123', 'username': 'xiansheng'}
    ]


    data02 = [
        {'password': '', 'username': 'siji'},
        {'password': 'xiansheng123', 'username': ''},
        {'password': 'siji1234', 'username': 'siji'},
        {'password': 'siji123', 'username': 'siji123'},
        {'password ':'','username':''}
    ]

    @pytest.mark.parametrize('data01', data01)
    def testcase01(self,data01):
        url=self.url
        res=Login.CMSlogin(self,url=url,data=data01).json()
        code=res['resultCode']
        assert code=='0'
        print(res['resultDesc'])

    @pytest.mark.parametrize('data02',data02)
    def testcase02(self,data02):
        url = self.url
        res=Login.CMSlogin(self,url=url,data=data02).json()
        code=res['resultCode']
        assert code=='CMS1008'
        print(res['resultDesc'])



