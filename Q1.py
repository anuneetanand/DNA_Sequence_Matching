# -*- coding: utf-8 -*-
"""
      IQB, Winter 2020
      Assignment-1
      Question-1
Aditya Singh Rathore : 2018007
Anuneet Anand        : 2018022
Divyam Gupta         : 2018032

"""
import sys

X = { 
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T', 
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',                  
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P', 
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R', 
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A', 
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G', 
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S', 
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L', 
        'UAC':'Y', 'UAU':'Y', 'UAA':'*', 'UAG':'*', 
        'UGC':'C', 'UGU':'C', 'UGA':'*', 'UGG':'W', 
    } 

I = open(sys.argv[1],"r")
Data = I.readlines()
I.close()

DNA = ""
for Line in Data:
	if Line[0]!=">":
		DNA = DNA + Line

DNA = DNA.replace("\n","")
print("DNA:",DNA)

RNA = DNA.replace("T","U")
print("RNA:",RNA)

PS = ""

for i in range(0,len(RNA),3):
	PS = PS + X[RNA[i:i+3]]

print("Protein Sequence:",PS)

O = open(sys.argv[2],"w")
O.write(PS + "\n")