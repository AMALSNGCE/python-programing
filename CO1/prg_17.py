#dict sort.py
people = {3: "abhi", 2: "denver", 4: "caterine", 1: "basil"}
d1=dict(sorted(people.items()))
print(d1)
d2=dict(sorted(people.items(), key=lambda item: item[1]))
print(d2)
d1=dict(sorted(people.items(),reverse=True))
print(d1)
d2=dict(sorted(people.items(), key=lambda item: item[1] ,reverse=True))
print(d2)
