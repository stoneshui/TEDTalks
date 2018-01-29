###################################################################################
###########  DB2Transcript.py created by Zhao Xiao at Dec.25.2017 21:42 ###########
###########	 															###########
###########																###########
###########	 # -*- coding: utf-8 -*- 									###########
###########  Revised at 												###########
###################################################################################


import pymysql
#import pymongo

import time
import re
from datetime import datetime

#TED Talks结构数据
filename = 'speaker_description.txt'

#数据库设置

# 打开数据库连接
db = pymysql.connect( host='47.100.116.64',
                      port=3306,
                      user='ted',
                      passwd='OIGKHDJjCz2lOjTT',
                      db='ted',
                      charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

#创建文件对象
outFILE_OBJECT = open(filename, 'w', encoding='UTF-8')
sql = "SELECT transcript.talk_id,speaker_description FROM transcript right JOIN  talks on transcript.talk_id=talks.talk_id Where talks.record_time Between '0000-01-01' And '2017-12-31'order by talks.record_time "
#执行SQL语句
cursor.execute(sql)

# 使用 fetchone() 方法获取一条数据
datarows = cursor.fetchall()

for row in datarows:
    if (row[0] == 'NULL') | (row[0] == None):
        continue
    print(row[0])
    outFILE_OBJECT.write(str(row[0]))
    outFILE_OBJECT.write('\t')
    outFILE_OBJECT.write(row[1])
    outFILE_OBJECT.write('\n')

outFILE_OBJECT.close()

# 关闭数据库连接
db.close()