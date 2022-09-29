h,m=map(int, input().split())
if m<45:
    m+=15 
    #45보다 작은 분은 60분을 꿔와서 -45 이므로
    #m+60-45 => m+=15
    if h==0: h=23
    else: h-=1
else: m-=45
print(h,m)