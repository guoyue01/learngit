import requests
from TEST.COMMON.token import *
import time
import pymysql
from TEST.API.login import *
from TEST.API.Coupon.CouponStatus import *
import os
from TEST.DB.mysql import *

class addDoupon(object):
    def tuboboAddDoupon(self,couponName,receiveTime,overPrice=100,price=10,quantity=2,receiveUidMax=1,couponType='fullcut',customerType='all',
                        validTimeType=1,useTime=["2018-08-03 08:14:50","2019-09-05 08:14:50"],overlay='true',isOpen=1,limitType='allspu',description='',remark='',discount='',maxPrice='',
                        couponId='',availableSpuIds=[],availableCategoryIds=[],intervalDay=''):
        # url='http://siji-operation-web.qafc.ops.com/distribute/add'
        url = 'http://gateway.qafc.ops.com/operation-manage-supplychain/coupon/add'
        head=Login().TuboboLogin(url='http://tubobo-admin.qafc.ops.com/tubobo/sysUser/login')['headers']

        overPrice=overPrice*100
        price=price*100

        #print(receiveTime)


        receiveTimeStart = int(time.mktime(time.strptime(receiveTime[0], '%Y-%m-%d %H:%M:%S')))*1000
        #如果不乘以1000就是以秒为单位的时间戳，乘以1000是以毫秒为单位的时间戳
        receiveTimeEnd = int(time.mktime(time.strptime(receiveTime[1], '%Y-%m-%d %H:%M:%S')))*1000
        #receiveTimeStart=1533111291000
        #receiveTimeEnd =1535703291000
        useTimeStart = int(time.mktime(time.strptime(useTime[0],'%Y-%m-%d %H:%M:%S')))*1000
        print('useTimeStart',useTimeStart)
        useTimeEnd = int(time.mktime(time.strptime(useTime[1],'%Y-%m-%d %H:%M:%S')))*1000
        print('useTimeEnd',useTimeEnd)


        data = {
    "couponName":couponName,
            #优惠券名称，必填
    "description":description,
            #优惠券的描述，非必填
    "remark":remark,
            #优惠券备注，非必填
    "couponType":couponType,
            #优惠券类型：fullcut:满减券，discount:满折券
    "overPrice":overPrice,
            #满额，非必填，int,数值*100=99900,
    "price":price,
            #减额，非必填，int,数值*100=9900,
    "discount":discount,
            #折扣，非必填，float，数值*10
    "maxPrice":maxPrice,
            #减额封顶，非必填，float
    "quantity":quantity,
            #发券总数，必填，int
    "receiveUidMax":receiveUidMax,
            #每个账号限制领取数量，必填，int
    "receiveTime":receiveTime,
            #领取时间段，必填，[ "2018-08-01 08:14:50","2018-08-31 08:14:50"],
    "receiveTimeStart":receiveTimeStart,
            #领取开始时间，必填，时间戳1533111290529,
    "receiveTimeEnd":receiveTimeEnd,
            #领取结束时间，必填，1535703290529,
    "customerType":customerType,
            #领取对象，必填，用户对象限制类型：new新用户 old老用户 所有用户 all
    "validTimeType":validTimeType,
            #有效时间类型，必填，1,
    "intervalDay":intervalDay,
            #非必填
    "useTime":useTime,
            #["2018-08-01 08:14:50","2018-09-24 08:14:50"],
    "useTimeStart":useTimeStart,
            #1533111290534,
    "useTimeEnd":useTimeEnd,
            #1537776890534,
    "overlay":overlay,
            #是否可叠加，必填，'true、false',
    "isOpen":isOpen,
            #是否公开，必填，0：不公开 1：公开
    "limitType":limitType,
            #限制类型，必填，allspu：所有商品，category：指定分类，spu：指定商品,
    "couponId":couponId,
            #非必填"",
    "availableSpuIds":availableSpuIds,
            #非必填，[],
    "availableCategoryIds":availableCategoryIds
            #非必填，[]
        }


        res = requests.post(url=url, headers=head, json=data).json()

        if res['resultCode']== '0':
            mysql=MySQLCommand(db='promotioncenter')
            sql = "select id  from t_xg_coupon where coupon_name='%s'" % couponName
            SQLresult=mysql.queryMysql(sql=sql)
            mysql.closeMysql()
            return SQLresult

        else:
            print('优惠券新增失败，响应：',res)



if __name__ == '__main__':
    couponName='test%s'%time.time()
    receivetime=["2018-08-01 08:14:50","2019-08-03 08:14:50"]
    result = addDoupon().tuboboAddDoupon(couponName=couponName,receivetime=receivetime)
    print('couponid',result)

    couponId = result[0]
    print(result[0])
    couponstatus = CouponStatus('tubobo')
    status = "on"
    res = couponstatus.couponstatus(couponId, status)
    print('启用优惠券',res)




