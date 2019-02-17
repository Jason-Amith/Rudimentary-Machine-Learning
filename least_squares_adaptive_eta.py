#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jason.A.Fernando
"""
# -*- coding: utf-8 -*-
#--------------------------------------------------------------
import sys
import random

def normalizeln(datafile):
    norml = []

    
    for i in range(len(datafile[0])):
       
        norml.append(1)
        
    for j in range(len(datafile)):
        for k in range(len(datafile[0])-1):
            
            norml[k] += (datafile[j][k])**2
            
            

    for i in range(len(datafile)):
        for j in range(len(datafile[0])-1):
            
                datafile[i][j] = (datafile[i][j]/(norml[j])**0.5)
                
    return datafile


def normalize(datafile):
    max = []
    min = []

    
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
                
    return datafile


##read data file
datafile = sys.argv[1]
f = open (datafile)#""ionosphere""


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

# data = normalizeln(data)
data = normalize(data)

rows = len(data)
cols = len(data[0])

f.close()
#--------------------------------------------------------------
##read label data
labelfile = sys.argv[2]
f = open(labelfile)

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
eta = 0.001

##calculate error outside the loop
error=0.0
for i in range (rows):
    if(trainlabels.get(i) != None):
        error += ( dot_prod(w,data[i]) - trainlabels.get(i) )**2

#initialize flag and iteration parameters
flag = 0
k=0

# eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001 ]
# bestobj = 100000000000000

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

###adaptive eta 
    eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001 ]
    bestobj = 100000000000000

    for n in range(0, len(eta_list), 1):
        eta = eta_list[n]

        ## update w
        for j in range(cols):
            w[j] = w[j] - eta*delf[j]

        ##get new error
        curr_error = 0
        for i in range(0, rows, 1):
            if(trainlabels.get(i) != None):
                ##update error
                curr_error += ( dot_prod(w,data[i]) - trainlabels.get(i) )**2

        obj = curr_error
        

    ##update bestobj and best_eta    
        if obj < bestobj:
            bestobj = obj
            besteta = eta

    ##remove the eta for the next
        # eta = 0

    ##insert code here for w = w - eta*dellf
        for j in range(cols):
            w[j] = w[j] + eta*delf[j]
  
    ## use best eta
    if besteta != None:
        eta = besteta

##update w
    for j in range(cols):
        w[j] = w[j] - eta*delf[j]

##compute error
    curr_error = 0
    for i in range (rows):
        if(trainlabels.get(i) != None):
            curr_error += ( dot_prod(w,data[i]) - trainlabels.get(i) )**2
            
            # print(curr_error,k,eta)

    # print(error-curr_error,k,eta)
    
    if error - curr_error < 0.001:
        flag = 1
    error = curr_error
# ---------------------------------
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
# print(k)
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













