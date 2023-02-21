import calculator1 as c
a1=int(input("enter your number"))
b1=int(input("enter your number"))
print("choose your options:")
choice=int(input("Enter the choice:1. Addition 2. Sub 3.Mul 4.Div"))
if choice==1:
    s1=c.sum(a1,b1)
    print(s1)
elif choice==2:
    s2=c.substract(a1,b1)
    print(s2)
elif choice==3:
    s3=c.multiplication(a1,b1)
    print(s3)
elif choice==4:
    s4=c.division(a1,b1)
    print(s4)
else:
    print=int(input("wrong choice"))