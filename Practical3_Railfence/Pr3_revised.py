def user_input() -> tuple:
    """Get user input for the action (encrypt/decrypt), key, text, and number of rounds."""
    while True:
        try:
            action = input(
                "Would you like to encrypt or decrypt? (e/d): ").lower()
            if action not in ['e', 'd']:
                raise ValueError(
                    "Please enter 'e' for encryption or 'd' for decryption.")

            keystring: int = int(
                input("Enter a numeric key (number of rails): "))
            text: str = input("Enter the text: ").replace(" ", "")
            rounds: int = int(input("Enter the number of rounds: "))
            if keystring <= 0 or rounds <= 0:
                raise ValueError("Key and rounds must be positive integers.")

            return action, keystring, text, rounds
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")


def encrypt(key: int, text: str) -> str:
    """Encrypt the given text using the Rail Fence Cipher with the specified key."""
    if key == 1:
        return text

    rails = ['' for _ in range(key)]
    rail = 0
    direction = 1

    for index, char in enumerate(text):
        rails[rail] += char
        rail += direction
        if rail == 0 or rail == key - 1:
            direction *= -1

    encrypted_text = ''.join(rails)
    return encrypted_text


def decrypt(key: int, text: str) -> str:
    """Decrypt the given text using the Rail Fence Cipher with the specified key."""
    if key == 1:
        return text

    # Determine the length of each rail
    rail_lengths = [0] * key
    rail = 0
    direction = 1
    for index in range(len(text)):
        rail_lengths[rail] += 1
        rail += direction
        if rail == 0 or rail == key - 1:
            direction *= -1

    # Reconstruct the rails
    rails = []
    index = 0
    for length in rail_lengths:
        rails.append(text[index:index + length])
        index += length

    # Reconstruct the original text
    decrypted_text = ''
    rail = 0
    direction = 1
    for index in range(len(text)):
        decrypted_text += rails[rail][0]
        rails[rail] = rails[rail][1:]
        rail += direction
        if rail == 0 or rail == key - 1:
            direction *= -1

    return decrypted_text


def main():
    action, keystring, text, rounds = user_input()

    if action == 'e':
        result = text
        for _ in range(rounds):
            result = encrypt(keystring, result)
        print(f"\nEncrypted text after {rounds} rounds: {result}")

    elif action == 'd':
        result = text
        for _ in range(rounds):
            result = decrypt(keystring, result)
        print(f"\nDecrypted text after {rounds} rounds: {result}")


if __name__ == "__main__":
    main()
