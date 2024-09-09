import random


def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)


def random_shift(key):
    random.seed(sum(ord(char) for char in key))
    shifts = [random.randint(1, 25) for _ in range(len(key))]
    return shifts


def encrypt(message, key):
    key = generate_key(message, key)
    shifts = random_shift(key)
    cipher_text = []

    for i in range(len(message)):
        char = (ord(message[i]) - ord('A') + shifts[i]) % 26
        char += ord('A')
        cipher_text.append(chr(char))

    return ''.join(cipher_text)


def decrypt(cipher_text, key):
    key = generate_key(cipher_text, key)
    shifts = random_shift(key)
    original_text = []

    for i in range(len(cipher_text)):
        char = (ord(cipher_text[i]) - ord('A') - shifts[i]) % 26
        char += ord('A')
        original_text.append(chr(char))

    return ''.join(original_text)


def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()

    if choice == 'E':
        plaintext = input("Enter the plaintext (A-Z only): ").upper()
        key = input("Enter the key (A-Z only): ").upper()
        ciphertext = encrypt(plaintext, key)
        print("Encrypted Message with random shifts:", ciphertext)

    elif choice == 'D':
        ciphertext = input("Enter the ciphertext (A-Z only): ").upper()
        key = input("Enter the key (A-Z only): ").upper()
        plaintext = decrypt(ciphertext, key)
        print("Decrypted Message with random shifts:", plaintext)

    else:
        print("Invalid choice! Please choose either E or D.")


if __name__ == "__main__":
    main()
