import requests
import json

'''
cms的登录
'''

class Login(object):
    def CMSlogin(self,data,url='http://cms.qafc.ops.com'):
        url = (url+'/user/login')  #测试环境：http://cms.qafc.ops.com/user/login
        head = {
            'Content-Type': 'application/json',
        }
        res=requests.post(url=url,headers=head,json=data)
        token=res.json()['resultData']['token']
        headers={
            'Content-Type': 'application/json',
            'Authorization': token
        }
        return {'result':res,'headers':headers}

    def TuboboLogin(self,url,data={"phone": "13486939171", "password": "YKwY/Xwdy4tZxyOQxbwYkg=="}):
        #url='http://tubobo-admin.qafc.ops.com/tubobo/sysUser/login'

        head = {
            'Content-Type': 'application/json',
        }
        res = requests.post(url=url, headers=head, json=data)
        token=res.json()['resultData']['token']
        headers = {
            'Content-Type': 'application/json',
            'Authorization': token,
            'platformId': '2',
            'bizCode': '1'

        }
        return {'result':res,'headers':headers}

    def SijiLogin(self,url,data={"username": "13732259026", "password": "YdNlnXcBWw9ZinGtraP3YQ==", "type": "username"}):
        head = {
            'Authorization': 'Basic anV0b25nOmp1dG9uZw ==',
            'Content-Type':'application/json'
        }
        res = requests.post(url=url, headers=head, json=data)
        token=res.json()['resultData']['access_token']
        header={
            'Content-Type': 'application/json',
            'Authorization': 'bearer'+token,
        }
        return {'result':res,'headers':header}



if __name__=='__main__':
    url='http://cms.qafc.ops.com'
    data01={'password':'siji123','username':'siji'}
    result=Login().CMSlogin(url=url,data=data01)
    res=result['result'].json()
    print('cms',res)
    print('header',result['headers'])


    url = 'http://gateway.qafc.ops.com/xgusercenter/account/login'
    data={"username": "13732259026", "password": "YdNlnXcBWw9ZinGtraP3YQ==", "type": "username"}
    res=Login().SijiLogin(url=url,data=data)
    print(res)

    url='http://tubobo-admin.qafc.ops.com/tubobo/sysUser/login'
    data02={
        "phone": "13486939171",
        "password": "YKwY/Xwdy4tZxyOQxbwYkg=="
    }
    res=Login().TuboboLogin(url=url,data=data02)
    print(res)


