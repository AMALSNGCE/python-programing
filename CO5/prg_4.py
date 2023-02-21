import csv
filename = "details.csv"
ff=open(filename,'r')
#csvreader = csv.reader(ff)
data = csv.DictReader(ff)
print("No. Brand Model")
for x in data:
print(x['No'], x['Brand'], x['Model'])