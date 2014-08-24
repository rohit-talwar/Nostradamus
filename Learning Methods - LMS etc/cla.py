import random
from numpy import *
from itertools import *

class DataItem:
	def __init__(self,label,linearr):
		self.feature = linearr[:]
		self.classLabel = label
		
class Dataset:
	def __init__(self):
		self.data = []
		
	def readData(self,filename):
		label = 4
		delim =','
		fd = open(filename)
		clabel = {}
		cid = 1
		for line in fd:
			if(len(line)<2):
				continue
			line = line.strip()
			line = line.replace("\n","")
			a = line.split(delim)
			if a[label] not in clabel:
				clabel[a[label]] = cid
				cid = cid + 1
			linearr = [1]
			for i in range(len(a)):
				if(i!=label):
					linearr.append(float(a[i]))
			tmp = DataItem(clabel[a[label]],linearr)
			self.data.append(tmp)

	def writeData(self,filename):
		fd = open(filename,'w')
		for i in range(len(self.data)):
			fd.write(str(self.data[i].classLabel))
			fd.write(" ")
			for element in self.data[i].feature:
				fd.write(str(element))
				fd.write(" ")	
			fd.write('\n')


def splitDataset(complete,folds=2):
	retsplit = []
	length = len(complete.data)
	randata = complete.data[:]
	random.shuffle(randata)
	#print randata
	part = length/folds
	rem = length
	index = 0
	for i in range(folds):
        	small = Dataset()
		rem = rem - part
		if(rem<part):
			part = part+rem
      		for j in range(part):
  			tmp = DataItem(randata[index].classLabel,randata[index].feature)
			small.data.append(tmp)
			index = index+1
		retsplit.append(small)	
        return retsplit

# merging numdatasets given by indices to merge
def mergeDatasets(toMerge,indicesToMerge):	
	tmp = Dataset()
	for i in indicesToMerge:
		for dat in toMerge[i].data:
			tmp.data.append(dat)
	return tmp	
		

class LinearClassifier:
	def __init__(self):
		self.yk = []       	 # this is also a list of lists keeping the different datasets used to arrive at a value of 'a'
		self.label = []   	 # similarly this is the correspinding labels of the tuples in yk
		self.a = []        	 # this is actually a list of lists for the different lines made
		self.distinctLabel = []  # this is the actual number of classlabels present in the dataset
		self.ansA = []		 # this stores the answer/class(es) which was considered for generating a
		self.dim = 0		 # the dimension of the feature vector
		self.modelType = 0

	def loadModel(self,modelfilename):
		fd = open(modelfilename)
		line = fd.readline()
		line = line.strip()
		line = line.split(' ')
		for lab in line:
			self.distinctLabel.append(int(lab))
		line = fd.readline()
		line = line.strip()
		line = line.split(' ')
		self.modelType = int(line[-1])
		line = fd.readline()
		line = line.strip()
		line = line.split(' ')
		numofa = int(line[-1])
		for i in range(int(numofa)):
			line = fd.readline()
			line = line.strip()
			line = line.split(',')
			tmp = []
			for j in line:
				tmp.append(int(j))
#			print tmp
			self.ansA.append(tmp)
			line = fd.readline()
			line = line.strip()
			line = line.split(',')
			tmp = []
			for j in line:
				tmp.append(float(j))
			self.a.append(tmp)

	def saveModel(self,modelfilename):
		fd = open(modelfilename,'w')
		for i in self.distinctLabel:
			fd.write(str(i))
			fd.write(' ')
		fd.write("\n")
		fd.write("modelType = ")
		fd.write(str(self.modelType))
		fd.write("\n")
		fd.write(str(len(self.ansA)))
		fd.write("\n")
		for i in range(len(self.ansA)):
			for j in range(len(self.ansA[i])):
				fd.write(str(self.ansA[i][j]))
				if(j!=len(self.ansA[i])-1):
					fd.write(",")
			fd.write("\n")
			for j in range(len(self.a[i])):
				fd.write(str(self.a[i][j]))
				if(j!=len(self.a[i])-1):
					fd.write(",")
			fd.write("\n")
		fd.close()
