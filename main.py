def factorial_new_new(n):
  if n == 0:
    return 1
  else:
    return n * factorial_new_new(n - 1)
print(factorial_new_new(5))
