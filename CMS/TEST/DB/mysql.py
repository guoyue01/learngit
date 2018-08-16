import pymysql

'''
create 2018-08-14
author guoyue
用于连接功能测试的数据库
'''
class MySQLCommand(object):
    def __init__(self,db='cms'):

    #连接数据库
        try:
            # 创建连接对象
            self.conn = pymysql.connect(host='mysqltest.ops.com', port=3306, user='guoyue', password='guoyue',
                                        db=db)
            # 创建游标
            self.cursor = self.conn.cursor()
        except:
            print('connect mysql error')

    #查询数据
    def queryMysql(self,sql):
        try:
            self.cursor.execute(sql)
            row=self.cursor.fetchone()
            return row
        except:
            print(sql+'查询数据失败')

    def commitMysql(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
            print('数据操作失败，已回滚！')

    def closeMysql(self):
        self.cursor.close()
        self.conn.close()









