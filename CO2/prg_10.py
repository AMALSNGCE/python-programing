# num=int(input("enter the number:"))
# print("The factors of",num,"are:")
# for i in range(1, num + 1):
#    if num % i == 0:
#        print(i)


import math
n=int(input('Enter the number :'))
print('The factors of ',n,'are ',end=" ")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
