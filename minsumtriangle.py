levels=int(input())
tree=[]
tree.append(list(map(int,input().split())))
dp=[[0 for i in range(levels)] for j in range(levels)]
dp[0][0]=tree[0][0]
for i in range(1,levels):
	tree.append(list(map(int,input().split())))
	for j in range(len(tree[-1])):
		if(j==0):
			dp[i][j]=dp[i-1][j]+tree[i][j]
		elif(j==i):
			dp[i][j]=dp[i-1][j-1]+tree[i][j]
		else:
			dp[i][j]=min(dp[i-1][j-1],dp[i-1][j])+tree[i][j]
print(min(dp[-1]))