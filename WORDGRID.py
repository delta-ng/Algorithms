n=int(input())
for l in range(n):
	n1=int(input())
	strings=[]
	for i in range(n1):
		temp=input()
		if(temp[::-1] not in strings):
			strings.append(temp)
	print(strings)
	if(len(strings)>8):
		print("grid\nsnot\nposs\nible")
	elif(len(strings)<=4):
		for i in strings:
			print(i)
	else:
		strings.sort()
		for i in range(len(strings)):
			top=strings[i]
			for 

	print("\n")
	
