listOfNames = ["Moin","Abdul","Zeeshan","Vivek","Saqlain"]
listOfMarks = [89,90,78,85,88]

print(listOfNames[0:5:2]) # 0 is start, 5 is end, 2 is jump index

lst = [i for i in range(10) if i%2==0] #List comprehension
print(lst)

for lon in listOfNames:
  print(lon)

for lom in listOfMarks:
  print(lom)

if 81 in listOfMarks:
  print("Yes, It is there!")
else:
  print("No!")

if "Moin" in listOfNames:
  print("Yes, Moin is at the first index in listOfNames!")
else:
  print("Not there!")

# ----------------------------------List Methods-------------------------
listOfNames = ["Moin","Abdul","Zeeshan","Vivek","Saqlain"]
listOfMarks = [85,90,78,85,88]
listOfMarks.append(100)
listOfNames.append("Aqif")
listOfMarks.sort(reverse=True)
listOfNames.sort()
listOfMarks.insert(1,950)

moreMarks = [120,430,896,567,873]
listOfMarks.extend(moreMarks)

print(listOfNames)
print(listOfMarks)