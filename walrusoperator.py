#Walrus Operator is ':='
# numbers = [1,2,3,4,5]
# while(n := (len(numbers)) > 0):
#     print(f"The pop number is {numbers.pop()}"


                                                  # Normal Way 
# foods = list()
# while(True):
#     print("Write quit to exit!")
#     food = input("Which food do you like: ")
#     if(food == "quit"):
#         break
#     foods.append(food)
# print(foods)

# Best Example for understanding the walrus operator with the above example
foods = list()
while(food := input("Which food do you like:")) != "quit":
    foods.append(food)
print(f"You like all these foods:{foods}")


