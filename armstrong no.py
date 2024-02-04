num=int(input('enter the number:'))
order=len(str(num))
temp=num
sum=0
while(temp>0):
    i=temp%10
    sum=sum+i**order
    temp=temp//10

if(num==sum):
    print("Armstrong no")
else:
    print("Not an armstrong no")
