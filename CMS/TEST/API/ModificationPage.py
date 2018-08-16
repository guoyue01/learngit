import requests

'''
create 2018-08-07
author guoyue
首页/活动页的上线、下线操作
'''

class ModificationPage(object):
    def __init__(self,base_url):
        url=base_url+'/page/modification'

    def alterPage(self):
      url=self.url