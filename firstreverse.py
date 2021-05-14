num=int(input())
s=c=n=0
temp=num
while num:
    num=num//10
    c+=1
temp2=c-1
num=temp
c=c-1
a=num//pow(10,c)
b=num%10
while num:
    s=num%10
    num=num//10
    if c==temp2:
        s=a
    elif c==0:
        s=b
    n=n*10+s
    c-=1
    print(n)
