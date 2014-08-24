# the first part is to make a training and testing data set

import os
import random
import math

tests = 10  # change the min number of times to run ai2
accuracies = []

for i in range(tests):
	f = open('haberman.data')                  
	lines = 0
	elements = []
	classes = []

	for line in f:
		if(len(line)>1):
			lines += 1
			line =line.replace("\n","")
			tmp = line.split(',')
			elements.append(tmp)
			if(tmp[3] not in classes):
				classes.append(tmp[3])

#	print classes
	confusion = {}
	for clas in classes:
		confusion[clas] = {}
		for a in classes:
			confusion[clas][a] = 0

#	print confusion
	train = random.sample(elements,lines/2)
	test = []

# the above arrays have the values in an arbit order but test will be in sorted order
# the files are sorted
# key - look closely then we only need the test data set to be ordered as
# then we can directly -see- compare where the misses are
	tmp = '%d_train.data' %i
	ftrain =  open(tmp,'w')
	tmp = '%d_test.data' %i
	ftest = open(tmp,'w')

	for line in elements:
		if(line not in train):
			tmp = ','.join(line)+'\n'
			ftest.write(tmp)
			test.append(line)
		else:
			tmp = ','.join(line)+'\n'
			ftrain.write(tmp)
	
# now find the least distance and predict the value
# EXTRA store it in a file and see it neatly :D

	d = 99999999.9
	tmp1 = 0.0
	tmp2 = 0.0
	ans=''
	res = []
	tmp = '%d_res.data' %i
	fans = open(tmp,'w')
	hit = 0
	miss = 0


	for i in range(len(test)):
		d = 99999999.9
		tmp2 = 0.0
		a1 = float(test[i][0])
		a2 = float(test[i][1])
		a3 = float(test[i][2])
		for tru in train:
			tmp2 = 0.0
			tmp1 = 0.0
			tmp1 = float(tru[0]) - a1
			tmp1 *= tmp1
			tmp2 += tmp1
			tmp1 = 0.0
			tmp1 = float(tru[1]) - a2
			tmp1 *= tmp1
			tmp2 += tmp1
			tmp1 = 0.0
			tmp1 = float(tru[2]) - a3
			tmp1 *= tmp1
			tmp2 += tmp1	
			if(tmp2<d):
				d = tmp2
				ans = tru[3]
		res.append(ans)
		confusion[test[i][3]][ans] += 1 
		if(ans==test[i][3]):
			hit += 1
			fans.write('HIT -->  calculated - '+ans+'  expected - '+test[i][3]+'\n')
		else:
			miss +=1
			fans.write('MISS -->  calculated - '+ans+'  expected - '+test[i][3]+'\n')	

#print confusion		
	accuracy = 0.0
	accuracy = hit*100.0/(hit+miss)
	print 'hit ',hit
	print 'miss ',miss
	print 'accuracy ',accuracy
	accuracies.append(accuracy)
	
#accuracy = no of true pos + true neg/total
# to calc using confusion matrix

	for a in confusion:
		print a,
		for b in confusion[a]:
			print confusion[a][b],
		print ""


sum_mean = 0.0
mean = 0.0
  
for a in accuracies:
	sum_mean += a
   
mean = sum_mean/tests
   
   # sd calculation
sum_sd = 0.0
sd = 0.0
 
for a in accuracies:
	tmp = a-mean
	sum_sd += tmp*tmp
 
sd = math.sqrt(sum_sd/tests)

print ' ---->   DEVIATION', sd,'     MEAN',mean

