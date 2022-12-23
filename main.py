def factorial_new_main(n):
  if n == 0:
    return 1
  else:
    return n * factorial_new_main(n - 1)
print(factorial_new_main(5))
