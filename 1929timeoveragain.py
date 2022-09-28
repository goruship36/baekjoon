m, n= map(int, input().split())
for i in range(m,n+1):
    primeNum=1
    if i==1: pass
    for j in range(2,int(i/2)+1):
        if i%j==0:
            primeNum=0
            break
    if primeNum: print(i)