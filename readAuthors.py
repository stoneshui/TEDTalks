###################################################################################
###########  httprequest.py created by Zhao Xiao at 22:14 Otc.19.2017 	###########
###########	 															###########
###########																###########
###########	 # -*- coding: utf-8 -*- 									###########
###########  Revised at 22:35 Otc.20.2017								###########
###################################################################################


import pymysql

#数据库设置
host = '172.0.0.1'
port = 3306
user = ''
passwd = ''
db = ''
charset='utf8'

# 打开数据库连接
db = pymysql.connect( host='art4.gift',port=3306, user='aqi', passwd='aqi',db='aqirawdata',charset="utf8")
	 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql =""

#执行SQL语句
cursor.execute()

#将执行提交数据库
db.commit()

# 关闭数据库连接
db.close()


