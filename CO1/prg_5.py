#Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.
n=int(input("enter number of elements:"))
list2=[]
for i in range(n):
    num=int(input('enter the number:'))
    if num>100:
        list2.append('over')
    else:
        list2.append(num)
print('the output is: ',list2)
