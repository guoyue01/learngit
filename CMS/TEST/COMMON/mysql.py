import pymysql



#创建连接对象
conn=pymysql.connect(host='mysqltest.ops.com',port=3306,user='guoyue',password='guoyue',db='promotioncenter')
#创建游标
cursor=conn.cursor()

#执行sql，查询数据
sql='select * from t_xg_coupon'
cursor.execute(sql)
row_1=cursor.fetchone()
print(row_1)

#关闭游标
cursor.close()
#关闭连接
conn.close()