#coding=utf-8
import pytest

from TEST.API.program import CMSProgram
'''
对接小程序的case
'''

class TestProgram(object):
    # 数据准备：
    data01 = [
        {'pageId': 'f0d28b79-e623-4cfc-a179-979826da1ec3', 'projectId': 'siji','appVersion':11000,'shopId':''},
        {'projectId': 'siji','appVersion':11000}
    ]
    data02=[
        {'pageId':111,'projectId':'siji','appVersion':11000,'shopId':''},
        {'pageId':'@@aaa','projectId':'siji','appVersion':11000,'shopId':''},
        {'pageId':'f0d28b79-e623-4cfc-a179-979826dc3','projectId':'siji', 'appVersion': 13000, 'shopId': ''}
    ]

#将参数传入

    @pytest.mark.parametrize('data01',data01)
    def testcase01(self,data01):
        cmsprogram = CMSProgram()
        res = cmsprogram.sijiProgram(**data01)
        res=res.json()
        print(res['resultDesc'])
        code =int(res['resultCode'])
        assert code==0

    @pytest.mark.parametrize('data02',data02)
    def testcase02(self,data02):
        res = CMSProgram().sijiProgram(**data02).json()
        res=res['resultDesc']
        print(res)
        assert res=='页面ID无效，页面查询结果失败'





