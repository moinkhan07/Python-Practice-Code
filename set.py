set0 = {"moin",1,2,"khan",2,"moin"}
set1 = set() # It will create a empty set.

print(type(set1))

for i in set0:
  print(i)

#Methods: 
set1 = {1,2,2,3,4,5,5}
set2 = {10,12,12,13,14,15,15}
set3 = {1,4,6,101}
set4 = {1,2,3,4,5}
set5 ={1,3,5,8,9}
name1 = {"Moin","Khan","Is","A","Villian"}
name2 = {"Moin","Khan","Is","A","Villian"}

if "Moin" in name1:
  print("Yes, Moin is there in name1  variable!")
else:
  print("Not found!")

name1.clear()
print(name1)

del name1
print(name1)

name1.pop()
print(name1)

name1.add("don")
print(name1)

name1.remove("don")
print(name1)

print(name1.issuperset(name2)) # If both have similar value true
print(name2.issubset(name1)) # If both have similar value true

print(name1.isdisjoint(name2)) #If both diff value then true

print(set1.union(set2))

set1.update(set3)
print(set1)

inter = set1.intersection(set3)
print(inter)

symdif = set4.symmetric_difference(set5)
print(symdif)

symdif = set4.difference(set5)
print(symdif)

