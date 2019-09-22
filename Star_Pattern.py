import time
n=int(input("N:"))
m=int(input("Number of pattern in a line:"))
p=int(input("Number of pattern (row):"))
arr=[]
total=2*n-1
char_arr=[]
print(n)
for k in range(p):
	if(k==0):
		for i in range(total):
			if(i+1<=n):
				arr.append(i+1)
				temp=total-(2*len(arr)-1)
				char=" "*(int(temp/2))
				char+="".join(list(map(str,arr[:]+arr[-2::-1])))
				char+=" "*(int(temp/2))
				char*=m
				char_arr.append(char)
			else:
				arr.pop()
				temp=total-(2*len(arr)-1)
				char=" "*(int(temp/2))
				char+="".join(list(map(str,arr[:]+arr[-2::-1])))
				char+=" "*(int(temp/2))
				char*=m
				char_arr.append(char)
			print(char)
			time.sleep(0.1)
	else:
		k1=k%(2*n-1)
		for i in range(len(char_arr)):
			print(char_arr[i][k1:]+char_arr[i][:k1])
			time.sleep(0.1)





