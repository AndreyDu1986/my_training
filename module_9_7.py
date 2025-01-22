import math

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def is_prime_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if is_prime(result):
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@is_prime_decorator
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)