# IQB-1

Assignment 1 Of IQB

## Instructions to run the scripts

All scripts run with the standard command : `python Qx.py -i inputFile -o outputFile`

## Question-1

For this question, we simply maintain a dictionary of all proteins corresponding to a given sequence of RNA residues. The final output is the protein sequence derived from the RNA sequence. The RNA sequence is built by replacing all the T's by U's in the given file.

## Question-2

For this question, we open the input file, split it line-wise and perform linear serach on all the lines obatined. If the line contains 'HEADER', we extract the header directly. The same goes for TITLE. For the resolution, as specified by the PDB format, it is always found in REMARK 2. Thus, it is also extracted easily.

## Question-3

For this question, we first build the match matrix, i.e., the matrix which contains 1 for a match and 0 for non-matching characters. Then we create the DOTPLOT on the basis of this matrix. Further, we compute the sum matrix using the algorithm as described in the lecture slides. Lastly, we backtrace the sum matrix to derive one of the possible alignments.

NOTE: Since the gap penalty is 0, there can be multiple possible alignments for two given sequences.



