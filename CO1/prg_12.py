#Accept a file name from user and print extension of that. 
a = input("enter the Filename: ")
b= a.split(".")
print ("The extension of the file is : ",b[-1])