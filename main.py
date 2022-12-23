def factorial_new_main_toooo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_new_main_toooo(n - 1)


print(factorial_new_main_toooo(5))
