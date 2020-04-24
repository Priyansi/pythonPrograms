# -*- coding: utf-8 -*-
import re
import collections

NO_OF_MOST_COMMONS = 10
EXCLUDE_STOPWORDS = 'n'


def mostCommonWords(EXCLUDE_STOPWORDS='y'):
    words = []
    with open('WarAndPeace.txt', 'r') as f:
        text = f.read().lower()
    words = re.findall(r'[a-záéëíÀóúèîôàçâêïýöäüÁœÉæ]+', text)
    if EXCLUDE_STOPWORDS.lower() == 'n':
        with open('stopwords.txt', 'r') as f:
            stopwords = f.read().split()
        words = [
            word for word in words if word not in stopwords and len(word) > 3]
    wordCount = collections.Counter(words)
    return ''.join('{} : {}\n'.format(word, count) for word, count in wordCount.most_common(NO_OF_MOST_COMMONS))


print(mostCommonWords(EXCLUDE_STOPWORDS))
