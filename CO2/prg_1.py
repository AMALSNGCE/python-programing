# n=int(input("enter your number:"))
# factorial=1
# for i in range(1,n+1):
#     factorial=i*factorial
# print("factorial is:",factorial)


def fact(x):
    if x==1:
        return 1
    else:
        return(x*fact(x-1))
num=int(input("enter a no"))
print("the factorial of",num," is",fact(num))
