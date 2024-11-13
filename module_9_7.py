from math import sqrt


def prime_check(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result <= 1:
            print(f'Данное число не относится ни к простым ни к составным числам')
        else:
            print("Простое" if prime_check(result) else "Составное")
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
