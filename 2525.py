h,m=map(int, input().split())
cooking=int(input())
m+=cooking
if m>=60:
    temp=m//60 # //연산 : 몫
    h+=temp
    m-=(60*temp)
if h>=24:
    n=h-24
    h=0+n
print(h, m)