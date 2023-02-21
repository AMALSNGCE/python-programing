#List comprehensions:
#(a) Generate positive list of numbers from a given list of integers
#(b) Square of N numbers
#(c) Form a list of vowels selected from a given word
#(d) List ordinal value of each element of a word (Hint: use ord() to get ordinal values)

#answer (a)
l=[-1,2,3,4,5,6,7]
pn=[i for i in l if  i>= 0]
print(pn)

#answer(b)
k=[1,2,3,4,5,6]
sn=[2**i for i in k]
print(sn)

#answer(c)
a=str(input("enter the word"))
vwl=["A","I","O","E","U","a","e","i","o","u"]
s=[i for i in a if i in vwl]
print(s)

#answer(d)
w=input("enter the word:")
s=[ord(i) for i in w]
print(s)