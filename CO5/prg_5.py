import csv
field_names = ['No', 'Brand', 'Model']
mobs = [
{'No': 1, 'Brand': 'Apple','Model': 'iPhone X'},
{'No': 2, 'Brand': 'Samsung', 'Model': 'S21Ultra'},
{'No': 3,'Brand':'OnePlus', 'Model': '9Pro'},
{'No': 4, 'Brand': 'Xiaomi', 'Model': 'Redmi Note 4'},
]
with open("mobdetails.csv","w") as csvfile:
writer = csv.DictWriter(csvfile, fieldnames = field_names)
writer.writeheader()
writer.writerows(mobs)#print(" ")
filename = "mobdetails.csv"
ff=open(filename, 'r')
rows=[]
csvreader = csv.reader(ff)
for r in csvreader:
rows.append(r)
for r in rows[:4]:
print(*r)