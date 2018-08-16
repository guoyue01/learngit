from TEST.API.Coupon.addDoupon import addDoupon
import time
from TEST.API.Coupon.CouponStatus import CouponStatus
from TEST.API.CouponList import *
import pytest
import pymysql
from TEST.DB.mysql import *
'''
creat 2018-08-09
auther guoyue
优惠券的测试用例：优惠券的领取限制、校验
'''
class TestCoupon(object):  #测试类以Test开头(首字母大写），并且不能带有 init 方法
    data01=[
        { 'type':'tubobo',"receiveTime":["2018-08-13 08:14:50","2019-08-20 08:14:50"]},
        {'type':'tubobo',"receiveTime":["2018-08-12 08:14:50","2019-08-13 18:14:50"]},
        {'type':'tubobo',"receiveTime":["2018-08-13 15:14:50","2019-08-20 08:14:50"]}
    ]
    data02=[
        {'type': 'tubobo', "receiveTime": ["2018-08-10 08:14:50", "2019-08-11 08:14:50"]},
        {'type': 'tubobo', "receiveTime": ["2018-08-19 15:14:50", "2019-08-20 08:14:50"]},
        {'type': 'tubobo', "receiveTime": ["2018-08-13 15:14:50", "2019-08-20 08:14:50"]}

    ]
    data03 = [
        {'type': 'tubobo', "receiveTime": ["2018-10-10 08:14:50", "2019-11-11 08:14:50"]},
        {'type': 'tubobo', "receiveTime": ["2018-09-19 15:14:50", "2019-10-20 08:14:50"]},

    ]

    # def setup(self):
    #     couponName = 'cmstest%s' %time.time()
    #     self.couponId = addDoupon().tuboboAddDoupon(couponName=couponName)[0]
    #     print('优惠券id:',self.couponId)
    #
    #     couponstatus=CouponStatus('tubobo')
    #     couponstatus.couponstatus(couponId=self.couponId,status='on')

    def teardown(self):
        mysql = MySQLCommand(db='promotioncenter')
        sql = "delete from t_xg_coupon where id = '%s' " % self.couponId
        mysql.commitMysql(sql)
        mysql.closeMysql()


    def _addcoupon(self,receiveTime):
        # 创建优惠券
        couponName = 'cmstest%s' % time.time()
        self.couponId = addDoupon().tuboboAddDoupon(couponName=couponName, receiveTime=receiveTime)[0]
        print('优惠券id:', self.couponId)
        return self.couponId

    @pytest.mark.parametrize('data01', data01)
    def testcase_01(self,data01):
        self.couponId=TestCoupon()._addcoupon(data01["receiveTime"])

        #启用优惠券
        couponstatus = CouponStatus(type=data01['type'])
        res=couponstatus.couponstatus(couponId=self.couponId, status='on')
        assert res["resultCode"]=='0' , '优惠券启用失败'

        #cms配置优惠券
        coupons=Coupons(data01['type'])
        result =coupons.couponsList(self.couponId).json()
        #print(result)
        assert result["resultCode"]=='0' , '无法获取到优惠券的数据'
        assert result["resultData"]["couponsList"][0]["couponStatus"]==True , '优惠券的状态不是true'

    @pytest.mark.parametrize('data02',data02)
    def test_case02(self,data02): #测试未启用状态的优惠券
        self.couponId = TestCoupon()._addcoupon(data02["receiveTime"])

        # cms配置优惠券
        coupons = Coupons(data02['type'])
        result = coupons.couponsList(self.couponId).json()
        #print(result)
        assert result["resultCode"] == '0', '无法获取到优惠券的数据'
        assert result["resultData"]["couponsList"][0]["couponStatus"]==False , '优惠券的状态不是False'

    @pytest.mark.parametrize('data03', data03)
    def testcase_03(self,data03): #测试领取时间
        self.couponId=TestCoupon()._addcoupon(data03["receiveTime"])

        #启用优惠券
        couponstatus = CouponStatus(type=data03['type'])
        res=couponstatus.couponstatus(couponId=self.couponId, status='on')
        assert res["resultCode"]=='0' , '优惠券启用失败'

        #cms配置优惠券
        coupons=Coupons(data03['type'])
        result =coupons.couponsList(self.couponId).json()
        #print(result)
        assert result["resultCode"]=='0' , '无法获取到优惠券的数据'
        assert result["resultData"]["couponsList"][0]["couponStatus"]==False , '优惠券的状态不是False'















