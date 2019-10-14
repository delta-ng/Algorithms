n=int(input())
#length of the wire
dp=[0 for i in range(n+1)]
backtrace=[[] for i in range(n+1)]
for i in range(2,n+1):
	temp=0
	for j in range(1,i):
		if(max(j,dp[j])*max(i-j,dp[i-j])>temp):
			temp=max(j,dp[j])*max(i-j,dp[i-j])
			back=[]
			if(j<dp[j]):
				back.extend(backtrace[j])
			else:
				back.append(j)
			if(i-j<dp[i-j]):
				back.extend(backtrace[i-j])
			else:
				back.append(i-j)
	dp[i]=temp
	backtrace[i]=back
print(dp)
print(backtrace)
