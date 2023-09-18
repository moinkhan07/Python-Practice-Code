num = input("Enter any number: ")
print(f"Multiplication table of {num}:")

try:
  for i in range(1,11):
    print(f"{int(num)} X {i} = {int(num)*i}")
except Exception as e:
  print("Invalid input!")
finally:
  print("Finally block")

print("Program end here!")

#raising custom error:
a = input("Enter a number between 5 to 10: ")

if not (a == "quit"):
  if(int(a) < 5 or int(a) > 10 ):
    raise ValueError("Number should be between 5 to 10!")