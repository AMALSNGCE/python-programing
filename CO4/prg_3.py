class rectangle:
    def __init__(self):
        self.__length=int(input("length="))
        self.__breadth=int(input("breadth="))

       
    def __lt__(self,ob2):
        area1=self.__length*self.__breadth
        area2=ob2.__length*ob2.__breadth
        print("area of first object",area1)
        print("area of second object",area2)
        return area1<area2
       
   

print("enter the length and breadth of first object")
obj1=rectangle()
print("enter the length and breadth of second object")
obj2=rectangle()


if obj1<obj2:
    print("area of rect1 is less than rect2")
else:
    print("area of rect1 greaterthan rect2")
