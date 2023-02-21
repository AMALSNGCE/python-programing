#Display future leap years from current year to a final year entered by user

current=int(input("enter the current year:"))
future=int(input("enter the future year:"))
print("the leap years are")
if current<future:
    for i in range(current,future):
        if(i%4==0 and i%100!=0) or(i%400==0):
            print(i)
