#Print out all colors from color-list1 not contained in color-list2.
#list diff.py
l1=['red','blue','black','green']
l2=['white','red','yellow','green']
l3=[]
for i in l1:
    if i not in l2:
        l3.append(i)
print(l3)