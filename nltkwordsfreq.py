import nltk
from nltk.book import *

#text4.dispersion_plot(["education","art","history","society","music"])

fdist1=FreqDist(text1)  
vocabulary1=fdist1.keys()  
vocab=list(vocabulary1)  
print("vocabulary1=",vocab)  
fdist1.plot(50,cumulative=True)  