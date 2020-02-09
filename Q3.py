# -*- coding: utf-8 -*-
"""
    IQB , Winter 2020
      Assignment-1
      Question-3

Aditya Singh Rathore : 2018007
Anuneet Anand        : 2018022
Divyam Gupta         : 2018032

"""

print("   ___   ___ _____ ")
print("  / _ \ / _ \___  |")
print(" | | | | | | | / / ")
print(" | |_| | |_| |/ /  ")
print("  \___/ \___//_/   ")

import matplotlib.pyplot as plt
import numpy

file1 = open('protein.fa', 'r')
Lines = file1.readlines()
sequences = [] 

for i in Lines:
   if (len(i) > 2 and i[0] != ">"):
      sans_EOL = i[0:len(i)-1]
      sequences.append(sans_EOL)

first = sequences[0]
second = sequences[1]

opt = numpy.zeros([len(first), len(second)], dtype = int)

points = []

for i in range(len(first)):
   for j in range(len(second)):
      if (first[i] == second[j]):
         opt[i][j] = 1
blank = ' '
nonblank = '*'

#The dot-plot
dotPlot = ""
dotPlot += ("                            _____ _                ____        _   ____  _       _                        \n")   
dotPlot += ("                           |_   _| |__   ___      |  _ \  ___ | |_|  _ \| | ___ | |_                      \n") 
dotPlot += ("                             | | | '_ \ / _ \_____| | | |/ _ \| __| |_) | |/ _ \| __|                     \n")
dotPlot += ("                             | | | | | |  __/_____| |_| | (_) | |_|  __/| | (_) | |_                      \n")
dotPlot += ("                             |_| |_| |_|\___|     |____/ \___/ \__|_|   |_|\___/ \__|                     \n\n\n")
dotPlot +=("\n")

dotPlot += (" |")
for i in second:
   dotPlot += i+" "
dotPlot += "\n"
dotPlot += ('-'*(2 + 2*len(second)))
dotPlot += "\n"

count = 0
for i in first:
   row = i
   row = row + "|"
   for k in opt[count]:
      if (k == 1):
         row = row + str(nonblank)+" "
      else :
         row = row + str(blank)+" "
   dotPlot += (row)+"\n"
   count+=1
dotPlot += "\n\n\n"

plt.imshow(numpy.array(opt))
x_axis = plt.xticks(numpy.arange(len(list(second))),list(second))
y_axis = plt.yticks(numpy.arange(len(list(first))),list(first))

#The sum matrix

"""
cell(R,C) = cell(R,C) + max(v1,v2,v3)
where
v1 = cell(R+1,C+1)
v2 = cell(R+1,C+2 to C_max)
v3 = cell(R+2 to R_max,C+2)

"""
C_max = len(second)
R_max = len(first)

for i in range(len(first)-1,-1,-1):
   for j in range(len(second)-1,-1,-1):
      R = i
      C = j
      v1 = 0
      v2 = 0
      v3 = 0

      if ((R+1<R_max) and (C+1<C_max)):
         v1 = opt[R+1][C+1]

      if ((R+1<R_max) and (C+2<C_max)):
         
         for k in range(C+2,C_max):
            v2 = max(v2,opt[R+1][k])
      
      if ((R+2<R_max) and (C+2<C_max)):         
         for k in range(R+2,R_max):
            v3 = max(v3,opt[k][C+1]) 

      opt[R][C] += max(v1,v2,v3)
      
r = len(first) -1
c = len(second) -1
i1 = len(first) - 1
i2 = len(second) - 1
align1 = ''
align2 = ''

while r>=1 and c>=1:
   neighbourhood = [opt[r-1][c-1], opt[r-1][c], opt[r][c-1]]
   maxReq = max(neighbourhood)
   if(opt[r-1][c-1] == maxReq):
      align1 = first[i1] + align1
      align2 = second[i2] + align2
      r-=1
      c-=1
      i1-=1
      i2-=1
      continue
   elif(opt[r][c-1] == maxReq):
      align1 = '-' + align1
      align2 = second[i2] + align2
      i2-=1
      c-=1
      continue
   else:
      align2 = '-' + align2
      align1 = first[i1] + align1
      i1-=1
      r-=1

if(r==1):
   align1 = '-' + align1
   align2 = second[i2] + align2
if(c==1):
   align2 = '-' + align2
   align1 = first[i1] + align1

if(i1>=0):
   align1 = first[:i1+1] + align1
if(i2>=0):
   align2 = second[:i2+1] + align2


sumMatrix = ""
sumMatrix += "                            _____ _               ____                  __  __       _        _                \n"
sumMatrix += "                           |_   _| |__   ___     / ___| _   _ _ __ ___ |  \/  | __ _| |_ _ __(_)_  __          \n"
sumMatrix += "                             | | | '_ \ / _ \____\___ \| | | | '_ ` _ \| |\/| |/ _` | __| '__| \ \/ /          \n"
sumMatrix += "                             | | | | | |  __/_____|__) | |_| | | | | | | |  | | (_| | |_| |  | |>  <           \n"
sumMatrix += "                             |_| |_| |_|\___|    |____/ \__,_|_| |_| |_|_|  |_|\__,_|\__|_|  |_/_/\_\          "+"\n\n\n"

sumMatrix += (" | ")
for i in second:
   sumMatrix += str(i)+" "
sumMatrix += "\n"
sumMatrix += ('-'*(2 + 2*len(second)))
sumMatrix += "\n"

for i in range(len(first)):
   row = first[i]
   row = row + "| "
   for j in range(len(second)):
      row += str(opt[i][j]) + " "
   sumMatrix += (row)+"\n"
   count+=1
sumMatrix += "\n\n\n"

#The Alignment


alignment = ""
alignment += "                            _____ _                  _    _ _                                  _             \n"
alignment += "                           |_   _| |__   ___        / \  | (_) __ _ _ __  _ __ ___   ___ _ __ | |_           \n"
alignment += "                             | | | '_ \ / _ \_____ / _ \ | | |/ _` | '_ \| '_ ` _ \ / _ \ '_ \| __|          \n"
alignment += "                             | | | | | |  __/_____/ ___ \| | | (_| | | | | | | | | |  __/ | | | |_           \n"
alignment += "                             |_| |_| |_|\___|    /_/   \_\_|_|\__, |_| |_|_| |_| |_|\___|_| |_|\__|          \n"
alignment += "                                                              |___/                                          \n"

aligned1 = "                                  " + align1  
aligned2 = "                                  " + align2 + '\n\n' 

print(dotPlot)
print(sumMatrix)
print(alignment)
print(aligned1)
print(aligned2)

responseCorrect = False
while not responseCorrect:
   print("Do you want image of the dot plot ? (y or n)")
   response = input()
   if(response == "Y" or response == "y" or response == "N" or response == "n"):
      responseCorrect = True
      if response == "y" or response == "Y":
         plt.show()
   else:
      print("\nWrong input\nTry again\n\n\n")
      responseCorrect = False