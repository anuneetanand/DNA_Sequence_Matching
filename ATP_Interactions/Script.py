# Anuneet Anand
# 2018022
# IQB Assignment 3
# ATP Interacting Residues
'''
Model Used : Balanced Bagging Classifier with SVM [C=2,gamma=0.1,Kernel="rbf"]
Input Features : Patterns of size 17 encoded as bit arrays
Runs : 5
'''

import pandas as pd
import numpy as np
from sklearn import svm
from imblearn.ensemble import BalancedBaggingClassifier

Encoding = { "A":[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "C":[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "D":[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "E":[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "F":[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "G":[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "H":[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "I":[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "K":[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "L":[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "M":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "N":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], "P":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], "Q":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], "R":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], "S":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], "T":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], "V":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], "W":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], "Y":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], "X":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], }

Train = pd.read_csv("train.data")
Test = pd.read_csv("test1.txt")

Sequences = [("X"*8)+i+("X"*8) for i in Train["Amino Acid Sequence"]]		# Adding X for Padding
Residues = ("X"*8)+''.join(map(str, Test["Lable"]))+("X"*8)					# Adding X for Padding
Patterns = []
Labels = []
Predictors = []

for s in Sequences:
	for i in range(8,len(s)-8):												# Converting Sequences to Patterns of size 17
		r = (s[i-8:i+9]).upper()
		p = [] 
		for j in r:
			p = p + Encoding[j]												# Binary Encoding of Patterns
		if ord(s[i])>96:
			l = 1
		else:
			l = -1
		Patterns.append(p)
		Labels.append(l)

for i in range(8,len(Residues)-8):
	r = (Residues[i-8:i+9]).upper()											# Converting Sequences to Patterns of size 17
	t = []
	for j in r:																# Binary Encoding of Patterns
		t = t + Encoding[j]
	Predictors.append(t)

Average_Predictions = [0 for i in range(len(Predictors))]					# Average of 5 Random Runs

for i in range(5):
	print("> Run:",i+1)
	SVM = svm.SVC(kernel="rbf",gamma=0.1,C=2)
	BBC = BalancedBaggingClassifier(base_estimator=SVM)
	BBC.fit(Patterns,Labels)
	P = BBC.predict(Predictors)
	for i in range(len(P)):
		Average_Predictions[i] += P[i]

for i in range(len(Average_Predictions)):
	if Average_Predictions[i]<0:
		Average_Predictions[i]=-1
	else:
		Average_Predictions[i]=1

Result = pd.DataFrame()														  # Exporting Predictions
Result["ID"] = Test ["ID"]
Result["Lable"] = Average_Predictions
Result.to_csv("2018022_AVG_SVM_BBC.txt",index=False)
print(Result)