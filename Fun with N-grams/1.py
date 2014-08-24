import os
import re
import string

filename = 'ngrams-dataset.txt'
f = open(filename,'rU')
text = f.read()
f.close()
text = string.lower(text)
text= text.replace('\n',' ')
text= text.replace('\t',' ')
text = text.replace(',',' ')
text = text.replace('!',' ')
text = text.replace('@',' ')
text = text.replace('#',' ')
text= text.replace('$',' ')
text = text.replace('%',' ')
text= text.replace('&',' ')
text= text.replace('*',' ')
text= text.replace('(',' ')
text= text.replace(')',' ')
text= text.replace('-',' ')
text= text.replace('_',' ')
text= text.replace('=',' ')
text= text.replace('+',' ')
text= text.replace('/',' ')
text= text.replace('"',' ')
text= text.replace(':',' ')
text= text.replace(';',' ')
text= text.replace('{',' ')
text= text.replace('}',' ')
text= text.replace('[',' ')
text= text.replace(']',' ')
text= text.replace('<',' ')
text= text.replace('>',' ')
text= text.replace('?',' ')
text= text.replace('`','')
text= text.replace('~',' ')
text= text.replace('?',' ')
text= text.replace('\'',' ')
text= text.replace('....',' ')
text= text.replace('...',' ')
text= text.replace('..',' ')
text= text.replace(' . ','####')
text= text.replace('.',' ')
text= text.replace('####',' . ')
text= text.replace('   ',' ')
text= text.replace('  ',' ')

text = text.split()

#print text
types = 0
tokens = 0
unigram = {}

for w in text:
	if w not in unigram:
		unigram[w] = 1
		tokens += 1
		types += 1
	else:
		unigram[w] += 1
		tokens += 1

print 'tokens',tokens
print 'types',types
key = unigram.keys()
key.sort()
a = 1.0
for w in key:
	a = a*unigram[w]/types
	print w,a
	a =1.0
#print unigram
print types,tokens
