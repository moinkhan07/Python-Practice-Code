name = "Moin,Khan,Is,A,Great,Person|||||||||"

print("Using replace: ",name.replace("," , "-"))

print("Using Split: ",name.split(","))

print("Using Splice: ",name[1:3])

print("Using upper: ",name.upper())

print("Using lower: ",name.lower())

print("Using capitalize: ",name.capitalize())

print("Using Count: ",name.count(","))

print("Using center",name.center(50))

print("Using endswith: ",name.endswith("||"))

print("Using rStrip",name.rstrip("|"))

# String Formatting
name = "Moin"
age = 19
sent = f"My name is {name} and I am {age} years old!"
print(sent)

# Docstring 
def square(n):
  '''Here  we will find the square f the n number.''' # Doc string basically the line that is just after the fundtion
  return n**2

ans = square(5)
print(ans)
print(square.__doc__) #Here it will print '''Here  we will find the square f the n number.'''

# PEP 8
