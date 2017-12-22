import io
import textract

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = textract.process('rezumat-hids-framework.doc', extension='doc')

char_encoding = "utf-8"
with io.open("review-text.log", 'w', encoding=char_encoding) as text_file:
    text_file.write(text.decode("unicode-escape"))
text_file.close()

#tokens = word_tokenize(text.decode('utf-8'))
punctuation = ['(',')',';',':','[',']',',']
stop_words = stopwords.words('english')
#keywords = [word for word in tokens if not word in punctuation]

token_lists = []
with io.open("review-text.log", encoding=char_encoding) as f:
#with open("text.log") as f:
    lines = f.readlines()

for line in lines:
    token_array = []

    if line.strip():
        for token in line.split():
            if token.strip():
                token_array.append(token)
    if token_array:
        token_lists.append(token_array)

issues = ['study', 'investigate', 'system', 'pipeline', 'features', 'combine', 'modify', 'expand']
solutions = ['develop', 'propose', 'model', 'representations']
## TODO: maybe 'stop_words' can remain in 'keywords' list
## Identify the incorect syntaxes and eventually correct them.
for idx, row in enumerate(token_lists):
    for column in row:
        if column in issues:
            print "From line %5d remove: %s" % (idx, column)
print "\tUse instead:\n%s" % solutions

## TODO: print romanian chars correctly, at the moment they do not
##       seem correctly encoded/decoded from 'text' variable

#print text
#print tokens
#print stop_words
#print keywords

#print token_lists

