import json
import random
from math import gcd

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_large_prime(start=100, end=500):
    primes = [i for i in range(start, end) if is_prime(i)]
    return random.choice(primes)

def find_d(e, lambda_):
    """Finds the modular multiplicative inverse of e modulo lambda_, which should be d."""
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = egcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x, _ = egcd(e, lambda_)
    if gcd != 1:
        raise ValueError("No modular inverse exists for the given e and lambda_.")
    return x % lambda_

def generate_rsa_keys():
    p = generate_large_prime()
    q = generate_large_prime()
    while q == p:  # Ensure p and q are distinct
        q = generate_large_prime()

    n = p * q
    lambda_ = (p - 1) * (q - 1)

    e = 65537  # Most commonly used as e
    if gcd(e, lambda_) != 1:
        e = next(i for i in range(3, lambda_, 2) if gcd(i, lambda_) == 1)

    # Calculate d
    d = find_d(e, lambda_)

    return {"public_key": (e, n), "private_key": (d, n)}

friends = {
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve"
}
keys = {}
for friend in friends:
    keys[friend] = generate_rsa_keys()

with open("friends_keys.json", "w") as f:
    json.dump(keys, f, indent=4)
print("Keys generated and saved to 'friends_keys.json'.")