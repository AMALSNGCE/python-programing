file=open("pythonfile.txt","w")
file.write("1. Python was invented by Guido van Rossum.\n2. It is easy to use and Learn.\n3. It supports Object Oriented programming")
file.close()

file=open("pythonfile.txt","r") 
file.seek(0,0)
ff=file.readlines()

for x in range(0,len(ff)):
print(ff[x])
print()
print(ff)
file.close()