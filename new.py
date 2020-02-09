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

L1 = len(First)
L2 = len(Second)

DM = numpy.zeros([L1, L2], dtype = int)

for i in range(L1):
   for j in range(L2):
      if (First[i] == Second[j]):
         DM[i][j] = 1

Dot_PlotX = []
Dot_PlotY = []
for i in range(L1):
   for j in range(L2):
      if DM[i][j]==1:
         Dot_PlotX.append(i)
         Dot_PlotY.append(j)

plt.title("Dot-Plot")
plt.scatter(Dot_PlotX,Dot_PlotY)
plt.xlabel("Sequence - 1")
plt.ylabel("Sequence - 2")
plt.xticks(numpy.arange(len(list(First))),list(First))
plt.yticks(numpy.arange(len(list(Second))),list(Second))
#plt.show()

DP = copy.deepcopy(DM)
R_max = L1
C_max = L2

Tuples = []
for i in range(L1):
   P = []
   for j in range(L2):
      P.append((i,j))
   Tuples.append(P)

Max_Tuple = (0,0)
Max_Value = 0

for R in range(L1-1,-1,-1):
   for C in range(L2-1,-1,-1):
      v1 = 0
      v2 = 0
      v3 = 0
      T = (R,C)
      Cur_Max = 0
      
      if ( (R+1 < R_max) and (C+1 < C_max) ):
         v1 = DP[R+1][C+1]
         T = (R+1,C+1)
         Cur_Max = v1
      
      if ( (R+1 < R_max) and (C+2 < C_max) ):
         temp = (R+1,C+2)         
         for k in range(C+2,C_max):
            v2 = max(v2,DP[R+1][k])
            if (v2<DP[R+1][k]):
               temp = (R+1,k)

         if (v2>v1):
            T = temp
            Cur_Max = v2

      if ( (R+2 < R_max) and (C+2 < C_max) ):         
         temp = (R+2,C+1)
         for k in range(R+2,R_max):
            v3 = max(v3,DP[k][C+1]) 
            if(v3 < DP[k][C+1]):
               temp = (k,C+1)

         if (v3>max(v1,v2)):
            T = temp
            Cur_Max = v3

      DP[R][C] += max(v1,v2,v3)
      Tuples[R][C] = T
      if (Max_Value < DP[R][C]):
         Max_Value_At = (R,C)
         Max_Value = DP[R][C]

Seq_1 = ""
Seq_2 = ""

x,y = Max_Value_At[0], Max_Value_At[1]
Trace_Back = [(x,y)]
while ((x<(L1-1)) and ((y<L2-1))):
   Temp_Tuple = Tuples[x][y]
   Trace_Back.append(Temp_Tuple)
   x = Temp_Tuple[0]
   y = Temp_Tuple[1]

#print(Trace_Back)

i = 0
j = 0
F = list(First)
S = list(Second)

while len(Trace_Back)>0:
   T = Trace_Back.pop(0)
   if j==T[1]:
      Seq_1 += F.pop(0)
   else:
      Seq_1 += "_" * (T[1]-j)
      j = T[1]
   if i==T[0]:
      Seq_2 += S.pop(0)
   else:
      Seq_2 += "_" * (T[0]-i)
      i = T[0]
   i +=1
   j +=1


# Generating Output

Dot_Plot = ""
Dot_Plot += ("                                         ____        _           ____  _       _                        \n")   
Dot_Plot += ("                                        |  _ \  ___ | |_        |  _ \| | ___ | |_                      \n") 
Dot_Plot += ("                                        | | | |/ _ \| __|       | |_) | |/ _ \| __|                     \n")
Dot_Plot += ("                                        | |_| | (_) | |___      |  __/| | (_) | |_                      \n")
Dot_Plot += ("                                        |____/ \___/ \____|     |_|   |_|\___/ \__|                     \n\n\n")
Dot_Plot +=("\n")
Dot_Plot += (" |")
for i in Second:
   Dot_Plot += i+" "
Dot_Plot += "\n"
Dot_Plot += ('-'*(2 + 2*len(Second)))
Dot_Plot += "\n"

j = 0
for i in First:
   row = i
   row = row + "|"
   for k in DM[j]:
      if (k == 1):
         row = row + "*"+" "
      else :
         row = row + " "+" "
   Dot_Plot += (row)+"\n"
   j+=1
Dot_Plot += "\n\n\n"

Axis_Spacing = len(str(Max_Value))
Sum_Matrix = ""
Sum_Matrix += "                                     ____                         __  __       _        _                \n"
Sum_Matrix += "                                    / ___| _   _ _ __ ___        |  \/  | __ _| |_ _ __(_)_  __          \n"
Sum_Matrix += "                                    \___ \| | | | '_ ` _ \       | |\/| |/ _` | __| '__| \ \/ /          \n"
Sum_Matrix += "                                     __) | |_| | | | | | |       | |  | | (_| | |_| |  | |>  <           \n"
Sum_Matrix += "                                    |____/ \__,_|_| |_||_|       |_|  |_|\__,_|\__|_|  |_/_/\_\          "+"\n\n\n"
Sum_Matrix += (" | ")

for i in Second:
   Sum_Matrix += str(i) + " "*Axis_Spacing
Sum_Matrix += "\n"
Sum_Matrix += ('-'*(2 + L2*(Axis_Spacing+1)))
Sum_Matrix += "\n"

for i in range(L1):
   Row = First[i]
   Row = Row + "| "
   for j in range(L2):
      Element_Spacing = Axis_Spacing - len(str(DP[i][j])) + 1
      Row += str(DP[i][j]) + " " * Element_Spacing
   Sum_Matrix += (Row)+"\n"
Sum_Matrix += "\n\n\n"

Alignment = ""
Alignment += "                                     _    _ _                                  _             \n"
Alignment += "                                    / \  | (_) __ _ _ __  _ __ ___   ___ _ __ | |_           \n"
Alignment += "                                   / _ \ | | |/ _` | '_ \| '_ ` _ \ / _ \ '_ \| __|          \n"
Alignment += "                                  / ___ \| | | (_| | | | | | | | | |  __/ | | | |_           \n"
Alignment += "                                 /_/   \_\_|_|\__, |_| |_|_| |_| |_|\___|_| |_|\__|          \n"
Alignment += "                                               |___/                                          \n\n\n"


print(Dot_Plot)
print(Sum_Matrix)
print(Alignment)