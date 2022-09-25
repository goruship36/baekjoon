origin=[1,1,2,2,2,8] #기본 체스말 구성 (킹,퀸, 비숍, 룩, 나이트, 폰 각각의 수)
now=list(map(int,input().split()))

for i in range(len(origin)):
    origin[i]-=now[i]
print(*origin) # print(*리스트명) 으로 출력하면 리스트의 대괄호([])와 컴마(,) 가 떼어져서 출력된다

#2022.09.25
"""
list 와 tuple 앞에 *(asterisk) 붙이면 인자들을 일일히 넘기는 것과 같은 효과를 준다
list unpacking (리스트 압축해제)
------------# print(*origin) 대신 for 문으로 출력하는 방법#------------
"""
# for j in origin:
#     print(j, end =" ")