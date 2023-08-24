print("Find the factorial")
n = int(input("Enter a number: "))


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


result = factorial(n)
print(f"The factorial of {n} is {result}")
