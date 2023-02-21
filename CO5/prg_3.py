import csv

filename = "sername.csv"

fields = []
rows = []

ff=open(filename,'r')
csvreader = csv.reader(ff)
fields = next(ff)
print(fields)
for r in csvreader:
rows.append(r)
print(rows)
print(" ")
print('\nFirst 4 Rows are: \n')
for r in rows[:4]:
print(*r)
print(" ")
print()
print("The File Content")
print()


for xy in rows:
for z in xy:
print(z)
print(" ")
print()
#print(z,end=" ")
print()
ff.close()