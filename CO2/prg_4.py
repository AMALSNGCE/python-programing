import math
n=int(input("enter a limit:"))
for i in range(1000,n):
    if math.sqrt(i)==int(math.sqrt(i)) and i%2==0:
        print(i)
