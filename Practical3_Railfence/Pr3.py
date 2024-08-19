def user_input() -> tuple:
    while True:
        try:
            # Prompt user for the key and convert it to an integer
            keystring: int = int(
                input("Enter a numeric key (number of rails): "))
            
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
            
            # Check if the key is a positive integer
            if keystring <= 0:
                raise ValueError("Key must be a positive integer.")

            return keystring, action, text
        except ValueError as e:
            # Display error message and prompt user to try again if input is invalid
            print(f"Error: {e}")
            print("Please try again.")


def encrypt(key: int, text: str) -> str:
    """Encrypt the given text using the Rail Fence Cipher with the specified key."""
    if key == 1:
        # If key is 1, no encryption is needed (only one rail)
        return text

    # Initialize a list of empty strings for each rail
    rails = ['' for _ in range(key)]
    rail = 0  # Start on the first rail
    direction = 1  # Move direction: 1 for down, -1 for up

    # Iterate over each character in the text
    for index, char in enumerate(text):
        # Append character to the current rail
        rails[rail] += char
        # Move to the next rail based on the direction
        rail += direction
        # Reverse direction if reaching the top or bottom rail
        if rail == 0 or rail == key - 1:
            direction *= -1

    # Concatenate all rails to form the encrypted text
    encrypted_text = ''.join(rails)
    return encrypted_text


def decrypt(key: int, text: str) -> str:
    """Decrypt the given text using the Rail Fence Cipher with the specified key."""
    if key == 1:
        return text

    # Initialize the matrix to keep track of rail positions
    rails = [['' for _ in range(len(text))] for _ in range(key)]
    rail = 0
    direction = 1

    # Mark the positions in the matrix
    for i in range(len(text)):
        rails[rail][i] = '*'
        rail += direction
        if rail == 0 or rail == key - 1:
            direction *= -1

    # Fill the matrix with the ciphertext
    index = 0
    for r in range(key):
        for c in range(len(text)):
            if rails[r][c] == '*':
                rails[r][c] = text[index]
                index += 1

    # Read the matrix in zigzag pattern to get the plaintext
    result = []
    rail = 0
    direction = 1
    for i in range(len(text)):
        result.append(rails[rail][i])
        rail += direction
        if rail == 0 or rail == key - 1:
            direction *= -1

    return ''.join(result)


def main():
    """Main function to handle user input and perform encryption or decryption."""
    keystring, action, text = user_input()

    if action == 'e':
        if keystring > len(text):
            print("Key is larger than the length of the text.")
            keystring = len(text)
            ciphertext = text  # No encryption needed if key is too large
        else:
            ciphertext = encrypt(keystring, text)
        print(f"\nEncrypted text: {ciphertext}")
    elif action == 'd':
        if keystring > len(text):
            print("Key is larger than the length of the text.")
            keystring = len(text)
            decrypted_text = text  # No decryption needed if key is too large
        else:
            decrypted_text = decrypt(keystring, text)
        print(f"\nDecrypted text: {decrypted_text}")


if __name__ == "__main__":
    main()
