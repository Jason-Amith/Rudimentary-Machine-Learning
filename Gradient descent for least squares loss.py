#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:39:19 2018

@author: Jason.A.Fernando
"""

# -*- coding: utf-8 -*-
#--------------------------------------------------------------
import sys
import random

##read data file
datafile = sys.argv[1]
f = open (datafile)#""ionosphere""
#f = open ("ionosphere.data")

data = []
i = 0
l = f.readline()

while(l != '') : #read
    a = l.split()
    b = len(a)
    l2 = []
    for j in range(0, b, 1):
        l2.append(float(a[j]))
        if j == (b-1) :
            l2.append(float(1))
        #data.append(l2)

    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])

f.close()
#--------------------------------------------------------------
##read label data
labelfile = sys.argv[2]
f = open(labelfile)#"ionosphere.trainlabels.1.txt"

#f = open("ionosphere.trainlabels.0")

trainlabels = {}
n = []
n.append(0)
n.append(0)

l = f.readline()
while(l != '') : #read

    a = l.split()
    if int(a[0]) == 0:
        trainlabels[int(a[1])] = -1
    else:
        trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
    n[int(a[0])] += 1

##print(trainlabels)
#print(trainlabels)

##initialize w
w = []
for j in range(cols):
    w.append(0)
    w[j] = (0.02 * random.uniform(0,1)) - 0.01
#    w[j] = 1

##define function dot_product
def dot_prod(list1, list2):
    dp = 0
    refw = list1
    refx = list2
    for j in range (cols):
        dp += refw[j] * refx[j]
    return dp

##initialize delf
delf = []
for i in range(cols):
    delf.append(0)

##gradient descent learning rate.
eta = 0.0001

##calculate error outside the loop
error=0.0
for i in range (rows):
    if(trainlabels.get(i) != None):
        error += ( dot_prod(w,data[i]) - trainlabels.get(i) )**2

#initialize flag and iteration parameters
flag = 0
k=0

#begin iteration
while(flag != 1):
    k+=1
    delf = []
    for i in range(cols):
        delf.append(0)
#    print(k)
#max_iterations = 5000
#for k in range(max_iterations):
#    delf = []
#    delf.append(0)s


    for i in range(rows):
        if(trainlabels.get(i) != None):
            d_p = dot_prod(w, data[i])
            for j in range (cols):
#                delf.append(0)
#                print(d_p)
#compute gradient
                delf[j] += (d_p - trainlabels.get(i)) * data[i][j]

##update
    for j in range(cols):
        w[j] = w[j] - eta*delf[j]

##compute error
    curr_error = 0
    for i in range (rows):
        if(trainlabels.get(i) != None):
            curr_error += ( dot_prod(w,data[i]) - trainlabels.get(i) )**2

#    print(curr_error,k)
    if error - curr_error < 0.001:
        flag = 1
    error = curr_error

### print error
## calculate differences in error:

#print("count",k)
#print("w =",w)

#normw = 0
#for j in range((cols-1)):
#    normw += w[j]**2
#    print(w[j])

#normw = (normw)**0.5
#print("||w||=", normw)

#d_origin = w[(len(w)-1)] / normw
#print("d =",d_origin)
##make predictions and write to a file
#fw = open("a2.txt", "w")

for i in range(rows):
    if(trainlabels.get(i) == None):
        d_p = dot_prod(w, data[i])
        if(d_p > 0):
#            fw.write("1", i, '\n')
            print("1",i)
        else:
#            fw.write("0", i, '\n')
            print("0",i)

#fw.close()













