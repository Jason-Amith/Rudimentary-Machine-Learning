#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jason.A.Fernando
"""

# -*- coding: utf-8 -*-
#--------------------------------------------------------------
import sys
import random
import math

def sigmoid(v):
    if v < 0:
        return 1 - 1 / (1 + math.exp(v))
    return 1 / (1 + math.exp(-v))

def normalize(datafile):
    max = []
    min = []

    # writeData = open("normalized","w")
    for i in range(len(datafile[0])):
        max.append(0)
        min.append(0)
        
    for j in range(len(datafile)):
        for k in range(len(datafile[0])-1):
            if (datafile[j][k] > max[k]) :
                max[k] = datafile[j][k]
            if (datafile[j][k] < min[k]) :
                min[k] = datafile[j][k]

    for i in range(len(datafile)):
        for j in range(len(datafile[0])-1):
            if (max[j] - min[j] != 0):
                datafile[i][j] = (datafile[i][j] - min[j])/(max[j] - min[j])
                # writeData.write(str(datafile[i][j]) + " ")
        # writeData.write("\n")
    return datafile
    
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

data = normalize(data)

rows = len(data)
cols = len(data[0])

# ## #check if normalising is required
# maxd = 0
# mind = 0
# normal = 0
# for i in range(cols):
#     maxd = max(data[0])
#     if (maxd > 1):
#         normal = 1

# if normal == 1 :
#     data = normalize(data)

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
    trainlabels[int(a[1])] = int(a[0])
    # if int(a[0]) == 0:
    #     trainlabels[int(a[1])] = -1
    # else:
    #     trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
    n[int(a[0])] += 1


##initialize w
w = []
for j in range(cols):
    w.append(0)
    w[j] = (0.02 * random.uniform(0,1)) - 0.01
#    w[j] = 1

##define function dot_product
def dot_prod(list1, list2):
    dp = 0
    for j in range(len(list1)):
        dp += list1[j] * list2[j]
    return dp

##initialize delf
delf = []
for i in range(cols):
    delf.append(0)

##gradient descent learning rate.
eta = 0.01

#initialize flag and iteration parameters
flag = 0
k=0
y_d_p = 0

# #regularised risk.
# reg_w = 0
# for j in range(cols):
#     reg_w += w[j]**2

##calculate error outside the loop
error=0.0
# class1cost = 0
# class2cost = 0
for i in range (rows):
    if(trainlabels.get(i) != None):
        y_d_p = (trainlabels.get(i))*dot_prod(w,data[i])
        d_p = dot_prod(w,data[i])
        y = trainlabels.get(i)
        sigm = (1/(1 + math.exp(-1*d_p)))
        error += (-y*math.log(sigm))-((1-y)*math.log((1-sigm)))
        

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
            y = trainlabels.get(i)
            sigm = (1/(1 + math.exp(-1*d_p)))
            for j in range (cols):
                
                delf[j] += (-y + sigm) * data[i][j]
    # for j in range(cols):
    #     delf[j] += 0.1*w[j]             

##update
    for j in range(cols):
        w[j] = w[j] - eta*delf[j]

    # reg_w = 0
    # for j in range(cols-1):
    #     reg_w += w[j]**2

##compute error
    curr_error = 0
    for i in range (rows):
        if(trainlabels.get(i) != None):
            y_d_p = (trainlabels.get(i))*dot_prod(w,data[i])
            d_p = dot_prod(w, data[i])
            y = trainlabels.get(i)
            sigm = (1/(1 + math.exp(-1*d_p)))
            curr_error += (-y*math.log(sigm))-((1-y)*math.log((1-sigm))) 
            
            if(abs(error - curr_error)<eta):
                eta = 0.1*eta
                
           
                           
    # print(k,curr_error,eta,abs(error - curr_error))
    
    ##check objective
    if abs(error - curr_error) < 0.00000001:
        flag = 1
    error = curr_error


# print("count",k)
# print("w =",w)

# normw = 0
# for j in range((cols-1)):
#    normw += w[j]**2
#    print(w[j])

# normw = (normw)**0.5
# print("||w||=", normw)

# d_origin = w[(len(w)-1)] / normw
# print("d =",d_origin)

##make predictions and write to a file
# w = open("a2.txt", "w")
for i in range(rows):
    if(trainlabels.get(i) == None):
        d_p = dot_prod(w, data[i])
        if d_p > 0.5:
            # w.write("1 " + str(i) + "\n")
            print("1",i)
        else:
            # w.write("1 " + str(i) + "\n")
            print("0",i)
# w.close()














