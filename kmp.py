def longestPrefix(s):
        if len(s)==1:
            return ""
        j,i=0,1
        lps=[0 for i in range(len(s))]
        while(i<len(s)):
            if(s[j]==s[i]):
                lps[i]=j+1
                i+=1
                j+=1
            else:
                if(j==0):
                    lps[i]=0
                    i+=1
                else:
                    j=lps[j-1]
        return lps
def kmp(s,p):
    lps=longestPrefix(p)
    i,j=0,0
    while(i<len(s)):
        if(s[i]==p[j]):
            if j==len(p)-1:
                return [i-j,i]
            i+=1
            j+=1
        else:
            if(j==0):
                i+=1
            else:
                j=lps[j-1]
    return False
print(kmp(input(),input()))