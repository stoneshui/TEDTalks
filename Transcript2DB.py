###################################################################################
###########  Transcript2DB.py created by Zhao Xiao at Nov.25.2017 15:36 ###########
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
filename = 'getTalkTrans2017-11-25 04-22-43transSQL.txt'

#数据库设置
host = '192.168.199.179'
port = 3306
user = 'root'
passwd = '147852'
db = 'ted'
charset='utf8'

# 打开数据库连接
db = pymysql.connect( host='192.168.199.179',
                      port=3306,
                      user='root',
                      passwd='147852',
                      db='ted',
                      charset='utf8')
	 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

#打开数据文件
inFILE_OBJECT = open(filename, 'r', encoding='UTF-8')
lineparts = 1
recordnum = 1

def readTime(timestring):   #从字符串中读取时间函数，返回Unix系统时间
    thetime = time.strptime(timestring, '%Y-%m-%dT%H:%M:%S.000+00:00') 
    #timeStamp = int(time.mktime(targettime))
    return time.strftime('%Y-%m-%d %H:%M:%S',thetime)

def CreatSQL(parts):
    
#   sql_header = "INSERT INTO ted (talk_id, title, views, record_time, speaker_id, url, tags, description, speaker_name, thread_id, speaker_description, speaker_whotheyare, speaker_whylisten, requestTime) VALUES ("
    for i in range (0,len(parts)):
        if(parts[i] == ""):
            parts[i] ='NULL'

    talk_id = pymysql.escape_string(parts[0])
    content = parts[1]
    language = 'English'
    
    #print(talk_id,"\n",content,"\n")

    insertsql = "INSERT INTO transcript (talk_id, content) VALUES("+talk_id+",'"+content+"','"+language+"')"
    #valuesql = talk_id + ",'"+title+"','"+description+"','"+event+"','"+recordtime+"',"+views+",'"+tags+"',"+thread_id+",'"+url+"','"+speaker_name+"',"+speaker_id+",'"+speaker_description+"','"+speaker_whotheyare+"','"+ speaker_whylisten+"','"+requestTime+"')"
    #print(talk_id,'\n',content,'\n')
    #print(insertsql)
    return insertsql
    #return "use ted"

for line in inFILE_OBJECT:    #读取文件每一行
    lineparts = re.split('@@@',line.rstrip().encode('utf-8').decode('utf-8-sig'))
    sql = CreatSQL(lineparts)

    #执行SQL语句
    cursor.execute(sql)

    #将执行提交数据库
    db.commit()

    print("第",recordnum,"条数据写入数据库成功！！！")
    recordnum = recordnum+1
    #break #临时测试中断，只执行一次
inFILE_OBJECT.close()

# 关闭数据库连接
db.close()