n=int(input())
for l in range(n):
	s=input()
	possible=[0 for i in range(len(s))]
	for i in range(len(s)):
		if(s[i]!="."):
			possible[i]+=1
			for j in range(1,int(s[i])+1):
				if(i-j>=0):
					possible[i-j]+=1
				if(i+j<len(s)):
					possible[i+j]+=1
	if(max(possible)>1):
		print("unsafe")
	else:
		print("safe")


