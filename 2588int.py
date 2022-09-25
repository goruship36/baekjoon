a=int(input());b=int(input())
b1=b%10
b2=b%100-b1
b3=b-b2-b1
print(b1*a,b2//10*a,b3//100*a,a*(b1+b2+b3),sep="\n")
#test