# this is the main thing--		
  	def learnModel(self,trainData,algorithm,combination):
		if(combination==1):
			self.modelType = 1
		if(combination==2):
			self.modelType = 2
		if(combination==3):
			self.modelType = 3
		if(combination==4):
			self.modelType = 4
		for train in trainData.data:
			tmp = train.feature[:]
			self.yk.append(tmp)
			self.label.append(train.classLabel)
			if(train.classLabel not in self.distinctLabel):
				self.distinctLabel.append(train.classLabel) 
		self.dim = len(self.yk[0])
		#print self.dim
		trainset = []
		classet = []
		if(combination==3):
			permut = []
			count = -1
			numofclass = len(self.distinctLabel)
			for i in range(numofclass):
				for j in range(numofclass-i-1):
					j=j+i+1
					tmp = []
					tmp.append(self.distinctLabel[i])
					tmp.append(self.distinctLabel[j])
					permut.append(tmp)
			for i in permut:
				count = count + 1
				train = []
				classet.append(i)
				for j in range(len(self.yk)):
					if(self.label[j]==classet[count][0]):
						train.append(self.yk[j])
					if(self.label[j]==classet[count][1]):
						tmp1 = [el*-1 for el in self.yk[j] ]
						train.append(tmp1)
				trainset.append(train)
				  
		
		if(combination==2):
			permut = combinations(self.distinctLabel,2)
			count = -1
			for i in permut:
				count = count + 1
				tmp =[]
				for j in i:
					tmp.append(j)
				train = []
				classet.append(tmp)
				for j in range(len(self.yk)):
					if(self.label[j]==classet[count][0]):
						train.append(self.yk[j])
					if(self.label[j]==classet[count][1]):
						tmp1 = [el*-1 for el in self.yk[j] ]
						train.append(tmp1)
				trainset.append(train)
		if(combination==1):
			for clas in self.distinctLabel:
				tmpu = []
				tmpu.append(clas)
				classet.append(tmpu)
				train = []
				for i in range(len(self.yk)):
					if(self.label[i] == clas):
						train.append(self.yk[i])
					else:
						tmp = [el * -1 for el in self.yk[i] ]
						train.append(tmp)
				trainset.append(train)
		if(algorithm==1):
			for i in range(len(trainset)):
				self.ansA.append(classet[i])
				tmpA = ones((self.dim,1),dtype = int)
				epoch = 0
				unclassified = True
				while (unclassified == True):
					epoch = epoch+1
					tmpA = tmpA.flatten()
					mg = linalg.norm(tmpA)
					tmpA = tmpA/mg
					tmpA = tmpA.transpose()
					epoch = epoch + 1
					if(epoch >= 1500):
						break
					count = 0
					for yi in trainset[i]:
						arrYi = array(yi)
						res = dot(arrYi,tmpA)
						if(res<0):
							tmpA = tmpA.flatten()
							mg = linalg.norm(tmpA)
							tmpA = tmpA/mg
							tmpA = tmpA.transpose()
							count = count+1
							arrYi = arrYi.flatten()
							tmpA = tmpA.flatten()
							tmpA = tmpA+arrYi
							tmpA = tmpA.transpose()
					if(count<=10):
						unclassified = False
				self.a.append(tmpA)
		if(algorithm==2):	
			theta = 0.05
			for i in range(len(trainset)):
				unclassified = True
				self.ansA.append(classet[i])
				tmpA = ones((self.dim,1),dtype = int)
				errorlimit = len(trainset[i])*0.1   # error of 10 percent of the total sample set
				epoch = 0
				batchyk = zeros((self.dim,1),dtype=int)   # the start sum of the misclassified yks
				while unclassified==True:
					count = 0
					epoch = epoch + 1
					#adding the result of prev iteration
					eta = random.random()
#					eta = 1.0/epoch
					magErr = eta*linalg.norm(batchyk) 
					batchyk = batchyk.flatten()
					tmpA = tmpA.flatten()
					tmpA = tmpA + eta*batchyk
					tmpA = tmpA.transpose()
#					if(epoch>1500):
#						break
#					print "upper ",batchyk
					batchyk = zeros((self.dim,1),dtype=int)   # the start sum of the misclassified yks
#					print "lower", batchyk
					for yi in trainset[i]:
						arrYi = array(yi)
						res = dot(arrYi,tmpA)
						if(res<0):
							tmpA = tmpA.flatten()
							mg = linalg.norm(tmpA)
							tmpA = tmpA/mg
							tmpA = tmpA.transpose()
							count = count+1
							arrYi = arrYi.flatten()
							batchyk = batchyk.flatten()
							batchyk = batchyk+arrYi
							batchyk = batchyk.transpose()
					if(magErr<theta):
#						print "THETA ",magErr
						if(magErr==0):
							continue
						break
					if(count<=errorlimit):
						unclassified = False
				self.a.append(tmpA)
		if(algorithm==3):
			b = 1  #  the selected margin
			for i in range(len(trainset)):
				self.ansA.append(classet[i])
				tmpA = ones((self.dim,1),dtype = int)
				#for epoch in range(100):
				errorlimit = len(trainset[i])*0.1   # error of 10 percent of the total sample set
				unclassified = True
				epoch = 0
				while(unclassified == True):
					count = 0
