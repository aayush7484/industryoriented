def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


# We will find the factorial of this number
print(factorial(5))