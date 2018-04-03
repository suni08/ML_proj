# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy
import scipy.stats
import xlrd
import math
import matplotlib.pyplot as pt

#Print details of each team member
print("UBitName\t=\tBhumika Khatwani\t\tSunita Pattanayak")
print("personNumber\t=\t50247656\t\t\t50249134")

#Read dataset for statistics analysis
filepath = "university data.xlsx"
workbook=xlrd.open_workbook(filepath)
sheet=workbook.sheet_by_index(0)

#initialisation of matrices used
aa=numpy.zeros((4,sheet.nrows - 2))
covarianceMat=numpy.zeros((4,sheet.nrows - 2))
corrCoef=numpy.zeros((4,sheet.nrows - 2))
l=numpy.zeros((4,4))
m=numpy.zeros((4,4))
n=numpy.zeros((4,4))
meanMatrix=[]
varMatrix=[]
sigmaMatrix=[]
cols=[]
lpdf=[]

cols=("CS Score", "Research Overhead", "Admin Base Pay", "Tuition")

#Finding mean, variance and standard deviation of each variable
for col in range (2,6):
    sum_array = []
    sum_array=sheet.col_values(col,1,sheet.nrows-1)

    #printing mean,variance and standard deviation for each column
    mean='%.3f' % float(numpy.mean(sum_array))
    meanMatrix.append(numpy.mean(sum_array))
    var='%.3f' % float(numpy.var(sum_array))
    varMatrix.append(numpy.var(sum_array))
    sigma='%.3f' % float(numpy.std(sum_array))
    sigmaMatrix.append(numpy.std(sum_array))
    print("mu"+str(col-1),"\t\t=\t",mean)
    print("var"+str(col-1),"\t\t=\t",var)
    print("sigma"+str(col-1),"\t\t=\t",sigma)
    aa[col-2] = sum_array

#Computing Covariance and Coefficient correlation matrix
print("\n")
#Formatting printing upto 3 decimal points
numpy.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
print("COVARIANCE MATRIX :")
covarianceMat = numpy.cov(aa)
print(covarianceMat)

print("\n")

print("CORRELATION COEFFICIENT MATRIX :")
corrCoef = numpy.corrcoef(aa)
print(corrCoef)

pt.plot(corrCoef,"bo")
pt.show()

#Computing max and min element in correlation coefficient matrix
max=min=corrCoef[0][1]
a=b=0
c=d=1
for i in range(0,4):
    for j in range(0,4):
        if i!=j:
            if(min>corrCoef[i][j]):
                min = corrCoef[i][j]
                a = i
                b = j
            if(max<corrCoef[i][j]):
                max = corrCoef[i][j]
                c = i
                d = j
print("\n")
print("Column",cols[a],"and column",cols[b],"are least correlated")
print("Column",cols[c],"and column",cols[d],"are most correlated")

#Calculating normal pdf using library function scipy.stats.norm.pdf
print("\n")
npdf=numpy.zeros((4,sheet.nrows-2))
for col in range (2,6):
    sub_array = []
    sub_array = sheet.col_values(col,1,sheet.nrows-1)
    a=numpy.sort(sub_array)
    npdf[col-2] = scipy.stats.norm.pdf(a,meanMatrix[col-2], sigmaMatrix[col-2])
    pt.plot(a,npdf[col-2])
    pt.show()
    
sum=0
for row in range(0,4):
    for col in range(0,49):
         sum = sum + math.log(npdf[row][col]) 
print("Loglikelihood(normal pdf) : ",'%.3f' % float(sum))       

sum=0
#Calculating PDF for multivariate condition by implementing formula
print("\n")
print("PDF values for each row :")

for row in range(1,50):
    sum_array=[] #Taking each row as input
    sum_array=sheet.row_values(row,2,6)
    #using formula implementation
    l=numpy.subtract(sum_array,meanMatrix)
    m=numpy.matrix.transpose(l)
    n=numpy.linalg.inv(covarianceMat)
    ex=numpy.exp(-0.5*numpy.dot(numpy.dot(m,n),l))
    f=1/(pow(2*3.14,2)*pow(numpy.linalg.det(covarianceMat),0.5))
    pdf=f*ex
    print("PDF for row ",row," \t:\t\t ",pdf)
    lpdf.append(math.log(pdf))
    sum=sum+lpdf[row-1]

print("\n")
print("Loglikelihood(formula implementation) : ",'%.3f' % float(sum))
