# MLBA Assignment - 2
# Prediction of Peptides
# Group 58 : Anuneet Anand (2018022), Pankil Kalra (2018061), Akanksha Arora (PhD20208)
# Submission ID : anuneet18022@iiitd.ac.in

import sys
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from xgboost import XGBClassifier
from pyteomics import electrochem, mass, parse
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier

AminoAcids = "ACDEFGHIKLMNPQRSTVWY"
Dipeptides = ["AA","AC","AD","AE","AF","AG","AH","AI","AK","AL","AM","AN","AP","AQ","AR","AS","AT","AV","AW","AY","CA","CC","CD","CE","CF","CG","CH","CI","CK","CL","CM","CN","CP","CQ","CR","CS","CT","CV","CW","CY","DA","DC","DD","DE","DF","DG","DH","DI","DK","DL","DM","DN","DP","DQ","DR","DS","DT","DV","DW","DY","EA","EC","ED","EE","EF","EG","EH","EI","EK","EL","EM","EN","EP","EQ","ER","ES","ET","EV","EW","EY","FA","FC","FD","FE","FF","FG","FH","FI","FK","FL","FM","FN","FP","FQ","FR","FS","FT","FV","FW","FY","GA","GC","GD","GE","GF","GG","GH","GI","GK","GL","GM","GN","GP","GQ","GR","GS","GT","GV","GW","GY","HA","HC","HD","HE","HF","HG","HH","HI","HK","HL","HM","HN","HP","HQ","HR","HS","HT","HV","HW","HY","IA","IC","ID","IE","IF","IG","IH","II","IK","IL","IM","IN","IP","IQ","IR","IS","IT","IV","IW","IY","KA","KC","KD","KE","KF","KG","KH","KI","KK","KL","KM","KN","KP","KQ","KR","KS","KT","KV","KW","KY","LA","LC","LD","LE","LF","LG","LH","LI","LK","LL","LM","LN","LP","LQ","LR","LS","LT","LV","LW","LY","MA","MC","MD","ME","MF","MG","MH","MI","MK","ML","MM","MN","MP","MQ","MR","MS","MT","MV","MW","MY","NA","NC","ND","NE","NF","NG","NH","NI","NK","NL","NM","NN","NP","NQ","NR","NS","NT","NV","NW","NY","PA","PC","PD","PE","PF","PG","PH","PI","PK","PL","PM","PN","PP","PQ","PR","PS","PT","PV","PW","PY","QA","QC","QD","QE","QF","QG","QH","QI","QK","QL","QM","QN","QP","QQ","QR","QS","QT","QV","QW","QY","RA","RC","RD","RE","RF","RG","RH","RI","RK","RL","RM","RN","RP","RQ","RR","RS","RT","RV","RW","RY","SA","SC","SD","SE","SF","SG","SH","SI","SK","SL","SM","SN","SP","SQ","SR","SS","ST","SV","SW","SY","TA","TC","TD","TE","TF","TG","TH","TI","TK","TL","TM","TN","TP","TQ","TR","TS","TT","TV","TW","TY","VA","VC","VD","VE","VF","VG","VH","VI","VK","VL","VM","VN","VP","VQ","VR","VS","VT","VV","VW","VY","WA","WC","WD","WE","WF","WG","WH","WI","WK","WL","WM","WN","WP","WQ","WR","WS","WT","WV","WW","WY","YA","YC","YD","YE","YF","YG","YH","YI","YK","YL","YM","YN","YP","YQ","YR","YS","YT","YV","YW","YY"]

def AAC(x):
    ''' Calculates Amino Acid Composition
        x : Amino Acid Sequence represented as string
        returns : 20 x 1 array with % Composition of Amino Acids
    '''
    A = {i:0 for i in AminoAcids}
    for i in range(len(x)): 
        if x[i] in AminoAcids: A[x[i]]+=1
    P = [round((A[i]*100)/len(x),3) for i in AminoAcids]
    return P

