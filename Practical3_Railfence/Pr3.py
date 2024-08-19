def user_input() -> tuple:
    while True:
        try:
            # Prompt user for the key and convert it to an integer
            keystring: int = int(
                input("Enter a numeric key (number of rails): "))
            # Prompt user for the plaintext and remove spaces
            plaintext: str = input(
                "Enter a sentence to encrypt: ").replace(" ", "")
            # Check if the key is a positive integer
            if keystring <= 0:
                raise ValueError("Key must be a positive integer.")
            return keystring, plaintext
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


def main():
    """Main function to handle user input and perform encryption."""
    keystring, plaintext = user_input()

    # Check if the key is larger than the length of the plaintext
    if keystring > len(plaintext):
        print("Key is larger than the length of the plaintext.")
        keystring = len(plaintext)  # Adjust key to the length of the plaintext
        ciphertext = plaintext  # No encryption needed if key is too large
    else:
        # Encrypt the plaintext using the Rail Fence Cipher
        ciphertext = encrypt(keystring, plaintext)

    # Display the encrypted text
    print(f"\nEncrypted text: {ciphertext}")


if __name__ == "__main__":
    main()
