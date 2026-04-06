def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


num = int(input("Enter a number: "))

if is_prime(num):
    print("It is a prime number")
else:
    print("It is NOT a prime number")