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
