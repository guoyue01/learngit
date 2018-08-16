#from TEST.API.login import *
from TEST.API.login import Login

class CMStoken(object):
    def tuboboToken(self):
        data={
            'password':'xiansheng123',
            'username':'xiansheng'
        }
        url = 'http://cms.qafc.ops.com/user/login'
        cmslogin = Login()
        res=cmslogin.TuboboLogin(url=url,data=data)
        result=res.json()
        #print(result)
        token = result['resultData']['token']
        #token='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4aWFuc2hlbmciLCJleHAiOjE5NjM4ODI1NzV9.OkLJlvEcITDR4gkEZhXxcdb4Hd1for7TMk4hnYPjN4w'
        return token

    def sijiToken(self):
        data={
            'password':'siji123',
            'username':'siji'
        }
        url = 'http://cms.qafc.ops.com/user/login'
        cmslogin = Login()
        res = cmslogin.SijiLogin(url=url, data=data)
        result = res.json()
        #print(result)
        result = result['resultData']
        token = result['token']
       # print(token)
        #token='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzaWppIiwiZXhwIjoxOTYzODg0OTI0fQ.zLxbdtHLnRZS7Kc9XF28xFt1znOdpqOq2-709ucUJng'
        return token

class AddCouponToken(object):
    def tubobo(self):
        data = {
            "phone": "13486939171",
            "password": "YKwY/Xwdy4tZxyOQxbwYkg=="
        }
        url='http://tubobo-admin.qafc.ops.com/tubobo/sysUser/login'
        res=Login().TuboboLogin(url=url,data=data).json()
        token = res['resultData']['token']
        return token

    def siji(self):
        data = {
            "username": "13732259026",
            "password": "YdNlnXcBWw9ZinGtraP3YQ==",
            "type": "username"
        }
        url = 'http://gateway.qafc.ops.com/xgusercenter/account/login'
        res = Login().SijiLogin(url=url, data=data).json()
        result = res['resultData']
        token = result['access_token']
        return token



if __name__=='__main__':
    res = CMStoken().tuboboToken()
    print(res)