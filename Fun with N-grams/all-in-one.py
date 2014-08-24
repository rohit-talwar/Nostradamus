# '<' stands for start of a line
# '>' stands for end of a line

import sys
import random
import string

def file(filename):
	f = open(filename, 'rU')
	text = []
	lines = 0
	exclude = set(string.punctuation)
	token = 0
	for line in f:
		lines = lines + 1
		line = ''.join(ch for ch in line if ch not in exclude)
		line = line.lower()
		line = line.split()
		text.append('<')
		for i in line:
			token = token + 1
			text.append(i)
		text.append('>')

	unigram = {}
	bigram = {}
	prob_big = {}
	total = 0

	for word in text:
		if word in unigram:
			unigram[word] = unigram[word] + 1.0
		else:
			unigram[word] = 1.0
			bigram[word] = {}
			prob_big[word] = {}

	prob_uni = unigram.copy()
	for key in prob_uni.keys():
		prob_uni[key] = prob_uni[key]/token
#	print prob_uni
	coverage = prob_uni.copy()
	for key in coverage.keys():
		coverage[key] = coverage[key]*100

	fil=open('unigramTable.txt','w')
        fil.write("Types are : %d\nTokens are:%d\n\n"%(len(unigram)-2,token))
        fil.write("Unigram  |  Count  |  Probability  |  Percentage of Coverage\n\n")
        for key in unigram.keys():
		if key != '<' and key != '>':
	                fil.write("%s  |  %d  |  %f  |  %f\n"%(key,unigram[key],prob_uni[key],coverage[key]))
        fil.close

#	print unigram,

#	print 'token: %d types: %d'%(len(text), len(unigram)),
	i = -1
	for word in text:
	 	i = i+1
		if i != len(text) - 1:
			if text[i + 1] in bigram[word]:
				bigram[word][text[i+1]] = bigram[word][text[i+1]] + 1.0
				prob_big[word][text[i+1]] = prob_big[word][text[i+1]] + 1.0
			else:
				bigram[word][text[i + 1]] = 1.0
				prob_big[word][text[i + 1]] = 1.0

	uni_big = {}
	for key1 in bigram.keys():
		for key2 in bigram[key1].keys():
			if key2 in uni_big:
				uni_big[key2] = uni_big[key2] + bigram[key1][key2]
			else:
				uni_big[key2] = bigram[key1][key2]

#	print uni_big
	for key1 in prob_big.keys():
		for key2 in prob_big[key1].keys():
			count = 0
			for key3 in bigram[key1].keys():
				count = count + bigram[key1][key3]
			prob_big[key1][key2] = prob_big[key1][key2]/count
	fil=open('bigramTable.txt','w')
       	fil.write("Previous  |  Next  |  Count  |  Probability\n\n")
	for key1 in bigram.keys():
		for key2 in bigram[key1].keys():
	                fil.write("%s  |  %s  |  %d  |  %f\n"%(key1,key2,bigram[key1][key2],prob_big[key1][key2]))
	fil.close
	
#	print bigram
#	print prob_big,
	f.close()

	i = 0
	fil=open('predict_line.txt','w')
	while i != 5:
		ind = random.randint(1,lines)
		tmp = 0
		j = 0

		f = open(filename, 'r')
		for line in f:
			if j == ind:
				break
			j = j + 1
		f.close()

		exclude = set(string.punctuation)
		line = ''.join(ch for ch in line if ch not in exclude)
		line = line.lower()
		line = line.split()
		text = []
		new_line = ''

		if len(line) >=6 and len(line) <= 10:
#			print line
			i = i + 1
			text.append('<')
			for j in line:
				text.append(j)
			text.append('>')

			uni_prob = 1.0
			for j in text:
				uni_prob = uni_prob * prob_uni[j]
#			print 'uni', uni_prob

			big_prob = 1.0
			k = -1
			for j in text:
				k = k + 1
				if k != len(text) - 1:
					big_prob = big_prob * prob_big[j][text[k+1]]
#			print 'big', big_prob

			new = []
			for j in range(4):
				new.append(text[j])
			for j in range(len(text) - 5):
#				print new
				mx = 0
				for key, value in prob_big[new[j+3]].iteritems():
					if value > mx:
						mx = value
						lkey = key
				new.append(lkey)

			uni_new = 1.0
			for j in new:
				uni_new = uni_new * prob_uni[j]
#			print 'uni', uni_new

			big_new = 1.0
			k = -1
			for j in new:
				k = k + 1
				if k != len(new) - 1:
					big_new = big_new * prob_big[j][new[k+1]]
#			print 'big', big_new
			selected_line = ' '.join(line)
			fil.write('Selected line: ')
			fil.write(selected_line)
			fil.write('\n')
			fil.write('Unigram Probability: %e\nBigram Probability: %e\n' %(uni_prob, big_prob))
#			print new
			for j in range(len(new)):
				if new[j] != '<' and new[j] != '>':
					new_line = new_line + ' ' + new[j]
				elif new[j] == '>':
					new_line = new_line + ' .'
			fil.write('New line: ')
			fil.write(new_line)
			fil.write('\n\n')
	fil.close

def main():
	file(sys.argv[1])

if __name__ == '__main__':
	main()
