print("ENter the marks of 3 subs: 0 to 100")
sub1=int(input("SUbject 1: "))
sub2=int(input("SUbject 2: "))
sub3=int(input("SUbject 3 "))
sum=sub1+sub2+sub3
per=(sum/300)*100

if per>=90:
    print("Grade A")
elif per>=75 and per<=89:
    print("Grade B")
elif per>=50 and per<=74:
    print("Grade C")
else:
    print("Fail")
    
