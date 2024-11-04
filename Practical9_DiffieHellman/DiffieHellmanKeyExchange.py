import random


def generate_keys(p, g):
    # Generate private keys
    private_key = random.randint(1, p - 1)
    # Calculate public key
    public_key = pow(g, private_key, p)  # base, exponent, mod  | b^e mod m  
    return private_key, public_key


def calculate_shared_secret(public_key, private_key, p):
    # g^a mod p
    return pow(public_key, private_key, p)


def main():
    # Publicly shared
    p = 23  # prime number
    g = 5   # primitive root modulo p

    private_key_a, public_key_a = generate_keys(p, g)
    private_key_b, public_key_b = generate_keys(p, g)

    # Calculate shared secrets
    shared_secret_a = calculate_shared_secret(public_key_b, private_key_a, p)
    shared_secret_b = calculate_shared_secret(public_key_a, private_key_b, p)

    # Output keys and shared secrets
    print("Person A private key:", private_key_a)
    print("Person B private key:", private_key_b)
    print("Person A public key:", public_key_a)
    print("Person B public key:", public_key_b)
    print("Shared secret key (Person A calculation):", shared_secret_a)
    print("Shared secret key (Person B calculation):", shared_secret_b)

    # Check if the shared secret keys match
    if shared_secret_a == shared_secret_b:
        print("Shared secret key successfully exchanged:", shared_secret_a)
    else:
        print("Error: Shared secrets do not match!")


# Run the main function
if __name__ == "__main__":
    main()
