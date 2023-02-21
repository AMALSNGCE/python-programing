# #Find gcd of 2 numbers. 
# #gcd.py
# import math
# a=int(input('Enter a number:'))
# b=int(input('Enter another number:'))
# gcd=math.gcd(a,b)
# print('the gcd of two numbers are',gcd)


def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("enter the number"))
b=int(input("enter the number"))
gcd=gcd(a,b)
print("gcd is ",gcd)