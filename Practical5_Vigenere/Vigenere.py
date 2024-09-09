def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)


def encrypt(message, key):
    cipher_text = []
    for i in range(len(message)):
        char = (ord(message[i]) + ord(key[i])) % 26
        char += ord('A')
        cipher_text.append(chr(char))
    return ''.join(cipher_text)


def decrypt(cipher_text, key):
    original_text = []
    for i in range(len(cipher_text)):
        char = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        char += ord('A')
        original_text.append(chr(char))
    return ''.join(original_text)


def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()

    if choice == 'E':
        plaintext = input("Enter the plaintext (A-Z only): ").upper()
        key = input("Enter the key (A-Z only): ").upper()
        key = generate_key(plaintext, key)
        ciphertext = encrypt(plaintext, key)
        print("Encrypted Message:", ciphertext)

    elif choice == 'D':
        ciphertext = input("Enter the ciphertext (A-Z only): ").upper()
        key = input("Enter the key (A-Z only): ").upper()
        key = generate_key(ciphertext, key)
        plaintext = decrypt(ciphertext, key)
        print("Decrypted Message:", plaintext)

    else:
        print("Invalid choice! Please choose either E or D.")


if __name__ == "__main__":
    main()
