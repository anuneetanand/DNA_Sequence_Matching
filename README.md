# Quantitative Biology :health_worker:

## Folder Structure
```
├── ATP_Interactions
│   ├── Script.py
│   └── train.data
├── AntiFungal_Peptides
│   ├── AAC_test.csv
│   ├── AAC_train.csv
│   ├── CellBots_SVM.py
│   ├── DP2F_test.csv
│   ├── DP2F_train.csv
│   ├── test.csv
│   └── train.csv
├── DNA_Sequence_Matching
│   ├── 1ifp.pdb
│   ├── DNA.fa
│   ├── Q1.py
│   ├── Q2.py
│   ├── Q3.py
│   └── protein.fa
├── Interacting_Patterns
│   ├── 58_script.py
│   ├── README.pdf
│   ├── test_data.csv
│   └── train_data.csv
├── Peptide_Classification
│   ├── 58_script.py
│   ├── README.pdf
│   ├── test.csv
│   └── train.csv
└── README.md
```

## ATP Interactions :sparkles:
Aim to predict ATP interacting residues in a protein. [**Kaggle**](https://www.kaggle.com/c/iqb213-atp) 
```
Model : Balanced Bagging Classifier with SVM(C=2, gamma=0.1, Kernel="rbf")
Score : 0.65072 
```
## AntiFungal Peptides :microbe:
Aim to predict AntiFungal Peptides. [**Kaggle**](https://www.kaggle.com/c/iqb2020)
```
Model : SVM(C = 5 , gamma = 0.003)
Score : 0.86444
```
## Interacting Patterns ♨️
Aim to predict Interacting Peptideds. [**Kaggle**](https://www.kaggle.com/c/mlba2021a1)
```
Model : estimators = [ ('rf', RandomForestClassifier(n_estimators=300, max_depth=45, min_samples_leaf=7, random_state=r)), ('mlp',      MLPClassifier(max_iter=200,random_state=r)), ('knn', KNeighborsClassifier(n_neighbors=4))] 
clf = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression( random_state=r), n_jobs=-1, verbose = 3)
Score : 0.64764
```
## Peptide Classification ⚕️
Aim to classify Peptides. [**Kaggle**](https://www.kaggle.com/c/peptide)
```
Model : BaggingClassifier(base_estimator =  RandomForestClassifier(random_state = 2), n_estimators = 100, random_state = 2, n_jobs = -1)
Score : 0.78620
```
## DNA Sequence Matching :dna:
Computations on DNA Sequences.
```
python Qx.py -i __inputFile__ -o __outputFile__
```
## Collaborators
[Aditya Singh Rathore](https://github.com/aditya18007)   
[Divyam Gupta](https://github.com/dgupta04)   
[Pankil Kalra](https://github.com/pankilkalra)

