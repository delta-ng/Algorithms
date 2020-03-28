arr=list(map(int,input().split()))
dp=[1 for i in range(len(arr))]
index=[-10 for i in range(len(arr))]
for i in range(1,len(arr)):
	val=max([[dp[j],j] if arr[j]<arr[i] else [0,0] for j in range(i)])
	# print(val)
	dp[i]=1+val[0]
	if(val[0]!=0):
		index[i]=val[1]
max_index=dp.index(max(dp))
temp_var=max_index
result=[]
while(temp_var!=-10):
	result.append(arr[temp_var])
	temp_var=index[temp_var]
print(result[::-1])
print("Total",max(dp))
