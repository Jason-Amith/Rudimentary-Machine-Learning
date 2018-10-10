#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jason.A.Fernando
"""

# -*- coding: utf-8 -*-
#--------------------------------------------------------------
import sys
import random

##read data file
datafile = sys.argv[1]
f = open (datafile)#""ionosphere""
# f = open ("ionosphere.data")

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
f = open(labelfile)#"ionosphere.trainlabels.0"
# f = open("ionosphere.trainlabels.0")

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

#initialize flag and iteration parameters
flag = 0
k=0
y_d_p = 0

##calculate error outside the loop
error=0.0
for i in range (rows):
    if(trainlabels.get(i) != None):
        y_d_p = (trainlabels.get(i))*dot_prod(w,data[i])
        # print (y_d_p)
        error += max(0.0, (1.0 - y_d_p))
        # print(error)
        # error += ( dot_prod(w,data[i]) - trainlabels.get(i) )**2
print(error)

#begin iteration
while(flag != 1):
    k+=1
    delf = []
    for i in range(cols):
        delf.append(0)

##compute gradient
    for i in range(rows):
        if(trainlabels.get(i) != None):
            d_p = dot_prod(w, data[i])
            y_d_p = (trainlabels.get(i)*dot_prod(w,data[i]))
            
            for j in range (cols):

                # delf[j] += (d_p - trainlabels.get(i)) * data[i][j]
                 if ( y_d_p < 1):
                     delf[j] += (-1 * (trainlabels.get(i) * data[i][j]))
                 elif(y_d_p >= 1):
                     delf[j] += 0

##update
    for j in range(cols):
        w[j] = w[j] - eta*delf[j]

##compute error
    curr_error = 0
    for i in range (rows):
        if(trainlabels.get(i) != None):
            y_d_p = (trainlabels.get(i))*dot_prod(w,data[i])
            curr_error += max(0, (1.0 - y_d_p))

#            curr_error += ( dot_prod(w,data[i]) - trainlabels.get(i) )**2
#            print(curr_error,k)
#            if(curr_error<0.01):
#                eta = 0.000001
#                if(curr_error<0.001):
#                    eta = 0.0000001
#                    if(curr_error<0.00001):
#                        eta = 0.00000001
#                        if(curr_error<0.000001):
                        #    flag=1
    print(curr_error,k)
    if error - curr_error < 0.00000001:
        flag = 1
    error = curr_error

### print error
## calculate differences in error:

print("count",k)
# print("w =",w)

#normw = 0
#for j in range((cols-1)):
#    normw += w[j]**2
#    print(w[j])

#normw = (normw)**0.5
#print("||w||=", normw)

#d_origin = w[(len(w)-1)] / normw
#print("d =",d_origin)

##make predictions and write to a file
# w = open("a2.txt", "w")
for i in range(rows):
    if(trainlabels.get(i) == None):
        d_p = dot_prod(w, data[i])
        if(d_p > 0):
            # w.write("1", i, '\n')
            print("1",i)
        else:
            # w.write("0", i, '\n')
            print("0",i)
# w.close()













