def encrypt(plaintext, key):
    # Remove spaces from the plaintext and convert to uppercase
    plaintext = plaintext.replace(' ', '').upper()

    # Determine the number of columns and rows
    num_cols = len(key)
    num_rows = len(plaintext) // num_cols
    if len(plaintext) % num_cols != 0:
        num_rows += 1

    # Create a matrix for the plaintext
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]

    # Fill the matrix with the plaintext
    for i, char in enumerate(plaintext):
        row = i // num_cols
        col = i % num_cols
        matrix[row][col] = char

    # Create a list of columns based on the key order
    col_order = sorted(range(len(key)), key=lambda k: key[k])

    # Read columns in order
    ciphertext = ''
    for col in col_order:
        for row in range(num_rows):
            if matrix[row][col] != '':
                ciphertext += matrix[row][col]

    return ciphertext


def decrypt(ciphertext, key):
    # Determine the number of columns and rows
    num_cols = len(key)
    num_rows = len(ciphertext) // num_cols
    if len(ciphertext) % num_cols != 0:
        num_rows += 1

    # Create a matrix for the ciphertext
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]

    # Create a list of columns based on the key order
    col_order = sorted(range(len(key)), key=lambda k: key[k])

    # Fill the matrix with the ciphertext
    index = 0
    for col in col_order:
        for row in range(num_rows):
            if index < len(ciphertext):
                matrix[row][col] = ciphertext[index]
                index += 1

    # Read the matrix in row-wise order
    plaintext = ''
    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] != '':
                plaintext += matrix[row][col]

    return plaintext


def user_input() -> tuple:
    while True:
        try:
            # Prompt user for the key and convert it to an integer
            keystring: int = input("Enter a key: ")

            # Prompt user for the action ('e' for encrypt or 'd' for decrypt)
            action: str = input(
                "Enter 'e' to encrypt or 'd' to decrypt: ").lower()

            # Check if the action is valid
            if action not in ['e', 'd']:
                raise ValueError(
                    "Action must be 'e' for encryption or 'd' for decryption.")

            # Prompt user for the plaintext or ciphertext
            text: str = input(
                "Enter the text to encrypt or decrypt: ").replace(" ", "")

            return keystring, action, text
        except ValueError as e:
            # Display error message and prompt user to try again if input is invalid
            print(f"Error: {e}")
            print("Please try again.")


def main():
    """Main function to handle user input and perform encryption or decryption."""
    keystring, action, text = user_input()

    if action == 'e':
        ciphertext = encrypt(text, keystring)
        print(f"\nEncrypted text: {ciphertext}")
    elif action == 'd':
        decrypted_text = decrypt(text, keystring)
        print(f"\nDecrypted text: {decrypted_text}")


if __name__ == "__main__":
    main()
