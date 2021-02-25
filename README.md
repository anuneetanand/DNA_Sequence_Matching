# Quantitative Biology :health_worker:
Assignments in the domain of Quantitative_Biology.

## Folder Structure
```
├── ATP_Interactions
│   ├── 2018022_AVG_SVM_BBC_1.txt
│   ├── 2018022_AVG_SVM_BBC_2.txt
│   ├── Script.py
│   └── train.data
├── AntiFungal_Peptides
│   ├── AAC_test.csv
│   ├── AAC_train.csv
│   ├── CellBots_Entry_1.csv
│   ├── CellBots_SVM.py
│   ├── DP2F_test.csv
│   ├── DP2F_train.csv
│   ├── test.csv
│   └── train.csv
└── DNA_Sequence_Matching
    ├── 1ifp.pdb
    ├── DNA.fa
    ├── Q1.py
    ├── Q2.py
    ├── Q3.py
    └── protein.fa
```

## ATP Interactions :sparkles:
Aim to predict ATP interacting residues in a protein. [**Kaggle**](https://www.kaggle.com/c/iqb213-atp)

**Input Features:** The protein sequences in the training set was processed to obtain patterns of length 17. To handle the corner cases, we appended a hypothetical "X" amino acid at both ends.Each Amino Acid in the pattern was converted to a unique bit array of size 21.Hence each row of input features have a width of 357.   

**Labels:** For each pattern, if the middle residue was ATP binding, label 1 was assigned and -1 otherwise.   

```
Model : Balanced Bagging Classifier with SVM [C=2, gamma=0.1, Kernel="rbf"]
Score : 0.65072 
```
## AntiFungal Peptides :microbe:
Aim to predict AntiFungal Peptides. [**Kaggle**](https://www.kaggle.com/c/iqb2020)

## DNA Sequence Matching :dna:
Computations on DNA Sequences.
```
python Qx.py -i __inputFile__ -o __outputFile__
```

