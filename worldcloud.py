import matplotlib.pyplot as plt
import matplotlib as mpl
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import jieba
import numpy as np
from PIL import Image
 
text= open('speaker_description.txt',encoding= 'utf8').read()
tistr='\u0057\u006f\u0072\u006c\u006f\u0075\u0064\u0020\u0062\u0079\u0020\u005a\u0058\u0069\u0061\u006f\u0020\u006f\u0066\u0020\u0054\u004a\u0055\u0020\u0041\u0043\u0020\u004c\u0061\u0062'
tistr1='TITLE'
tistr2='TITLE'
tistr3='TITLE'
tistr4='TITLE'

wordlist_after_jieba = jieba.cut(text, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

#根据图片创建模板对象
maskImg = np.array(Image.open("mask3.png"))

# 设置停用词
stopwords = set(STOPWORDS)
stopwords.add("said")

#创建字云对象，指定字云基本输出参数 
my_wordcloud = WordCloud(
						 #设置词云的背景颜色
						 background_color="white",

						 #设置词云的图片尺寸参数
						 width=600,		
						 height=800,
						 
						 #设置词云的最大单词数
						 max_words=500,
						 
						 #设置停用词
						 stopwords=stopwords,
						 
						 #设置词云中的最大字号
						 max_font_size=84,
						 
						 #设置词云中的最小字号
						 #min_font_size=16,
						 
						 #指定词云的模板对象
						 mask = maskImg,

						 random_state=42
						 )
#设置字云字体
my_wordcloud.front_path='msyh.ttf'

#根据文本创建词云对象
my_wordcloud.generate(text)

#生成字云
#my_wordcloud.generate_from_text(wl_space_split)

#根据图片创建着色对象
#img_colors = ImageColorGenerator(maskImg)

#使用着色对象对调整词云对象颜色
#my_wordcloud.recolor(color_func=img_colors)
 
###Main Fig Object and Setting
fig = plt.figure(figsize=(6,8),facecolor="grey")
plt.title(tistr)

#坐标轴显示设置
plt.axis("off")

plt.subplots_adjust(left=0.09,right=0.91,bottom=0.13,top=0.91,wspace=0.25,hspace=0.25) 

###Sub Fig Object and Setting
ax1 = fig.add_subplot(111)

#根据词云生成图像
plt.imshow(my_wordcloud, interpolation="bilinear")
plt.axis("off")

#ax2 = fig.add_subplot(222)
#plt.axis("off")

#ax3 = fig.add_subplot(223)
#plt.axis("off")

#ax4 = fig.add_subplot(224)
#plt.axis("off")


#输出显示图像
plt.show()