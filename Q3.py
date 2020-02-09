# -*- coding: utf-8 -*-
"""
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

#first = "AYCYNRCKCRBP" #[example in slides]
#second ="ABCNYRQCLCRPM" #[example in slides]
first = "rADITYA"
second = "ADITYA"
opt = numpy.zeros([len(first), len(second)], dtype = int)


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

tuples = []

for i in range(len(first)):
   l = []
   for j in range(len(second)):
      l.append((i,j))
   tuples.append(l)
maxTup = (0,0)
maxValue = 0

for i in range(len(first)-1,-1,-1):
   for j in range(len(second)-1,-1,-1):
      R = i
      C = j
      v1 = 0
      v2 = 0
      v3 = 0
      tup = (R,C)
      curMax = 0
      if ((R+1<R_max) and (C+1<C_max)):
         v1 = opt[R+1][C+1]
         tup = (R+1,C+1)
         curMax = v1
      if ((R+1<R_max) and (C+2<C_max)):
         temp = (R+1,C+2)         
         for k in range(C+2,C_max):
            v2 = max(v2,opt[R+1][k])
            if (v2<opt[R+1][k]):
               temp = (R+1,k)

         if (v2>v1):
            tup = temp
            curMax = v2

      if ((R+2<R_max) and (C+2<C_max)):         
         temp = (R+2,C+1)
         for k in range(R+2,R_max):
            v3 = max(v3,opt[k][C+1]) 
            if(v3 < opt[k][C+1]):
               temp = (k,C+1)

         if (v3>max(v1,v2)):
            tup = temp
            curMax = v3
      opt[R][C] += max(v1,v2,v3)
      tuples[R][C] = tup
      if (maxValue < opt[R][C]):
         maxValueAt = (R,C)
         maxValue = opt[R][C]
         

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
alignment += "                                                              |___/                                          \n\n\n"



x,y = maxValueAt[0],maxValueAt[1]
traceBack = [(x,y)]
while ((x<(len(first)-1)) and ((y<len(second)-1))):
   tempTuple = tuples[x][y]
   traceBack.append(tempTuple)
   x = tempTuple[0]
   y = tempTuple[1]


while(len(traceBack)>0):
   tempTup = traceBack.pop(0)
   alignment += "first sequence index = "+str(tempTup[0])+"   second sequence index = "+str(tempTup[1])+"\n"


alignment+="\n"

print(dotPlot)
print(sumMatrix)
print(alignment)
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
