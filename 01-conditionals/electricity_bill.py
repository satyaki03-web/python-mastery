n=int(input("ENter the total unit consumed: "))
amt=0.0
if n<0:
    print("Invalid Input")
else:
    if n<=100:
        amt=n*5
    elif n<=200:
        amt= (100*5)+((n-100)*7)
    else:
        amt=(100*5)+(100*7)+((n-200)*10)

    amt+=50

    if amt>1500:
        amt*=1.10

print(f"Total Bill: ₹{amt:.2f}")