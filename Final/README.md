# IQB-1

Assignment 1 Of IQB

## Instructions to run the scripts

All scripts run with the standard command : `python Qx.py -i __inputFile__ -o __outputFile__`

# Question-1

The RNA sequence is built from the given DNA sequence by replacing all the T's by U's in the given file.
We maintain a dictionary of proteins corresponding to different codons.
The final output is the protein sequence derived from the RNA sequence. 

# Question-2

For this question, we read the input file, split it line-wise and perform linear serach on all the lines obatined. If the line contains 'HEADER', we extract the header directly. The same goes for TITLE. For the resolution, as specified by the PDB format, it is found in REMARK 2. Thus, it is also extracted easily.

# Question-3

* Two input sequence are given. 
* We first calculate identity score matrix.
* We then Align the two using dynamic programming algorithm **Needleman Wunsch algorithm** This involves creating a Sum Matrix,followed by a trace back
* Output the alignment along with a dot plot and sum-matrix (DP Table)

### Penalties 

|    Ψ     | Score(Ψ) |
| :------: | :------: |
|  Match   |    1     |
| Mismatch |    0     |
|   Gap    |    0     |

**Ψ** represents possible interaction in alignment

### Recurrence relation 

Let `Sum` be our table. `first` and `second` be our sequences. `R_MAX` and `C_MAX` be last row and column of out table.

Initially,	

* `Sum[i,j] = 1` , if 	`first[i] == second[j]`. 

  `Sum[i,j] = 0` ,otherwise

After that,

```python
v1 = Sum[i+1,j+1]
v2 = -∞
v3 = -∞
for k in range(j+2,C_MAX):
	v2 = max(v2,Sum[i+1,k])
for k in range(i+2,R_MAX):
	v3 = max(v2,Sum[k,j+1])
Sum[i,j] = Sum[i,j] + max(v1,v2,v3)
```

