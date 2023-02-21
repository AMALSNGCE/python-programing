list1=[1,2,3,9,5]
list2=[6,2,8,9,10]
print(list1)
print(list2)
if len(list1)==len(list2):
    print("list 1 and list 2 are same length")
else:
    print("list 1 and list 2 are not same length")
if sum(list1)==sum(list2):
    print("sum of list1 and list 2 are same")
else:
    print("sum of list1 and list 2 are not same")
list3=[i for i in list1 if i in list2]
if len(list3)>0:
    print("the common elemnts are:",list3)
else:
    print("no common elements")