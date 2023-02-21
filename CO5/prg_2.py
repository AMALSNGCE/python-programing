file1=open("pythonfile.txt","r")
for x in file1:
print(x)
file1.seek(0,0)
print(" ")
print()

print("Odd Line: ",end=" ")
file2=open("odd.txt","w")
ff=file1.readlines()
with open('odd.txt','w') as file2:
for x in range(0,len(ff)):
if(x%2!=0):
print(ff[x])
file2.write(ff[x])