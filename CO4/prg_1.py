class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def get_area(self):
        return self.length*self.breadth
    def get_perimeter(self):
        return 2*(self.length+self.breadth)
    def compare(self,r2):
        if r1.get_area()>r2.get_area():
            print("greater=",r1.get_area())
        else:
            print("greater=",r2.get_area())
    
length1=int(input("enter the length="))
breadth1=int(input("enter the breadth="))
r1=rectangle(length1,breadth1)
print("area=",r1.get_area())
print("perimeter=",r1.get_perimeter())

length2=int(input("enter the length="))
breadth2=int(input("enter the breadth="))
r2=rectangle(length2,breadth2)
print("area=",r2.get_area())
print("perimeter=",r2.get_perimeter())
r1.compare(r2)