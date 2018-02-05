import io, re, sys
import textract
import enchant

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#text = textract.process('rezumat-hids-framework.doc', extension='doc')
ext = sys.argv[1].split('.')[1]
text = textract.process(sys.argv[1], extension=ext)
d = enchant.Dict("en_US")

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

issues = ['study', 'investigate', 'system', 'pipeline', 'features', 'combine', \
          'modify', 'expand', 'etc', 'for various reasons', 'this', 'that', 'it', \
          'these', 'which', 'now', 'new', 'will', 'below', 'above', 'very', 'our', \
          'is thought', 'possess', 'sufficient', 'utilize', 'demonstrate', 'assistance', \
          'terminate', 'prior to', 'due to the fact that', 'in a considerable number of cases', \
          'the vast majority of', 'during the time that', 'in close proximity to']
solutions = ['develop', 'propose', 'model', 'representations', \
             '"That" is defining; "which" is nondefining', 'I think', 'have', \
             'enough', 'use', 'show', 'help', 'end', 'before', 'because', 'often', 'most', \
             'when', 'near']

print "Check the inappropriate syntax:"
for idx, row in enumerate(token_lists):
    for column in row:
        if column in issues:
            print "From line %5d remove: %s" % (idx, column)
        if d.check(column) is False and re.match('^[a-zA-Z ]*$', column):
            print "From line %5d please correct: %s" % (idx, column)
print "\tUse instead:\n%s" % solutions

## TODO: print romanian chars correctly, at the moment they do not
##       seem correctly encoded/decoded from 'text' variable -> POSTPONED

## TODO: identify acronyms and see if they were defined the first time
##       they were used, else signal this as an issue
print "Check that the terminology and notation in the paper are defined before used!"
print "Make sure italics are used for definitions or quotes, not for emphasis!"

print "For more infor please consult:"
print "\thttps://cs.stanford.edu/people/widom/paper-writing.html"
print "\thttp://karpathy.github.io/2016/09/07/phd/"
print "\thttps://lemire.me/blog/rules-to-write-a-good-research-paper/"
print "\thttp://www.columbia.edu/cu/biology/ug/research/paper.html"

print "Also use the following script: style-check.rb -v *.tex"
print "\tMore info here: http://www.cs.umd.edu/~nspring/software/style-check-readme.html"

## TODO: identify if the paper has the proper structure, for this
##       NLP an ML might need to be used

## TODO: maybe 'stop_words' can remain in 'keywords' list
## Identify the incorect syntaxes and eventually correct them. -> DONE
