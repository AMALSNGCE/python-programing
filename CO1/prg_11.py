#Find biggest of 3 numbers entered.
a=int(input('enter the value a='))
b=int(input('enter the value b='))
c=int(input('enter the value c='))
if a>b and a>c:
    print("greatest is a=",a)
elif b>a and b>c:
    print('greatest is b=',b)
else:
    print('greatest is c=',c)