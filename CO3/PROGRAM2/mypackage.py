from Graphics.rectangle import*
from Graphics.circle import*
from Graphics.threedgraphics.cuboid import*
from Graphics.threedgraphics.sphere import*

l=int(input("enter the length of rectangle:"))
b=int(input("enter the breadth of rectangle:"))
print("area of rectangle is=",rectarea(l,b))
print("perimeter of rectangle is=",rectperimeter(l,b))
print()
r=int(input("enter the radius of circle:"))
print("area of circle is=",cirarea(r))
print("perimeter of circle is=",cirperimeter(r))
print()
r=int(input("enter the radius of sphere:"))
print("area of sphere is=",sparea(r))
print("perimeter of sphere is=",spperimeter(r))
print()
l=int(input("enter the length of cuboid:"))
b=int(input("enter the breadth of cuboid:"))
h=int(input("enter the height of cuboid:"))
print("area of cuboid is=",cubarea(l,b,h))
print("perimeter of cuboid is=",cubperimeter(l,b,h))