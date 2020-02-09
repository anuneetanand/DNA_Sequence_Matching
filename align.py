from random import randint as randi

first = "AYCYNRCKCRBP" #[example in slides]
second = "ABCNYRQCLCRPM" #[example in slides]


dp= [[0 for i in range(len(first)+1)] for j in range(len(second)+1)]
trace = [['N' for i in range(len(first)+1)] for j in range(len(second)+1)]

for i in range(1, len(first)+1):
    trace[0][i] = 'L'
for i in range(1, len(second)+1):
    trace[i][0] = 'U'

for i in range(1,len(second)+1):
    for j in range(1,len(first)+1):
        if(first[j-1] == second[i-1]):
            dp[i][j] = dp[i-1][j-1] + 1
            trace[i][j] = 'D'
        else:
            if(dp[i-1][j]>dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
                trace[i][j] = 'U'
            elif(dp[i-1][j]<dp[i][j-1]):
                dp[i][j] = dp[i][j-1]
                trace[i][j] = 'L'
            else:
                dp[i][j] = dp[i][j-1]
                trace[i][j] = 'U/L'


m = len(first)
n = len(second)
i1 = len(first) - 1
i2 = len(second) - 1
align1 = ''
align2 = ''

while n >= 0 and m >= 0:
    if(n==0 and m==0):
        break
    if(trace[n][m] == 'D'):
        align1 = first[i1] + align1
        align2 = second[i2] + align2
        m-=1
        n-=1
        i1-=1
        i2-=1
    elif(trace[n][m] == 'L'):
        align2 = '-' + align2
        align1 = first[i1] + align1
        m-=1
        i1-=1
    elif(trace[n][m] == 'U'):
        align1 = '-' + align1
        align2 = second[i2] + align2
        n-=1
        i2-=1
    else:
        choice = randi(0,1)
        if(choice == 0):
            align1 = '-' + align1
            align2 = second[i2] + align2
            n-=1
            i2-=1
        else:
            align2 = '-' + align2
            align1 = first[i1] + align1
            m-=1
            i1-=1

print(align1)
print(align2)