def DPC(x):
    ''' Calculates Dipeptide Composition (1st Order)
        x : Amino Acid Sequence represented as string
        returns : 400 x 1 array with % Composition of Dipeptides
    '''
    D = {i:0 for i in Dipeptides}
    for i in range(len(x)-1): 
        if x[i:i+2] in D: D[x[i:i+2]]+=1
    P = [round((D[i]*100)/(len(x)-1),3) for i in Dipeptides]
    return P

def Model_1(train, test):
    ''' Trains the model and Saves the predictions in a CSV file
        train : Training set
        test : Test set
    '''
    # Preprocessing
    X_train = [AAC(x)+DPC(x)+[mass.calculate_mass(sequence=x)/len(x)]+[electrochem.charge(x,len(x))]+[ProteinAnalysis(x).isoelectric_point()] for x in train['Sequence']]
    X_test = [AAC(x)+DPC(x)+[mass.calculate_mass(sequence=x)/len(x)]+[electrochem.charge(x,len(x))]+[ProteinAnalysis(x).isoelectric_point()] for x in test[' Sequence']]
    Y_train = train[' Label']

    # Training
    clf = BaggingClassifier(base_estimator =  RandomForestClassifier(random_state = 2), n_estimators = 100, random_state = 2, n_jobs = -1)
    clf.fit(X_train, Y_train)

    # Predicting
    Y_prob = [x[1] for x in clf.predict_proba(X_test)]
    Y_pred = clf.predict(X_test)

    result = pd.DataFrame()
    result["ID"] = test["ID"]
    result["Label"] = Y_prob
    result.to_csv("Submission_1.csv", index = False)
    result["Label"] = Y_pred
    result.to_csv("Prediction_1.csv", index = False)

def Model_2(train, test):
    ''' Trains the model and Saves the predictions in a CSV file
        train : Training set
        test : Test set
    '''
    # Preprocessing
    X_train = [AAC(x)+[mass.calculate_mass(sequence=x)/len(x)]+[electrochem.charge(x,len(x))]+[ProteinAnalysis(x).isoelectric_point()] for x in train['Sequence']]
    X_test = [AAC(x)+[mass.calculate_mass(sequence=x)/len(x)]+[electrochem.charge(x,len(x))]+[ProteinAnalysis(x).isoelectric_point()] for x in test[' Sequence']]
    Y_train = train[' Label']

    X_train, Y_train, X_test = np.array(X_train), np.array(Y_train), np.array(X_test)
    X_train,Y_train = shuffle(X_train,Y_train,random_state = 3)

    # Training
    param = {'max_depth':25,'objective':'reg:logistic','n_estimators':100,'booster':'gbtree',
            'colsample_bylevel':0.7,'colsample_bytree': 1,'n_thread': 2}

    xgb = XGBClassifier( **param, random_state = 3)
    clf = BaggingClassifier(base_estimator = xgb, n_estimators = 23, random_state = 3, n_jobs = -1)
    clf.fit(X_train, Y_train)

    # Predicting
    Y_prob = [x[1] for x in clf.predict_proba(X_test)]
    Y_pred = clf.predict(X_test)

    result = pd.DataFrame()
    result["ID"] = test["ID"]
    result["Label"] = Y_prob
    result.to_csv("Submission_2.csv", index = False)
    result["Label"] = Y_pred
    result.to_csv("Prediction_2.csv", index = False)

if __name__ == "__main__":

    try:
        train = pd.read_csv(sys.argv[1])
        train.drop(train.tail(1).index,inplace=True)
        test = pd.read_csv(sys.argv[2])
        model = sys.argv[3]
        if model == "1": 
            Model_1(train, test)
        elif model == "2":
            Model_2(train, test)
        elif model == "0":
            Model_1(train, test)
            Model_2(train, test)
        else:
            raise ValueError()

    except IndexError:
        print('Error: please provide the required arguments')
        raise SystemExit(f"Usage: python3 58_script.py <train_data> <test_data> <model>")
    except FileNotFoundError:
        print('Error: unable to find the specified data file')
        raise SystemExit(f"Usage: python3 58_script.py <train_data> <test_data> <model>")
    except ValueError:
        print("Error: invalid model specified")
        raise SystemExit(f"Usage: python3 58_script.py <train_data> <test_data> <model>")

