m, n= map(int, input().split())
for i in range(m,n+1): #파이썬은 m 부터 n까지를 의미
    primeNum=1
    if i==1: pass
    for j in range(2,i):
        if i%j==0:
            primeNum=0
            break
    if primeNum: print(i)