#Create a string from given string where first and last characters exchanged. [eg: python -
#> nythop] 

temp = "python"
print(temp)
a=temp[1:-1]
b=temp[-1] + temp[1:-1] + temp[:1]
print(b)
