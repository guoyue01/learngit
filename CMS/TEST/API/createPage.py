import requests
import re
import time

from TEST.COMMON.token import CMStoken

'''
create 2018-08-03
guoyue
创建首页&活动页
'''
class CreatePage(object):
    def __init__(self):
        self.url='http://cms.qafc.ops.com/page/creation'

    # 将版本号做转换成xxx000的格式
    def _MinVersion(self,minVersion):
        minVersion=re.findall(r"\d\d*",minVersion)
        number=0
        for i in minVersion:
            num=int(i)
            number=number*10+num

        print(number*1000)
        return number*1000

    def createpage(self,platform,pageName,minVersion,pageType='home',shopId='',copyFromPageId='',type='siji',):
        if type == 'siji':
            token = CMStoken().sijiToken()
        elif type == 'tubobo':
            token = CMStoken().tuboboToken()
        else:
            print('用户不存在')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': token
        }
        minVersion=CreatePage()._MinVersion(minVersion)

        data={
            "platform":platform,
                #平台：小程序、H5、"APP"
            "pageName":pageName,
            "minVersion":minVersion,
            "pageType":pageType,
                #页面类型，首页或者活动页"HOME",active
            "shopId":shopId,
            "copyFromPageId":copyFromPageId
        }

        res=requests.post(url=self.url,headers=headers,json=data)
        print(res.json())
        return res

if __name__=='__main__':
    time=time.time()
    pagename=str(time)+'首页测试'
    res=CreatePage().createpage(platform='APP',pageName=pagename,minVersion='1.4.0')

