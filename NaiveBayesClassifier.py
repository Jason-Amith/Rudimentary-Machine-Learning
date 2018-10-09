# -*- coding: utf-8 -*-
#--------------------------------------------------------------
import sys

#read data file
datafile = sys.argv[1]
f = open (datafile)#""breast_cancer.txt""
# f = open ("breast_cancer.txt")

data = []
i = 0
l = f.readline()

while(l != '') : #read
    a = l.split()
    b = len(a)
    l2 = []
    for j in range(0, b, 1):
        l2.append(float(a[j]))
        #data.append(l2)

    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])

f.close()
#--------------------------------------------------------------
##read label data
labelfile = sys.argv[2]
f = open(labelfile)#"breast_cancer.trainlabels.1.txt"

# f = open("breast_cancer.trainlabels.1.txt")

trainlabels = {}
n = []
n.append(0)
n.append(0)

l = f.readline()
while(l != '') : #read
    #trainlabels = {}
    a = l.split()
    trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
    n[int(a[0])] += 1

##print(trainlabels)
#print(trainlabels)



## compute means
m0 = []
for j in range(0, cols, 1):
      m0.append(1)

m1 = []
for j in range(0, cols, 1):
      m1.append(1)

for i in range(0, rows, 1):
    #print(trainlabels[i])
    if( trainlabels.get(i) != None and trainlabels[i] == 0):
        for j in range(cols):
            m0[j] = m0[j] + data[i][j]

    if( trainlabels.get(i) != None and trainlabels[i] == 1):
        for j in range(cols):
            m1[j] = m1[j] + data[i][j]

for j in range(0, cols, 1):
        m0[j] = m0[j]/n[0]
        m1[j] = m1[j]/n[1]

#print (m0)
#print (m1)


## compute  standard deviations
sd0 = []
sd0.append(0)
sd1 = []
sd1.append(0)

sqsd0 = []
for j in range(0, cols, 1):
      sqsd0.append(0)


sqsd1 = []
for j in range(0, cols, 1):
      sqsd1.append(0)

for i in range(0, rows, 1):
  if( trainlabels.get(i) != None and trainlabels[i] == 0):
     for j in range(0, cols, 1):
        sqsd0[j] = sqsd0[j] + (m0[j] - data[i][j])**2

  if( trainlabels.get(i) != None and trainlabels[i] == 1):
     for j in range(0, cols, 1):
        sqsd1[j] = sqsd1[j] + (m1[j] - data[i][j])**2

for j in range(0, cols, 1):
      sd0.append(0)
      sd1.append(0)
      sd0[j] = (sqsd0[j]/(n[0]-1))**0.5
      sd1[j] = (sqsd1[j]/(n[1]-1))**0.5

#print (sd0)
#print (sd1)

## calculate likelihood and classify
p0 = []
for j in range(0, cols, 1):
      p0.append(0)

p1 = []
for j in range(0, cols, 1):
      p1.append(0)


for i in range(0, rows, 1):
    if( trainlabels.get(i) == None):
        p0 = 0
        p1 = 0
        for j in range(0, cols, 1):
            p0 += ((m0[j] - data[i][j])/sd0[j])**2
            p1 += ((m1[j] - data[i][j])/sd1[j])**2

        if(p0<p1):
            print("0",i)


        elif(p1<p0):
            print("1",i)





