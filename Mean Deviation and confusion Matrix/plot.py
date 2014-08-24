import matplotlib as mp
import matplotlib.pyplot as plt
import numpy

f = open('iris.data','r')

sepal1 = []
petal1 = []
sepal2 = []
petal2 = []
sepal3 = []
petal3 = []

for line in f:
	if(len(line)>1):
		line = line.replace("\n","")
		line = line.split(",")
		if(line[4]=="Iris-setosa"):
			sepal1.append(float(line[1]))
			petal1.append(float(line[3]))
		elif(line[4]=="Iris-versicolor"):
			sepal2.append(float(line[1]))
			petal2.append(float(line[3]))
		else:
			sepal3.append(float(line[1]))
			petal3.append(float(line[3]))

# making decision region
# -0.5 to 3 in y and x - 1.5 to 5

yy = numpy.arange(-0.5,3,0.1)
xx = numpy.arange(1.5,5,0.1)
nx1 = []
ny1 = []
nx2 = []
ny2 = []
nx3 = []
ny3 = []
dbx = []
dby = []
for i in xx:
	flag1 = 0
	for j in yy:
		min1 = 9999999
		min2 = 9999999
		min3 = 9999999
		for one in range(len(sepal1)):
			tmp1=i-sepal1[one]
			tmp2=j-petal1[one]
			tmp3=tmp1*tmp1 + tmp2*tmp2
			if(tmp3<min1):
				min1 = tmp3
		for one in range(len(sepal2)):
			tmp1=i-sepal2[one]
			tmp2=j-petal2[one]
			tmp3=tmp1*tmp1 + tmp2*tmp2
			if(tmp3<min2):
				min2 = tmp3
		for one in range(len(sepal3)):
			tmp1=i-sepal3[one]
			tmp2=j-petal3[one]
			tmp3=tmp1*tmp1 + tmp2*tmp2
			if(tmp3<min3):
				min3 = tmp3
		if(min1<min2 and min1<min3):
			if(flag1 != 1 and j>0):
				dbx.append(i)
				dby.append(j)
			else:
				nx1.append(i)
				ny1.append(j)
			flag1 = 1
		if(min3<=min1 and min3<=min2):
			if(flag1 != 2 and j>0):
				dbx.append(i)
				dby.append(j)
			else:
				nx3.append(i)
				ny3.append(j)
			flag1 = 2
		if(min2<min1 and min2<min3):
			if(flag1 != 3 and j>0):
				dbx.append(i)
				dby.append(j)
			else:
				nx2.append(i)
				ny2.append(j)
			flag1 = 3

#making a line - 
		

plt.plot(sepal1, petal1, 'ro', sepal2, petal2, 'gs', sepal3, petal3, 'b^',dbx,dby,'bx')
#plt.plot(nx1, ny1, 'ro', nx2, ny2, 'gs', nx3, ny3, 'b^',dbx,dby,'bx')
#plt.scatter(sepal1,petal1,marker='o',c='b')
#plt.scatter(nx1,ny1,marker='o',c='b')
#plt.scatter(sepal2,petal2,marker='x',c='r')
#plt.scatter(nx2,ny2,marker='x',c='r')
#plt.scatter(sepal3,petal3,marker='^',c='g')
#plt.scatter(ny3,ny3,marker='^',c='g')
plt.ylabel("petal width")
plt.xlabel("sepal width")
plt.show()

