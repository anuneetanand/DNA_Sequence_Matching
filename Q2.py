# -*- coding: utf-8 -*-
"""
      IQB, Winter 2020
      Assignment-1
      Question-2
Aditya Singh Rathore : 2018007
Anuneet Anand        : 2018022
Divyam Gupta         : 2018032

"""

import sys

I = open(sys.argv[1],"r")
Data = I.readlines()
I.close()

HEADER = ""
TITLE = ""
RESOLUTION = ""

for L in Data:

	if "HEADER" in L:
		X = L.split()
		for i in X[1:]:
			HEADER = HEADER + i + " "

	if "TITLE" in L:
		X = L.split()
		if TITLE == "":
			for i in X[1:]:
				TITLE = TITLE + i + " "
		else:
			for i in X[2:]:
				TITLE = TITLE + i + " "

	if "RESOLUTION." in L:
		X = L.split()
		x = X.index("RESOLUTION.")
		if x!=len(X)-1:
			RESOLUTION = X[x+1]

HEADER = "HEADER: " + HEADER
TITLE = "TITLE: " + TITLE
RESOLUTION = "RESOLUTION: " + RESOLUTION

print(HEADER)
print(TITLE)
print(RESOLUTION)

O = open(sys.argv[2],"w")
O.write(HEADER + "\n" + TITLE + "\n" + RESOLUTION + "\n")
