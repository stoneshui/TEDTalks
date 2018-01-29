###################################################################################
###########  httprequest.py created by Zhao Xiao at 22:14 Otc.22.2017   ###########
###########                                                             ###########
###########                                                             ###########
###########  # -*- coding: utf-8 -*-                                    ###########
###########  Revised at                                                 ###########
###################################################################################
import re

filename = 'getTalksInfo_txt2017-10-22 22-29-34.txt'
outfilename= 'TalkDescriptionAll_Text.txt'
talkidlist= 'talkidlist.txt'

inFILE_OBJECT = open(filename, 'r', encoding='UTF-8')	
	
outFILE_OBJECT = open(talkidlist,'w', encoding='UTF-8')
for line in inFILE_OBJECT:
    lineparts = re.split('@@@',line.rstrip())
    outFILE_OBJECT.write(lineparts[0] + "\n")
inFILE_OBJECT.close()
outFILE_OBJECT.close()
print("TED Talks Description Processing Finished!")