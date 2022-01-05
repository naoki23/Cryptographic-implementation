import random
import math

def get_random_number():
    digit = 100
    return random.randrange(10 ** (digit - 1), 10 ** digit)

def get_prime_number():
    while(True):
        prime_number = get_prime_number()
        for num_squared in (num ** 2 for num in range(prime_number)):
            if prime_number % num_squared == 0:
                return prime_number
            else:
                break
        
        prime_sqrt = math.sqrt(prime_number)
        if prime_sqrt is int:
            return prime_number
        else:
            prime_sqrt_previous = math.floor(prime_sqrt)

def do_encrypt(E, N, plain_text):
    plain_integers = map(ord, plain_text)
    encrypted_integers = [pow(i, E, N) for i in plain_integers]
