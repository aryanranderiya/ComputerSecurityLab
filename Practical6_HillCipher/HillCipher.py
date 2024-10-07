# Helper function to find the modular inverse of a number modulo m
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to encrypt a message using Hill Cipher


def hill_encrypt(plaintext, key, n):
    # Converting plaintext to numerical values (A=0, B=1, ..., Z=25)
    text_numbers = [ord(c) - ord('A')
                    for c in plaintext.upper() if c.isalpha()]

    # Padding the text if it's not divisible by n
    while len(text_numbers) % n != 0:
        text_numbers.append(0)  # Padding with A (0)

    # Convert the key into a matrix
    key_matrix = [[key[i * n + j] for j in range(n)] for i in range(n)]

    # Encrypt in n-grams
    encrypted_numbers = []
    for i in range(0, len(text_numbers), n):
        vector = text_numbers[i:i + n]
        encrypted_vector = [0] * n

        # Matrix multiplication (key_matrix * vector)
        for row in range(n):
            for col in range(n):
                encrypted_vector[row] += key_matrix[row][col] * vector[col]
            encrypted_vector[row] %= 26  # Mod 26 for letters

        encrypted_numbers.extend(encrypted_vector)

    # Convert numbers back to letters
    encrypted_text = ''.join(chr(num + ord('A')) for num in encrypted_numbers)
    return encrypted_text

# Function to decrypt the message using Hill Cipher


def hill_decrypt(ciphertext, key, n):
    # Converting ciphertext to numerical values (A=0, B=1, ..., Z=25)
    cipher_numbers = [ord(c) - ord('A')
                      for c in ciphertext.upper() if c.isalpha()]

    # Convert the key into a matrix
    key_matrix = [[key[i * n + j] for j in range(n)] for i in range(n)]

    # Find determinant of the key matrix
    determinant = key_matrix[0][0] * key_matrix[1][1] - \
        key_matrix[0][1] * key_matrix[1][0]
    determinant = determinant % 26

    # Find the modular inverse of the determinant
    det_inv = mod_inverse(determinant, 26)

    if det_inv is None:
        raise ValueError("Key matrix is not invertible")

    # Find the inverse key matrix
    inverse_key_matrix = [[key_matrix[1][1] * det_inv % 26, -key_matrix[0][1] * det_inv % 26],
                          [-key_matrix[1][0] * det_inv % 26, key_matrix[0][0] * det_inv % 26]]

    # Decrypt in n-grams
    decrypted_numbers = []
    for i in range(0, len(cipher_numbers), n):
        vector = cipher_numbers[i:i + n]
        decrypted_vector = [0] * n

        # Matrix multiplication (inverse_key_matrix * vector)
        for row in range(n):
            for col in range(n):
                decrypted_vector[row] += inverse_key_matrix[row][col] * vector[col]
            decrypted_vector[row] %= 26  # Mod 26 for letters

        decrypted_numbers.extend(decrypted_vector)

    # Convert numbers back to letters
    decrypted_text = ''.join(chr(num + ord('A')) for num in decrypted_numbers)
    return decrypted_text

# Function to take user input


def get_input():
    plaintext = input("Enter the plaintext: ").upper().replace(" ", "")
    n = int(input("Enter the size of the n-gram (e.g., 2 for 2x2 matrix): "))

    # Enter key matrix
    key = []
    print(f"Enter the {n}x{
          n} key matrix row by row (e.g., 3 3 for first row):")
    for i in range(n):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        key.extend(row)

    return plaintext, key, n


if __name__ == "__main__":
    # Example usage:
    plaintext, key, n = get_input()

    ciphertext = hill_encrypt(plaintext, key, n)
    print("\nEncrypted:", ciphertext)

    decrypted_text = hill_decrypt(ciphertext, key, n)
    print("Decrypted:", decrypted_text)
