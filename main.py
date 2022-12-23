def factorial_new(n):
  if n == 0:
    return 1
  else:
    return n * factorial_new(n - 1)
print(factorial_new(5))
