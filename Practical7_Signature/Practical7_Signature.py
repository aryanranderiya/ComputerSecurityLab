import random

# Function to compute greatest common divisor (gcd)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to compute modular inverse of e mod phi(n)


def mod_inverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % phi

# Function to compute (base^exp) % mod using iterative method (modular exponentiation)


def power_mod(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# Simple hash function (sum of ASCII values of characters in message)


def simple_hash(message):
    return sum(ord(char) for char in message)

# Key generation function


def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose public exponent e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = 65537  # Commonly used prime for RSA
    if gcd(e, phi) != 1:
        raise ValueError("e and phi(n) are not coprime")

    # Compute private exponent d
    d = mod_inverse(e, phi)

    return (e, n), (d, n)  # Public key (e, n), Private key (d, n)

# Signing the message


def sign_message(message, private_key):
    d, n = private_key
    hashed_message = simple_hash(message)
    signature = power_mod(hashed_message, d, n)  # S = m^d % n
    return signature

# Verifying the signature


def verify_signature(message, signature, public_key):
    e, n = public_key
    hashed_message = simple_hash(message)
    verified_hash = power_mod(signature, e, n)  # m' = S^e % n
    return hashed_message == verified_hash


# Example usage
if __name__ == "__main__":
    # Example prime numbers (for real-world use, these should be much larger)
    p = 61
    q = 53

    # Generate public and private keys
    public_key, private_key = generate_keys(p, q)

    # Original message
    message = "Hello, RSA!"

    # Sign the message
    signature = sign_message(message, private_key)
    print(f"Signature: {signature}")

    # Verify the signature
    is_valid = verify_signature(message, signature, public_key)
    print(f"Signature valid: {is_valid}")


# Primality test using trial division (suitable for small primes)
def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to generate a random prime number within a range


def generate_random_prime(start, end):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

# Key generation function with random prime numbers


def generate_keys():
    # Choose two large random prime numbers p and q
    p = generate_random_prime(50, 500)  # Adjust range as needed
    q = generate_random_prime(50, 500)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose public exponent e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = 65537  # Commonly used prime for RSA
    if gcd(e, phi) != 1:
        raise ValueError("e and phi(n) are not coprime")

    # Compute private exponent d
    d = mod_inverse(e, phi)

    return (e, n), (d, n)  # Public key (e, n), Private key (d, n)

# Remaining functions (gcd, mod_inverse, power_mod, simple_hash, sign_message, verify_signature) are the same as before


# Example usage
if __name__ == "__main__":
    # Generate public and private keys with random primes
    public_key, private_key = generate_keys()

    # Display the generated keys
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    # Original message
    message = "Hello, RSA!"

    # Sign the message
    signature = sign_message(message, private_key)
    print(f"Signature: {signature}")

    # Verify the signature
    is_valid = verify_signature(message, signature, public_key)
    print(f"Signature valid: {is_valid}")
