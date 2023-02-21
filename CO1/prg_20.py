#From a list of integers, create a list removing even numbers.
l1= [11, 22, 33, 44, 55, 66, 77, 88, 99]
print("List Items = ",l1)
for i in l1:
    if (i % 2 == 0):
        l1.remove(i)
print("List Items after removing even Items = ",l1)