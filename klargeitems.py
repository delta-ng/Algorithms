import heapq
arr=[1,100,20,31,50,5,1001,200,10]
k=3
i=k+1
temp=arr[:k+1]
heapq.heapify(temp)
while(i!=len(arr)):
	heapq.heapreplace(temp,arr[i])
	i+=1
print(temp[1:])

# print(heapq.nlargest(3,arr))