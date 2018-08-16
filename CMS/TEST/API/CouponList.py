import requests
from TEST.API.login import *


class Coupons(object):
    def __init__(self,type):
        if type=='tubobo':
            data={
            'password': 'xiansheng123',
            'username': 'xiansheng'
            }
        elif type=='siji':
            data={
                'password': 'siji123',
                'username': 'siji'
            }
        else:
            print('cms中该用户不存在')

        self.header=Login().CMSlogin(data=data)['headers']

    def couponsList(self,*couponId):
        url='http://cms.qafc.ops.com/project/couponList'

        body={
            'coupons':couponId
        }

        result=requests.post(url=url,headers=self.header,json=body)
        return result



if __name__=='__main__':

    #print(url)
    couponID = ['236135934259642368']
    coupons = Coupons(type='tubobo')
    res=coupons.couponsList(*couponID)
    print(res.json())
    res=res.json()['resultData']['couponsList'][0]['couponStatus']
    print(res)
