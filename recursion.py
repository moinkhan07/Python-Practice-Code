def factorial(n):
  if(n == 1 or n == 0):
    return 1
  else:
    return n * factorial(n-1)

ans = factorial(5)
print(ans)

def fibonacci(num):
  if(num <= 1):
    return num
  else:
    return fibonacci(num-1) + fibonacci(num-2)

ans = fibonacci(5)
print(ans) # Here count start from 1 that is why asnwer is 5

for i in  range(5):
  print(fibonacci(i)) # Here it is starting from 0