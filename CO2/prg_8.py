a=[]
n=int(input("enter the number of elements in list:"))
for i in range(1,n+1):
    element=input("enter the words:")
    a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
    if (len(i))>max1:
        max1=len(i)
        temp=i
print("the word with longest length is:",temp)
        