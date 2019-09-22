#!/bin/python3

import math
import os
import random
import re
import sys
# Query and answer in o(n) or o(log n)
# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr=[]
    j=n
    fin=[0 for i in range(n)]
    while(j>1):
        arr.append([0 for k in range(j)])
        j=math.ceil(j/2)
    arr.append([0])
    for (a,b,k) in queries :
        a-=1
        b-=1
        i=0
        while(a!=b and i<len(arr)):
            if(a%2==1):
                arr[i][a]+=k
                a+=1
            if(a==b):
                break
            if(b%2==0):
                arr[i][b]+=k
                b-=1
            if(a==b):
                break
            a=math.floor(a/2)
            b=math.floor(b/2)
            i+=1
        if(a==b):
            arr[i][a]+=k
    for j in range(n):
        i=0
        t=j
        while(i<len(arr)):
            fin[j]+=arr[i][t]
            i+=1
            t=math.floor(t/2)
    return max(fin)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
