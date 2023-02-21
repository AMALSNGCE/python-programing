#Create a list of colors from comma-separated color names entered by user. Display 
# first and last colors.
list=[]
n=int(input("enter the no of elements"))
for i in range(0,n):
    a=input("enter the items:")
    list.append(a)
print(list)
print("the first and last colors are:",list[0],list[-1])