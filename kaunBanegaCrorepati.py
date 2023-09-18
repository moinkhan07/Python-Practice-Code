listOfQuestions = ["1.What is the capital of India?","2.Who is the national Bird in India?","3.Who is the president of India?","4.What is the programming language is used to create android apps?"]
listOfAnswers = ["a.Mumbai | b.Kolkata | c.Delhi | d.Chennai","a.Peacock | b.Pegion | c.Elephant | d.Lion","a.Narendra Modi | b.Yogi | c.Rahul Gandhi | d.Droupadi Murmu","a.Javascript | b.Python | c.Spring Boot | d.Kotlin"]

i = 0
count = 0
while(i < 4):
  print(listOfQuestions[i])
  print(listOfAnswers[i])
  ans = input("Choose Option: ")
  if(listOfQuestions[i] == "1.What is the capital of India?" and ans == "c"):
    print("Correct Option!, You won 1K")
    print("============================================")
    count = count + 1000
  elif(listOfQuestions[i] == "2.Who is the national Bird in India?" and ans == "a"):
    print("Correct Option!, You won 5k")
    print("============================================")
    count = count + 5000
  elif(listOfQuestions[i] == "3.Who is the president of India?" and ans == "d"):
    print("Correct Option!, You won 10k")
    print("============================================")
    count = count + 10000
  elif(listOfQuestions[i] == "4.What is the programming language is used to create android apps?" and ans == "d"):
    print("Correct Option!, You won 50K")
    print("============================================")
    count = count + 50000
  else:
    print("Oop's Wrong Answer!")
    print("============================================")
    break

  i = i + 1
print("You Won:",count)
print("============================================")
count = 0
