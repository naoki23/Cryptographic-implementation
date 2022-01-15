import random
import math

def get_random_number():
    digit = 2
    return random.randrange(10 ** (digit - 1), 10 ** digit)

def get_prime_number():
    while(True):

        prime_number = get_random_number()
        prime_sqrt = math.sqrt(prime_number)

        if type(prime_sqrt) == int:
            return prime_number
        else:
            prime_sqrt_only_int = math.floor(prime_sqrt)
        
        for num in range(2, prime_sqrt_only_int):
            if prime_sqrt_only_int % num == 0:
                return prime_number

def lcm(p, q):
    return (p * q) // math.gcd(p, q)

def get_public_key():
    p, q = get_prime_number(), get_prime_number()
    N = p * q
    L = lcm(p-1, q-1)

    for i in range(2, L):
        if math.gcd(i, L) == 1:
            E = i
            break
    
    for i in range(2, L):
        if (E * i) % L == 1:
            D = i
            break
    
    return (E, N), (D, N)

def do_encrypt(public_keys, plain_text):
    E, N = public_keys
    plain_integers = map(ord, plain_text)
    encrypted_integers_iter = [pow(i, E, N) for i in plain_integers]
    encrypted_text = ''.join(chr(w) for w in encrypted_integers_iter)
    return encrypted_text

def do_decrypt(private_keys, encrypted_text):
    D, N = private_keys
    encrypted_integers = map(ord, encrypted_text)
    decrypted_integers_iter = [pow(i, D, N) for i in encrypted_integers]
    decrypted_text = ''.join(chr(w) for w in decrypted_integers_iter)
    return decrypted_text

input_text = input('Please enter text: ')

public_keys, private_keys = get_public_key()
print(f'Public Keys {public_keys}')
print(f'Private Keys {private_keys}')

encrypted_text = do_encrypt(public_keys, input_text)
print(encrypted_text)
decrypted_text = do_decrypt(private_keys, encrypted_text)
print(decrypted_text)
