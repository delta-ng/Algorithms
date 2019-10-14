a=input()
b=input()
dp=[[0 for j in range(len(a)+1)] for i in range(len(b)+1)]
backtrace=[[[] for j in range(len(a)+1)] for i in range(len(b)+1)]
for i in range(len(b)+1):
	for j in range(len(a)+1):
		if(i==0 or j==0):
			dp[i][j]=0
		elif(a[j-1]==b[i-1]):
			dp[i][j]=1+dp[i-1][j-1]
			backtrace[i][j]=backtrace[i-1][j-1]+[a[j-1]]
		else:
			dp[i][j]=max(dp[i-1][j],dp[i][j-1])
			if(dp[i-1][j]>dp[i][j-1]):
				backtrace[i][j]=backtrace[i-1][j]
			else:
				backtrace[i][j]=backtrace[i][j-1]
print(dp[len(b)][-1])
print(backtrace[len(b)][-1])