#					if(epoch>1500):
#						break
					epoch = epoch+1
					for yi in trainset[i]:
						epoch = epoch +1
						arrYi = array(yi)
						res = dot(arrYi,tmpA)
						if(res < b):
							count = count+1
							mag = linalg.norm(arrYi)
							naruto = (b-res)/(mag*mag)
							eta = random.random()
							eta = eta*naruto
							arrYi = arrYi.flatten()
							tmpA = tmpA.flatten()
							tmpA = tmpA + eta*arrYi
							tmpA = tmpA.transpose()
							tmpA = tmpA.flatten()
							mg = linalg.norm(tmpA)
							tmpA = tmpA/mg
							tmpA = tmpA.transpose()
					if(count <= errorlimit):
						unclassified = False
					elif(epoch>=1500):
#						print "error is not decreasing - error of ",count
						break
					
				self.a.append(tmpA)
		if(algorithm == 4):
			b = 1  #  the selected margin
			for i in range(len(trainset)):
				self.ansA.append(classet[i])
				tmpA = ones((self.dim,1),dtype = int)
				#for epoch in range(100):
				unclassified = True
				errorlimit = len(trainset[i])*0.1   # error of 10 percent of the total sample set
				epoch = 0
				batchyk = zeros((self.dim,1),dtype=int)   # the start sum of the misclassified yks
				while(unclassified == True):
					count = 0
					eta = random.random()
					batchyk = batchyk.flatten()
					tmpA = tmpA.flatten()
					tmpA = tmpA + eta*batchyk
					tmpA = tmpA.transpose()
					tmpA = tmpA.flatten()
					mg = linalg.norm(tmpA)
					tmpA = tmpA/mg
					tmpA = tmpA.transpose()
#					if(epoch>1000):
#						break
					epoch = epoch +1
					batchyk = zeros((self.dim,1),dtype=int)   # the start sum of the misclassified yks
					for yi in trainset[i]:
						arrYi = array(yi)
						res = dot(arrYi,tmpA)
						if(res < b):
							count = count+1
							mag = linalg.norm(arrYi) #magnitude lol
							naruto = (b-res)/(mag*mag)
							arrYi = arrYi.flatten()
							batchyk = batchyk.flatten()
							batchyk = batchyk + naruto*arrYi
							batchyk = batchyk.transpose()
					if(count <= errorlimit):
						unclassified = False
					elif (epoch>=1500):
