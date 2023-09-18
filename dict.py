dic = {
  "name":"Moin",
  "age":19,
  "gender":"Male",
  "eligible":True
}

for k,v in dic.items():
  print(f"The key is {k} and the values is {v}")

print(dic.items())
print(dic["name"])
print(dic.keys())
print(dic.values())

for info in dic.keys():
  print(info ,":", dic[info])

  #Methods:
emp = {
  101:95,
  102:90,
  103:68,
  104:86,
  105:78,
  106:81,
  107:61,
}
emp2 = {
  108:59,
  109:73,
  110:92
}

emp.clear()

emp.update(emp2)
print(emp)

emp.pop(101)

# emp.popitem() It will pop the last key and value

# del emp It will delete the dictionary


print(emp)