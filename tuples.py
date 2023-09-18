tup = (23,54,12,78,56,81,42) # It will not change
# tup[0] = 50   # It will give us error

print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

print(tup[0:7])

if 540 in tup:
  print("Yes, 54 is in the tup tuples")
else:
  print("No, 54 is not in the tup tuples")

# Tuples Methods 
tup = (1,2,3,4,5,6,1,2,1,2)
temp = list(tup)
temp.append(7)
temp.pop(2)
temp[1] = 101
tup = tuple(temp)
cnt = tup.count(1)
cnt = tup.index(2,4,8)
len = len(tup);
print(len)
print(tup)
print(cnt)