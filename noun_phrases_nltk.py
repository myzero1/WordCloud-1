#!/usr/bin/env python
# coding=UTF-8
#
# Output the 50 most-used words from a text file, using NLTK FreqDist()
# (The text file must be in UTF-8 encoding.)
#
# Usage:
#
#   ./freqdist_top_words.py input.txt
#
# Sample output:
#
# et;8
# dolorem;5
# est;4
# aut;4
# sint;4
# dolor;4
# laborum;3
# ...
#
# Requires NLTK. Official installation docs: http://www.nltk.org/install.html
#
# I installed it on my Debian box like this:
#
# sudo apt-get install python-pip
# sudo pip install -U nltk
# python
# >>> import nltk
# >>> nltk.download('stopwords')
# >>> nltk.download('punkt')
# >>> exit()

import sys
import codecs
import nltk
from nltk.corpus import stopwords
import docx
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob
from os import path
reload(sys)
sys.setdefaultencoding('utf-8')

d = './workplace/'

# NLTK's default German stopwords
default_stopwords = set(nltk.corpus.stopwords.words('german'))

# We're adding some on our own - could be done inline like this...
# custom_stopwords = set((u'–', u'dass', u'mehr'))
# ... but let's read them from a file instead (one stopword per line, UTF-8)
stopwords_file = path.join(d, 'setting/stopwords.txt')
custom_stopwords = set(codecs.open(stopwords_file, 'r', 'utf-8').read().splitlines())

all_stopwords = default_stopwords | custom_stopwords

input_file = path.join(d, 'input/input.txt')

fp = codecs.open(input_file, 'r', 'utf-8')

#words = nltk.word_tokenize(fp.read())

blob = TextBlob(fp.read())
words = blob.noun_phrases

# print(words)
# exit()
# Remove single-character tokens (mostly punctuation)
words = [word for word in words if len(word) > 1]

# Remove numbers
words = [word for word in words if not word.isnumeric()]

# Lowercase all words (default_stopwords are lowercase too)
words = [word.lower() for word in words]

# Stemming words seems to make matters worse, disabled
# stemmer = nltk.stem.snowball.SnowballStemmer('german')
# words = [stemmer.stem(word) for word in words]

# Remove stopwords
words = [word for word in words if word not in all_stopwords]

# Calculate frequency distribution
fdist = nltk.FreqDist(words)

# Output top 50 words

myword = {}
f=open(path.join(d, 'output/output.txt'),'w')
f.write('')
f.close()

f=open(path.join(d, 'output/output.txt'),'a')
for word, frequency in fdist.most_common(999999999):
    # print(u'{};{}'.format(word, frequency))
    myword[word] = frequency
    item = '%s:%s\n' % (word,frequency)
    f.write(item)
f.close()



#myword = {"a":11,"b":221,"c":2255,"d":224,"e":223}
#wordcloud = WordCloud(max_font_size=40).generate_from_frequencies(myword)

oWordcloud = WordCloud(width=800, height=600)
wordcloud = oWordcloud.generate_from_frequencies(myword)

oWordcloud.to_file(path.join(d, 'output/output.png'));

# plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()