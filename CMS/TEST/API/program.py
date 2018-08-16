#coding=utf-8
from TEST.COMMON.token import CMStoken
import requests
import pymysql

'''
created 2018.07.24
author guoyue
对接小程序，小程序通过接口获取首页和活动页的配置数据

'''
url = 'http://cms.dev.ops.com/pagehome/program'
class CMSProgram(object):

    def sijiProgram(self,projectId,**kwargs):
        #url = 'http://cms.qafc.ops.com/pagehome/program'
        cmstoken=CMStoken()
        token=cmstoken.sijiToken()
        head = {
            'Content-Type': 'application/json',
            'Authorization': token
        }

        data={
            'projectId':projectId,
            **kwargs
        }
        #print('data:',data)

        res=requests.post(url=url,headers=head,json=data)
        return res

    def toboboProgram(self,projectId,**kwargs):

        cmstoken=CMStoken()
        token=cmstoken.tuboboToken()
        head = {
            'Content-Type': 'application/json',
            'Authorization': token
        }

        data={
            'projectId':projectId,
            **kwargs
        }


        res=requests.post(url=url,headers=head,json=data)
        return res

if __name__=='__main__':
    pageId= "f0d28b79-e623-4cfc-a179-979826da1ec3"
    projectId='siji'
    appVersion=11000
    d={
        #'pageId':pageId,
        'appVersion':appVersion
    }
    res = CMSProgram().sijiProgram( projectId=projectId, **d)
    result=res.json()
    print('result:',result)

