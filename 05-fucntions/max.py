def max(x):
    largest=x[0]
    for num in x:
        if num > largest:
            largest=num
    return largest

n=int(input("Enter the range: "))
li=[]
print("ENter the elements: ")
for i in range(n):
    nums=int(input())
    li.append(nums)
ans=max(li)
print("Max is: ",ans)
