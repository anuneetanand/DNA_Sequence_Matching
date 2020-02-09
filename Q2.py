# Group 7
# Aditya Singh Rathore (2018007)
# Anuneet Anand (2018022)
# Divyam Gupta (2018032)
# IQB - A1 - Q2

import sys

argv = sys.argv

inputFile = ''
outputFile = ''

for i in range(len(argv)):
    if argv[i] == '-i':
        inputFile = argv[i+1]
    elif argv[i] == '-o':
        outputFile = argv[i+1]

inputPtr = open('1ifp.pdb')

lines = inputPtr.readlines()

title = ''
resolution = ''
header = ''

for i in lines:
    if(i.find('TITLE')>=0):
        a = i.split(' ')
        for j in a:
            if((j!='TITLE' and ((j<='1' or j>='9')) and j!='' and j!='\n')):
                title += j + ' '
    if(i.find('REMARK') >=0):
        a = i.split(' ')
        if ('2' in a) and ('RESOLUTION.' in a):
            j = 0
            l = len(a)
            for j in a:
                if (j== 'REMARK' or j == '' or j =='2' or j == 'RESOLUTION.' or j == '\n'):
                    continue
                else:
                    resolution+= j + ' '
    if(i.find('HEADER') >=0):
        a = i.split(' ')
        for j in a:
            if((j!='HEADER' and j!='' and j!='\n')):
                try:
                    checkNum = int(j)
                except ValueError:
                    header += j + ' '
            
print(title)
print(resolution)
print(header)

if(outputFile!= ''):
    try:
        op = open(outputFile, 'x')
    except FileExistsError:
        op = open(outputFile, 'w')    
    op.write('Header : ' + header + '\n')
    op.write('Title : ' + title + '\n')
    op.write('Resolution : ' + resolution + '\n')

