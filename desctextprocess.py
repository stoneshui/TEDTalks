###################################################################################
########### desctextprocess.py created by Zhao Xiao at 16:58 Otc.25.2017###########
########### This program read all talk descropitons as plain text and   ###########
########### out put a NL word list.                                     ###########
###########  # -*- coding: utf-8 -*-                                    ###########
###########  Revised at                                                 ###########
###################################################################################
from __future__ import division
import nltk, re, pprint
from nltk import *
#from nltk.book import *

print('开始从文件中读取文本...')
f = open('transcript\\transcript_1999.txt','r', encoding='UTF-8')
raw = f.read()    #将文本以字符串形式存入变量raw中
#raw = 'A frequency distribution for the outcomes of an experiment. A frequency distribution records the number of times each outcome of an experiment has occurred. For example, a frequency distribution could be used to record the frequency of each word type in a document. Formally, a frequency distribution can be defined as a function mapping from each sample to the number of times that sample occurred as an outcome.Frequency distributions are generally constructed by running a number of experiments, and incrementing the count for a sample every time it is an outcome of an experiment. For example, the following code will produce a frequency distribution that encodes how often each word occurs in a text:'
f.close()

print('文件读取成功，进行文本规范化')
set(w.lower() for w in raw)

print('开始进行分词...')
tokens = nltk.word_tokenize(raw)    #使用NLTK进行分词，产生word和标点的链表
print('分词完成.')
print(len(tokens))
#print(tokens)

print('创建不含非字母单词和过短单词的子集')
lengthlimit = 5
selecttoken = [w for w in tokens if len(w) >= lengthlimit and w.isalpha()] #挑选只包含字母且长度超过5的词汇创建新语料


print('开始进行词型归并')
wnl = nltk.WordNetLemmatizer()
token_wnl=[wnl.lemmatize(t) for t in selecttoken]

print('进行词性分类标记')
token_tag=nltk.pos_tag(token_wnl)

print('开始生成NLTK语料...')
text = nltk.Text(token_wnl)#############################################################

#输出指定词性的单词列表
#单词计数器
NounCount = 0		#名词计数器
VerbCount = 0		#动词计数器
AdjCount = 0		#形容词
AdvCount = 0		#副词
elseCount = 0       #其它词

#创建输出文件对象
#名词
outNoun='nonelen'+str(lengthlimit)+'.txt'
outNoun_FILE_OBJECT = open(outNoun,'w', encoding='UTF-8')
#动词
outVerb='verblen'+str(lengthlimit)+'.txt'
outVerb_FILE_OBJECT = open(outVerb,'w', encoding='UTF-8')
#形容词/副词
outAdj='adjlen'+str(lengthlimit)+'.txt'
outAdj_FILE_OBJECT = open(outAdj,'w', encoding='UTF-8')
#副词
outAdv='advlen'+str(lengthlimit)+'.txt'
outAdv_FILE_OBJECT = open(outAdv,'w', encoding='UTF-8')

#判断并输出

for word,pos in token_tag:
    if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
        #print(word,pos)
        outNoun_FILE_OBJECT.write(word+ ", ")
        NounCount=NounCount+1
    elif(pos == 'V' or pos == 'MOD' or pos == 'VD' or pos == 'VG' or pos == 'VN' or pos == 'VBG' or pos == 'VBD' or pos == 'VBZ' or pos == 'VBN'):
        #print(word,pos)
        outVerb_FILE_OBJECT.write(word+ ", ")
        VerbCount=VerbCount+1
    elif(pos == 'ADJ' or pos == 'JJ'):
        #print(word,pos)
        outAdj_FILE_OBJECT.write(word+ ", ")
        AdjCount=AdjCount+1
    elif(pos == 'ADV' or pos == 'RB'):
        #print(word,pos)
        outAdv_FILE_OBJECT.write(word+ ", ")
        AdvCount=AdvCount+1
    else: elseCount = elseCount+1

#关闭文件对象
outNoun_FILE_OBJECT.close()
outVerb_FILE_OBJECT.close()
outAdj_FILE_OBJECT.close()

#显示单词分类输出结果
print('名词总数为：',NounCount)
print('动词总数为：',VerbCount)
print('形容词总数为：',AdjCount)
print('副词总数为：',AdvCount)
print('其它词总数为：',elseCount)


#print(text[100:150])
#text.collocations()

#print(subtext_wnl[100:150])

print('创建包含给定样本的频率分布...')
fdist1=FreqDist(text)
sorted(fdist1.items(),key=lambda word: fdist1.B())
vocabulary1=fdist1.keys()
vocab=list(vocabulary1)
print(vocab[0:50])

#for word in sorted(fdist1.items(),key=lambda word: fdist1.B()):
#	print(word[0],',',word[1])  
#vocabulary1=fdist1.keys()  
#vocab=list(vocabulary1)  
#print("vocabulary1=",vocab[0:50])
#print('绘制给定样本的频率分布图...')  
#fdist1.plot(50)  