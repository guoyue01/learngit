import requests
from TEST.COMMON.token import *
from TEST.API.login import *
import json

'''
create 2018-08-09
author guoyue
删除、启用、停用优惠券（状态）
'''
#tubb:http://gateway.qafc.ops.com/operation-manage-supplychain/common/coupon/status/update
#siji:http://gateway.qafc.ops.com/fourseason-operation-manage/common/coupon/status/update
class CouponStatus(object):
    def __init__(self,type):

        if type=='tubobo':
            self.url='http://gateway.qafc.ops.com/operation-manage-supplychain/common/coupon/status/update'
            admin_url='http://tubobo-admin.qafc.ops.com/tubobo/sysUser/login'
            admin_data={
                "phone":"13486939171",
                "password":"YKwY/Xwdy4tZxyOQxbwYkg=="
            }
            self.header=Login().TuboboLogin(url=admin_url,data=admin_data)['headers']

        elif type=='siji':
            self.url='http://gateway.qafc.ops.com/fourseason-operation-manage/common/coupon/status/update'
            admin_url='http://gateway.qafc.ops.com/xgusercenter/account/login'
            admin_data={
                "username":"13732259026",
                "password":"YdNlnXcBWw9ZinGtraP3YQ==",
                "type":"username"
            }
            self.header=Login().SijiLogin(url=admin_url,data=admin_data)['headers']
        else:
            print('type不存在')

    def couponstatus(self,couponId,status='up'):
        data={
            "couponId":couponId,
            "status":status
        }
        result=requests.post(url=self.url,headers=self.header,json=data).json()
        if result['resultCode']=='0':
            return result
            #print('优惠券启用/停用/删除，成功,响应：',result)
        else:
            print('优惠券启用/停用/删除，失败，响应：',result)


if __name__=='__main__':
    couponstatus=CouponStatus('tubobo')
    couponId = "235819858757959680"

    status = "on"
    #on:上线、up:停止派发，abandon:作废类型'

    res=couponstatus.couponstatus(couponId,status)
    print(res.json())



