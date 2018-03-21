a=int(input("Enter number: "))
sum=0
for i in range(2,a//2+1):
    if(a%i==0):
        sum=sum+1
if(sum<=0):
    print("yes")
else:
    print("no")
