def factorial_new_main_tooood(n):
    if n == 0:
        return 1
    else:
        return n * factorial_new_main_tooood(n - 1)


print(factorial_new_main_tooood(5))
