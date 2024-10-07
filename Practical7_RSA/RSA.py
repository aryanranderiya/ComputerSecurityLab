import random


def gcd(a, b):
    """Calculate the greatest common divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    """Find the modular inverse of a under modulo m."""
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime_candidate(length):
    """Generate a random prime candidate of given bit length."""
    p = random.getrandbits(length)
    # Ensure p is odd and has the correct length
    return p | (1 << (length - 1)) | 1


def generate_prime_number(length):
    """Generate a prime number of specified bit length."""
    p = 4
    while not is_prime(p):
        p = generate_prime_candidate(length)
    return p


def generate_keypair(bits):
    """Generate RSA keypair of given bit length."""
    p = generate_prime_number(bits)
    q = generate_prime_number(bits)

    while p == q:  # Ensure p and q are different
        q = generate_prime_number(bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e
    e = 65537  # Common choice for e
    if gcd(e, phi) != 1:
        raise ValueError("e and phi(n) are not coprime.")

    # Calculate d
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))  # Public and private key pairs


def encrypt(public_key, plaintext):
    """Encrypt plaintext using RSA public key."""
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher


def decrypt(private_key, ciphertext):
    """Decrypt ciphertext using RSA private key."""
    d, n = private_key
    plaintext = ''.join(chr(pow(char, d, n)) for char in ciphertext)
    return plaintext


# Example usage:
if __name__ == "__main__":
    # Take user input for bit length
    bits = int(
        input("Enter the bit length for generating the keypair (e.g., 8, 16, 32): "))
    public_key, private_key = generate_keypair(bits)

    # Display generated keys
    print("\nPublic Key (e, n):", public_key)
    print("Private Key (d, n):", private_key)

    # Take user input for the message to encrypt
    message = input("\nEnter the message to encrypt: ")
    print("\nOriginal Message:", message)

    # Encrypt the message
    encrypted_msg = encrypt(public_key, message)
    print("Encrypted Message:", encrypted_msg)

    # Decrypt the message
    decrypted_msg = decrypt(private_key, encrypted_msg)
    print("Decrypted Message:", decrypted_msg)
