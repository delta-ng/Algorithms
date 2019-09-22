arr=list(map(int,input().split(" ")))
search=int(input())
def binary(arr,search):
	low=0
	high=len(arr)-1
	while(low<=high):
		mid=int((low+high)/2)
		if(arr[mid]<search):
			low=mid+1
		elif(arr[mid]>search):
			high=mid-1
		else:
			return mid
print(binary(arr,search))
