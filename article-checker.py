#import sys
import textract

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = textract.process('rezumat-hids-framework.doc', extension='doc')

#reload(sys)
#sys.setdefaultencoding('utf8')

tokens = word_tokenize(text.decode('utf-8'))
punctuation = ['(',')',';',':','[',']',',']
stop_words = stopwords.words('english')

keywords = [word for word in tokens if not word in stop_words and not word in punctuation]

# TODO: maybe 'stop_words' can remain in 'keywords' list
## Identify the incorect syntaxes and eventually correct them.

#print text
#print tokens
print stop_words
#print keywords
