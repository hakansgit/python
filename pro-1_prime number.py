def is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6

    return True

for n in range(1,50):
    print(f"{n} is " + ("not " if not is_prime(n) else "") + "a prime")