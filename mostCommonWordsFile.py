import re
import collections

NO_OF_MOST_COMMONS=10

def mostCommonWords():
    with open('WarAndPeace.txt','r') as f:
        text = f.read().lower()

    words = re.findall(r'\w+', text)
    wordCount = collections.Counter(words)
    return ''.join('{} : {}\n'.format(word,count) for word, count in wordCount.most_common(NO_OF_MOST_COMMONS))


print(mostCommonWords())