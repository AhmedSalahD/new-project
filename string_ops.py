def f(s):
    try:
        d={}
        for i in s:
            if i not in d:
                d[i]=0
            d[i]+=1
        d
        e=''
        key=d.keys() 
        for k in key:
            e+=k
        return(e,max(d.values()))
    except:
        print('error')
############
def is_palindrome(s):
    try:
        if s[0:len(s)+1].lower()==s[::-1][0:len(s[::-1])+1].lower():
            return True
        else:
            return False
    except:
        print('error')
#########
def solve(a, b):
    try:
        blength = len(b)
        alength = len(a)
        dp = [[False for i in range(alength+1)] for j in range(blength+1)]
        b = " "+b
        a = " "+a
        dp[0][0]=True
        for i in range(1,alength+1):
            if a[i] == '*':
                dp[0][i] = dp[0][i-1]
        for i in range(1,blength+1):
             for j in range(1,alength+1):
                if b[i] == a[j]:
                    dp[i][j] = dp[i-1][j-1]
                elif a[j]=='*':
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[blength][alength]
    except:
        print('error')
#########
import fnmatch
def solve(a,b):
        x=fnmatch.fnmatch(b,a)
        return x
############
def find_nth_occurrence(substring, string, occurrence=1):
    try:
        where = string.find(substring)
        i=len(substring)
        if occurrence == 1:
            where = string.find(substring)
        else:
            while where >= 0 and occurrence > 1:
                where = string.find(substring, where+i)
                occurrence-=1
        return where
    except:
        print('error')
