###################################################################################
###########  readTranscript.py created by Zhao Xiao at 11:36 Nov.10.2017###########
###########	 															###########
###########																###########
###########	 # -*- coding: utf-8 -*- 									###########
###########  Revised at 								###########
###################################################################################


import pymysql
#import pymongo

import time
import re
from datetime import datetime

#TED Talks结构数据
filename = 'getTalksInfo_txt2017-11-14 00-18-20.txt'

#数据库设置
host = '192.168.199.179'
port = 3306
user = 'ted'
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
    
#	sql_header = "INSERT INTO ted (talk_id, title, views, record_time, speaker_id, url, tags, description, speaker_name, thread_id, speaker_description, speaker_whotheyare, speaker_whylisten, requestTime) VALUES ("
    for i in range (0,len(parts)):
    	if(parts[i] == ""):
    	    parts[i] ='NULL'

    talk_id = pymysql.escape_string(parts[0])
    title = pymysql.escape_string(parts[1])
    description = pymysql.escape_string(parts[2])
    event = pymysql.escape_string(parts[3])
    
    #print(lineparts[4])
    recordtime = pymysql.escape_string(readTime(parts[4]))  #需要格式转换成Unix系统时间

    views = pymysql.escape_string(parts[5])
    tags = pymysql.escape_string(parts[6])
    thread_id = pymysql.escape_string(parts[7])
    url = pymysql.escape_string(parts[8])
    speaker_name = pymysql.escape_string(parts[9])
    speaker_id = pymysql.escape_string(parts[10])
    speaker_description = pymysql.escape_string(parts[11])
    speaker_whotheyare = pymysql.escape_string(parts[12])
    speaker_whylisten = pymysql.escape_string(parts[13])
    
    #requestTime = time.strptime("2017-10-22 22-29-34", '%Y-%m-%d %H-%M-%S') #从字符串中读入指定格式的时间
    requestTime = pymysql.escape_string(readTime("2017-10-22T22:29:34.000+00:00"))

    #print(talk_id,"\n",title,"\n",description,"\n",event,"\n",recordtime,"\n",views,"\n",tags,"\n",thread_id,"\n",url,"\n",speaker_name,"\n",speaker_id,"\n",speaker_description,"\n",speaker_whotheyare,"\n",speaker_whylisten,"\n",requestTime,"\n")

    insertsql = "INSERT INTO talks (talk_id, title, description, event, record_time, views, tags, thread_id, url, speaker_name, speaker_id, speaker_description, speaker_whotheyare, speaker_whylisten,requestTime) VALUES("
    valuesql = talk_id + ",'"+title+"','"+description+"','"+event+"','"+recordtime+"',"+views+",'"+tags+"',"+thread_id+",'"+url+"','"+speaker_name+"',"+speaker_id+",'"+speaker_description+"','"+speaker_whotheyare+"','"+ speaker_whylisten+"','"+requestTime+"')"
    return insertsql+valuesql
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
