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
#text = text.replace(',',' ')
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

types =0
bigramtypes =0
tokens =0
#print text
tot = len(text)
z = {}
i=0
while i<tot-1:
    if text[i] not in z:
            z[text[i]] = {}
	    tokens += 1 
	    types += 1
    if text[i+1] not in z[text[i]]:
            z[text[i]][text[i+1]] = 1
	    bigramtypes += 1
	    tokens += 1 
    else:
            z[text[i]][text[i+1]] += 1
	    tokens += 1 
    i += 1
 
#print z
print tokens, types, bigramtypes

## making the unigram counts

keys = z.keys()
keys.sort()

unigram = {}

for w in keys:
	for y in z[w]:
		if y not in unigram:
			unigram[y] = z[w][y]
		else:
			unigram[y] += z[w][y]

keys = unigram.keys()
keys.sort()
t = 1.0
for w in keys:
	t = t*unigram[w]/types
	print w,t
	t = 1.0
t =1.0
for w in z:
	for q in z[w]:
		t = t*z[w][q]/bigramtypes
		print w,q,t
		t = 1.0

