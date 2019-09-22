def col_dfs(start):
	global count
	#Since we are updating global variable
	if(color[start]=="W"):
		color[start]="G"
		for i in arr[start]:
			if(color[i]=="G"):
				count+=1
			elif(color[i]=="W"):
				col_dfs(i)
		color[start]="B"
n=int(input("Number of Edge:"))
v=int(input("Number of Vertic:"))
#adj list
arr=[[] for j in range(v)]
color=["W" for i in range(v)]
for i in range(n):
	a,b=list(map(int,input().split()))
	# Directed a->b
	arr[a].append(b)
#Assuming connected graph
count=0
col_dfs(0)
print(count)