#						print "error is not decreasing - error of ",count
#					 	print count
					 	break
				self.a.append(tmpA)
		if(algorithm == 5):
			for i in range(len(trainset)):
				self.ansA.append(classet[i])
				b = ones((len(trainset[i]),1),dtype = int)
				matY = array(trainset[i])
				transY = matY.transpose()
				dotprod = dot(transY,matY)
				invers = linalg.inv(dotprod)
				dagger = dot(invers,transY)
				final = dot(dagger,b)
				ifinal = []
				for ki in final:
					for kj in ki:
						ifinal.append(kj)
				self.a.append(ifinal)
		if(algorithm == 6):
			b = []
			for i in range(len(trainset)):
				self.ansA.append(classet[i])
				tmpA = ones((self.dim,1),dtype = int)
				#for epoch in range(100):
				eta = []
				tmpb = []
				for j in range(len(trainset[i])):
					tmpb.append(1)  # can add random numbers here
					eta.append(random.random())
				b.append(tmpb)	
				theta = 5
				unclassified = True
				setLen = len(trainset[i])
				errorlimit = setLen*0.1   # error of 10 percent of the total sample set
				epoch =0
				while(unclassified == True ):
					if(epoch>=10):
						break
					epoch = epoch + 1
					for yi in range(setLen):
						arrYi = array(trainset[i][yi])
						res = dot(arrYi,tmpA)
						res = b[i][yi] - res
						res = eta[yi]*res
						arrYi = arrYi.flatten()
						arrYi = res*arrYi
						tmpA = tmpA.flatten()
						tmpA = tmpA + arrYi
						tmpA = tmpA.transpose()
						tmpA = tmpA.flatten()
						mg = linalg.norm(tmpA)
						tmpA = tmpA/mg
						tmpA = tmpA.transpose()
						noiseErr = []
						for check in range(setLen):
							arrYi = array(trainset[i][check])
							res = dot(arrYi,tmpA)
							res = b[i][check] - res
							res = eta[check]*res
							arrYi = arrYi.flatten()
							arrYi = res*arrYi
							if(linalg.norm(arrYi)>theta):
								noiseErr.append(check)
						if (len(noiseErr)<15):
							unclassified = False
							break
				self.a.append(tmpA)

	def classifySample(self,sample):
		ansLabel = 0
		sam = array(sample.feature)
		sam = sam.transpose()
		if(self.modelType==1):
			for i in range(len(self.a)):
				tmpdot = dot(self.a[i],sam)
				if(tmpdot>=0):
					return self.ansA[i][0]
		if(self.modelType==2):
			tmpansLabel = []
			for i in range(len(self.a)):
				if(dot(self.a[i],sam)>=0):
					tmpansLabel.append(self.ansA[i][0])
				else:
					tmpansLabel.append(self.ansA[i][1])
			count = {}
			for i in range(len(tmpansLabel)):
				if tmpansLabel[i] not in count:
					count[tmpansLabel[i]] = 1
				else:
					count[tmpansLabel[i]] = count[tmpansLabel[i]] + 1
			majority = -1
			for a in count:
				if (majority<count[a]):
					majority = count[a]
					ans = a
			ansLabel=ans

		if(self.modelType==3):
			reject = []
			for i in range(len(self.a)):
				if(self.ansA[i][0] in reject):
					continue
				if(self.ansA[i][1] in reject):
					continue
				if(dot(self.a[i],sam)>=0):
					reject.append(self.ansA[i][1])  # 1 gets rejected
					finalset = self.ansA[i][0]
				else:
					reject.append(self.ansA[i][0]) 
					finalset = self.ansA[i][1]
			ansLabel = finalset
		return ansLabel

	def classifyDataset(self, testset):
		confusion = {}
		error = 0.0 		# no class misclassified
		for i in self.distinctLabel:
			confusion[i] = {}
			for j in self.distinctLabel:
				confusion[i][j] = 0
		for test in testset.data:
			original = test.classLabel
			modelans = self.classifySample(test)
			if(modelans==0):
				error = error+1
				continue
			if(modelans=="unable to classify"):
				error = error+1
				continue
			if(original!= modelans):
				error = error+1.0
			confusion[original][modelans] = confusion[original][modelans] + 1
			
#			for prediction in modelans:
#				confusion[original][prediction] = confusion[original][prediction] + 1
		error = error/len(testset.data)
		retVal = []
		retVal.append(error)
		retVal.append(confusion)
		return retVal

def crossValidate(complete,folds,algo,comb):
	finalConf = {}
	splitSet = splitDataset(a,folds)
	errSum = 0.0
	sqrSum = 0.0
	for i in range(folds):
		learnfrom = []     			# indices to merge
		for j in range(folds):
			if(i==j):
				if(i==0 and j==0):
					tmp = LinearClassifier()
					tmp.learnModel(complete,0,0)   # no learning req as we only need the distinct labels
					labels = tmp.distinctLabel
					for si in labels:
						finalConf[si] = {}
						for sj in labels:
							finalConf[si][sj] = 0
				continue
			learnfrom.append(j)
		learndata = mergeDatasets(splitSet,learnfrom)
		learnedModel = LinearClassifier()
		learnedModel.learnModel(learndata,algo,comb)
		learnedModel.saveModel("model"+str(i))
		confusion = learnedModel.classifyDataset(splitSet[i])
		errSum = errSum+confusion[0]
		sqrSum = sqrSum + confusion[0]*confusion[0]
		for ki in confusion[1]:
			for kj in confusion[1][ki]:
				finalConf[ki][kj] = finalConf[ki][kj] + confusion[1][ki][kj]
	avErr = errSum/folds
	print "Standard Error",avErr
	sqrSum = sqrSum/folds
	stdDev = math.sqrt(sqrSum-avErr*avErr)
	print "Standard Deviation", stdDev
	for i in finalConf:
	    for j in finalConf[i]:
	    	finalConf[i][j] = finalConf[i][j]/folds
	print "Confusion Matrix",finalConf


a = Dataset()
a.readData("iris.data")
a.writeData("iris")
#l = splitDataset(a,4)
#l[0].writeData("1")
#l[1].writeData("2")
#l[2].writeData("3")
#l[3].writeData("4")
#s = mergeDatasets(l,2,[0,2])
#s.writeData("merge")
#b = LinearClassifier()
#b.learnModel(a,5,1)
#b.saveModel("algo6")
crossValidate(a,5,5,3)
