# -*- coding: utf-8 -*-
"""
    IQB , Winter 2020
      Assignment-1
      Question-3

Aditya Singh Rathore : 2018007
Anuneet Anand        : 2018022
Divyam Gupta         : 2018032

"""

import matplotlib.pyplot as plt
import numpy
import sys

I = open(sys.argv[1], 'r')
Data = I.readlines()
Sequences = [] 

for Line in Data:
   if (len(Line) > 2 and Line[0] != ">"):
      Sequences.append(Line[0:len(Line)-1])

First = Sequences[0]
Second = Sequences[1]

First = "AYCYNRCKCRBP" #[example in slides]
Second = "ABCNYRQCLCRPM" #[example in slides]

DP = numpy.zeros([len(First), len(Second)], dtype = int)

for i in range(len(First)):
   for j in range(len(Second)):
      if (First[i] == Second[j]):
         DP[i][j] = 1


plt.imshow(numpy.array(DP))
x_axis = plt.xticks(numpy.arange(len(list(Second))),list(Second))
y_axis = plt.yticks(numpy.arange(len(list(First))),list(First))
#plt.show()

'''
The sum matrix
cell(R,C) = cell(R,C) + max(v1,v2,v3)
wh
C_max = len(Second)
R_max = len(First)

for i in range(len(First)-1,-1,-1):
   for j in range(len(Second)-1,-1,-1):
      R = i
      C = j
      v1 = 0
      v2 = 0
      v3 = 0

      if ((R+1<R_max) and (C+1<C_max)):
         v1 = DP[R+1][C+1]

      if ((R+1<R_max) and (C+2<C_max)):
         
         for k in range(C+2,C_max):
            v2 = max(v2,DP[R+1][k])
      
      if ((R+2<R_max) and (C+2<C_max)):         
         for k in range(R+2,R_max):
            v2 = max(v2,DP[k][C+1]) 

      DP[R][C] += max(v1,v2,v3)