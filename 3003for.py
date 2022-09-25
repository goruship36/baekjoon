origin=[1,1,2,2,2,8] #기본 체스말 구성 (킹,퀸, 비숍, 룩, 나이트, 폰 각각의 수)
now=list(map(int,input().split()))

for i in range(len(origin)):
    origin[i]-=now[i]
for j in origin: #for 문으로 출력
    print(j, end =" ")
