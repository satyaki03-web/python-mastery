n=int(input("ENter the range: "))
li=[]
print("ENter the elements:")
for i in range(n):
    num=int(input())
    li.append(num)
l=0
sl=0
for num2 in li:
    if num2>l:
        sl=l
        l=num2
    elif num2!=l and num2>sl:
        sl=num2
print("The second largest is: ",sl)