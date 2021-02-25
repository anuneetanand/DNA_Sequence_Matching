# CellBots
# Aditya Singh Rathore (2018007)
# Anuneet Anand (2018022)
# Divyam Gupta (2018032)
# Kaggle Script : 1

'''
Model : SVM [ C = 10 , gamma = 0.0025]
Parameters : Amino Acid Composition , Dipepetide Composition (Order:2), Mass, Charge & pI Of Amino Acids
Sources : Pfeature & Biopython Library 
The hyperparameters of SVM model was tuned using GridSearchCV.
The model was tested by using 5-fold cross validation.
'''
import pandas as pd
from sklearn import svm
from sklearn.metrics import roc_auc_score,accuracy_score,confusion_matrix,make_scorer
from sklearn.model_selection import GridSearchCV, cross_val_score, KFold
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from pyteomics import electrochem,mass,parser

# Training Set Data
Train = pd.read_csv("train.csv")
Train_AAC = pd.read_csv("AAC_train.csv")
Train_DP2 = pd.read_csv("DP2F_train.csv")

Train_C = [electrochem.charge(x,len(x)) for x in Train["Sequence"]]
Train_M = [mass.calculate_mass(sequence=x)/len(x) for x in Train["Sequence"]]
Train_PI = [ProteinAnalysis(x).isoelectric_point() for x in Train["Sequence"]]

# Test Set Data
Test = pd.read_csv("test.csv")
Test_AAC = pd.read_csv("AAC_test.csv")
Test_DP2 = pd.read_csv("DP2F_test.csv")

Test_C = [electrochem.charge(x,len(x)) for x in Test["Sequence"]]
Test_M = [mass.calculate_mass(sequence=x)/len(x) for x in Test["Sequence"]]
Test_PI = [ProteinAnalysis(x).isoelectric_point() for x in Test["Sequence"]]

Labels = Train["Lable"]

# Assembing Parameters Of Training set
Features = pd.merge(Train_AAC,Train_DP2,how="inner",on="ID")
Features = Features.iloc[:,1:]
Features["Charge"] = Train_C
Features["Mass"] = Train_M
Features["Iso"] = Train_PI

# Assembing Parameters Of Test set
Predictors = pd.merge(Test_AAC,Test_DP2,how="inner",on="ID")
Predictors = Predictors.iloc[:,1:]
Predictors["Charge"] = Test_C
Predictors["Mass"] = Test_M
Predictors["Iso"] = Test_PI

# Building Model & Making Predictions
Model = svm.SVC(C=10,gamma=0.0025)
Model.fit(Features,Labels)
P = Model.predict(Predictors)

# Writing Data To Output File
Result = pd.DataFrame()
Result["ID"] = Test ["ID"]
Result["Label"] = P
Result.to_csv("CellBots_Entry_1.csv",index=False)
print(Result)

'''
p_grid = {	"C": [5,10], "gamma": [0.0025,0.01,1]	}
svr = svm.SVC()
inner_cv = KFold(n_splits=2, shuffle=True)
outer_cv = KFold(n_splits=5, shuffle=True)
acc_scorer = make_scorer(roc_auc_score)
clf = GridSearchCV(estimator=svr, param_grid=p_grid, cv=inner_cv,refit = True,scoring=acc_scorer,n_jobs=4)
nested_score = cross_val_score(clf, X=Features, y=Labels, cv=outer_cv).mean() 
print(nested_score)
clf.fit(Features,Labels)
Model = clf.best_estimator_
print(clf.best_params_) 
'''