import string
str_=input()
dp=[[[0,0] for i in range(26)] for j in range(len(str_))]
str_to_num=dict(zip(string.ascii_lowercase, range(0,26)))
for i in range(len(str_)):
	 if(i==0):
	 	dp[0][str_to_num[str_[i]]]=[1,0]
	 else:
	 	dp[0][str_to_num[str_[i]]][1]+=1
for i in range(1,len(str_)):
	for alpha in range(26):
		if(alpha==str_to_num[str_[i]]):
			x,y=dp[i-1][alpha]
			dp[i][alpha]=[x+1,y-1]
		else:
			dp[i][alpha]=dp[i-1][alpha]
max_=0
for i in range(len(str_)):
	sum_=0
	for alpha in range(26):
		sum_+=min(dp[i][alpha])
	if(sum_>max_):
		max_=sum_
print(max_)

