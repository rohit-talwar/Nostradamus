import os
import re
import string

random = [1,23,15,33]

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
#for w in keys:
#	print w,unigram[w]

#print unigram
filename = 'ngrams-dataset.txt'
f = open(filename,'rU')
lines = f.readlines()
f.close()

for i in random:
	text = lines[i]
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
	text= text.replace('`',' ')
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
	print text
	wordsinsentence = text.split()
	prod_uni = 1.0
	for word in wordsinsentence:
		prod_uni += unigram[word]
#		prod_uni *= unigram[word]*100/types
		
	print prod_uni
	strlength = len(wordsinsentence)
#	print strlength
	j = 0
	prod_bi = 1.0
	a = 1.0
	while j < strlength - 1:
#		prod_bi += z[wordsinsentence[j]][wordsinsentence[j+1]]
		prod_bi = prod_bi*a*z[wordsinsentence[j]][wordsinsentence[j+1]]*100/types
		j += 1
	print prod_bi

