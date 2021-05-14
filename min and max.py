   
num=int(input())
c=0
n=0
temp=num
while num:
    num=num//10
    c+=1
temp2=c-1
num=temp;
c-=1;
a=num%10
b=num//pow(10,c)
while num:
    s=num//pow(10,c)
    num=num%pow(10,c)
    if(c==temp2):
        s=a;
    elif (c==0):
        s=b;
    n=n*10+s
    c-=1
    print(n)
