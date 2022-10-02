n,x=map(int, input().split())
a=list(map(int,input().split()))
r=[]
for i in range(len(a)):
    if a[i]<x:
        r.append(a[i])
print(*r)