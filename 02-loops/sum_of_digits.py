n=int(input("Enter a number: "))
copy=n
sum=0
while n>0:
    d=n%10
    sum=sum+d
    n//=10
print("The sum of digits is: ",sum)