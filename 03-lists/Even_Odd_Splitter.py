n=int(input("Enter the range: "))
li=[]
print("Enter the elements: ")
for i in range(n):
    num=int(input())
    li.append(num)
even=[]
odd=[]
for num2 in li:
    if num2%2==0:
        even.append(num2)

    if num2%2!=0:
        odd.append(num2)
        
print(f"Even{even} is {len(even)}")
print(f"odd{odd} is {len(odd)}")