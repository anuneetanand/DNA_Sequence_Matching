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
import copy
import sys

for i in range(len(sys.argv)):
    if sys.argv[i] == '-i':
        inputFile = sys.argv[i+1]
    elif sys.argv[i] == '-o':
        outputFile = sys.argv[i+1]

I = open(inputFile, 'r')
Data = I.readlines()
Sequences = [] 

for Line in Data:
   if (len(Line) > 2 and Line[0] != ">"):
      Sequences.append(Line[0:len(Line)-1])

First = Sequences[0]
Second = Sequences[1]

#First = "AYCYNRCKCRBP" #[example in slides]
#Second = "ABCNYRQCLCRPM" #[example in slides]

DM = numpy.zeros([len(First), len(Second)], dtype = int)

for i in range(len(First)):
   for j in range(len(Second)):
      if (First[i] == Second[j]):
         DM[i][j] = 1

#plt.imshow(numpy.array(DM))
DotPlotX = []
DotPlotY = []
for i in range(len(First)):
   for j in range(len(Second)):
      if DM[i][j]==1:
         DotPlotX.append(i)
         DotPlotY.append(j)

plt.title("Dot-Plot")
plt.scatter(DotPlotX,DotPlotY)
plt.xlabel("Sequence - 1")
plt.ylabel("Sequence - 2")
plt.xticks(numpy.arange(len(list(First))),list(First))
plt.yticks(numpy.arange(len(list(Second))),list(Second))
#plt.show()

DP = copy.deepcopy(DM)
R_max = len(First)
C_max = len(Second)

for R in range(len(First)-1,-1,-1):
   for C in range(len(Second)-1,-1,-1):
      v1 = 0
      v2 = 0
      v3 = 0

      if ( (R+1 < R_max) and (C+1 < C_max) ):
         v1 = DP[R+1][C+1]

      if ( (R+1 < R_max) and (C+2 < C_max) ):
         for k in range(C+2,C_max):
            v2 = max(v2,DP[R+1][k])
      
      if ( (R+2 < R_max) and (C+2 < C_max) ):         
         for k in range(R+2,R_max):
            v2 = max(v2,DP[k][C+1]) 

      DP[R][C] += max(v1,v2,v3)

DP[0][0] = 300
Max = DP[0][0]
Axis_Spacing = len(str(Max))
Sum_Matrix = ""
Sum_Matrix += (" | ")

for i in Second:
   Sum_Matrix += str(i) + " "*Axis_Spacing
Sum_Matrix += "\n"
Sum_Matrix += ('-'*(2 + len(Second)*(Axis_Spacing+1)))
Sum_Matrix += "\n"

for i in range(len(First)):
   Row = First[i]
   Row = Row + "| "
   for j in range(len(Second)):
      Element_Spacing = Axis_Spacing - len(str(DP[i][j])) + 1
      Row += str(DP[i][j]) + " " * Element_Spacing
   Sum_Matrix += (Row)+"\n"
Sum_Matrix += "\n\n\n"

print(Sum_Matrix)