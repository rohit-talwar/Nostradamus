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
text= text.replace('?','')
text= text.replace('`','')
text= text.replace('~',' ')
text= text.replace('?',' ')
text= text.replace('\'','')
text= text.replace('....',' ')
text= text.replace('...',' ')
text= text.replace('..',' ')
#text= text.replace(' . ','####')
#text= text.replace('.','')
#text= text.replace('####',' . ')
text= text.replace('.','')
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
	if len(text[i])>1: 	   
		if text[i] not in z:
			z[text[i]] = {}
			tokens += 1 
			types += 1
		if len(text[i+1]) > 1:
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
	text= text.replace('`','')
	text= text.replace('~',' ')
	text= text.replace('?',' ')
	text= text.replace('\'','')
	text= text.replace('....',' ')
	text= text.replace('...',' ')
	text= text.replace('..',' ')
#	text= text.replace(' . ','####')
#	text= text.replace('.','')
#	text= text.replace('####',' . ')
	text= text.replace('.','')
	text= text.replace('   ',' ')
	text= text.replace('  ',' ')
	print text
	wordsinsentence = text.split()
	strlength = len(wordsinsentence)
	new_sen=[]
	new_ct = -1
	temp = 0
	while new_ct < 2:
		if len(wordsinsentence[temp])>1:
			new_sen.append(wordsinsentence[temp])
			new_ct = new_ct + 1
		temp = temp + 1
#	print 'temp', temp, new_ct,new_sen[new_ct]
	j=0
	while j < (strlength-3):
		max_f = 0
		for nxtword in z[new_sen[new_ct]]:
#			print 'word in dict ', nxtword
			if z[new_sen[new_ct]][nxtword] > max_f :
				max_f = z[new_sen[new_ct]][nxtword]
				new_entry = nxtword
		new_sen.append(new_entry)
#		print new_entry, max_f
		new_ct = new_ct+1
		j = j+1
	print new_sen
	strlength = len(new_sen)
	j = 0
        prod_bi = 1.0
	qwert = 1.0
	while j < strlength - 1:
		prod_bi = prod_bi*qwert*z[new_sen[j]][new_sen[j+1]]/bigramtypes
#		prod_bi += float(z[new_sen[j]][new_sen[j+1]])
#	print float(z[new_sen[j]][new_sen[j+1]])
		j += 1
	print prod_bi

