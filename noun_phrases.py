# coding: utf-8
from os import path
import numpy as np
import matplotlib.pyplot as plt
# matplotlib.use('qt4agg')
from wordcloud import WordCloud, STOPWORDS
# import jieba
from textblob import TextBlob
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class WordCloud_NounPhrases:
    '''
    use package wordcloud and jieba
    generating wordcloud for chinese character
    '''

    def __init__(self, stopwords_file):
        self.stopwords_file = stopwords_file
        self.text_file = text_file

    @property
    def get_stopwords(self):
        self.stopwords = {}
        f = open(self.stopwords_file, 'r')
        line = f.readline().rstrip()
        while line:
            self.stopwords.setdefault(line, 0)
            self.stopwords[line.decode('utf-8')] = 1
            line = f.readline().rstrip()
        f.close()
        return self.stopwords

    @property
    def seg_text(self):
        with open(self.text_file) as f:
            text = f.readlines()
            text = r' '.join(text)

            # seg_generator = jieba.cut(text)
            blob = TextBlob(text)
            seg_generator = blob.noun_phrases

            self.seg_list = [
                i for i in seg_generator if i not in self.get_stopwords]
            self.seg_list = [i for i in self.seg_list if i != u' ']
            self.seg_list = r' '.join(self.seg_list)
            # print self.seg_list
        return self.seg_list

    def show(self):
        # wordcloud = WordCloud(max_font_size=40, relative_scaling=.5)
        wordcloud = WordCloud()
        # wordcloud = WordCloud(font_path=u'./static/simheittf/simhei.ttf',
        #                       background_color="black", margin=5, width=1800, height=800)

        wordcloud = wordcloud.generate(self.seg_text)

        plt.figure()
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.show()

    def save(self):
        # wordcloud = WordCloud(max_font_size=40, relative_scaling=.5)
        oWordcloud = WordCloud()
        # wordcloud = WordCloud(font_path=u'./static/simheittf/simhei.ttf',
        #                       background_color="black", margin=5, width=1800, height=800)

        wordcloud = oWordcloud.generate(self.seg_text)

        # plt.figure()
        # plt.imshow(wordcloud)
        # plt.axis("off")
        # plt.show()

        wordcloud.to_file(output_file_png)

        word_counts = oWordcloud.process_text(self.seg_text)
        word_counts= sorted(word_counts.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
        # print word_counts

        f=open(output_file_txt,'a')
        f.write('')
        f.close()

        f=open(output_file_txt,'a')
        for word, frequency in word_counts:
            item = '%s:%s\n' % (word,frequency)
            f.write(item)
        f.close()

if __name__ == '__main__':
    stopwords_file = u'./workplace/setting/stopwords.txt'
    text_file = u'./workplace/input/input.txt'
    output_file_png = u'./workplace/output/output.png'
    output_file_txt = u'./workplace/output/output.txt'

    generater = WordCloud_NounPhrases(stopwords_file)
    # generater.show()
    generater.save()
