import requests
from TEST.COMMON.token import CMStoken

'''
create 2018-08-06
author guoyue
白名单的处理：新增、删除、查询
'''

class WhiteCode(object):
    def __init__(self,host,type='siji'):
        self.base_url=host
        self.type=type

        if self.type=='siji':
            self.token=CMStoken().sijiToken()
        elif self.type=='tubobo':
            self.token=CMStoken().tuboboToken()

        self.head = {
            'Content-Type':'application/json',
            'Authorization': self.token
        }

    def add_whitecode(self,whiteList):
        url=self.base_url+'/whitecode/addition'

        data={
            'whiteList':whiteList
        }
        res=requests.post(url=url,headers=self.head,json=data)
        #print(res)
        return res

    def remove_whitecode(self,whiteList):
        url=self.base_url+'/whitecode/removal'
        #print(url)
        data = {
            'whiteList': whiteList
        }
        res=requests.post(url=url,headers=self.head,json=data)
        return res

    def all_whitecode(self):
        url=self.base_url+'/whitecode/all'
        res=requests.post(url=url,headers=self.head)
        res.status_code
        return res

if __name__=='__main__':
    res=WhiteCode('http://cms.qafc.ops.com','tubobo')
    whiteList=['187744432']
    result=res.add_whitecode(whiteList=whiteList)
    print('新增',result.json())
    res=res.all_whitecode().json()
    print('查询',res)
    #result=res.remove_whitecode(whiteList)
    #print(result)





