n=int(input())
m=int(input())
#n-number of edges 
#m-number of vertics
def topo(b,stack,visited):
	for i in range(m):
		if(adj[b][i]==1 and visited[i]==False):
			topo(i,stack,visited)
	stack.append(b)
	visited[b]=True
adj=[[0 for i in range(m)] for i in range(m)]
for i in range(n):
	a,b=list(map(int,input().split()))
	adj[a][b]=1
stack=[]
visited=[False for i in range(m)]
while(visited!=[True for i in range(m)]):
	edge=visited.index(False)
	topo(edge,stack,visited)
print(stack[::-1])
