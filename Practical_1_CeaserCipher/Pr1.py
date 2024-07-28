
alphabets=[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
  'm', 'n', 'o', 'p', 'q', 'r',  's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]


def user_input(is_encrypt: bool = True) -> tuple:
    while True:
        try:
            string = input(f"Enter a string to {'encrypt' if is_encrypt else 'decrypt' }: ").lower()
            key = int(input("Enter a number for the key: "))
            return string, key
        except ValueError:
            print("Invalid input! Please enter a valid integer for the key.")
        

def search_letter(character: str) -> None | int:
    for index, letter in enumerate(alphabets):
        if letter == character:
            return index
    return None

def convert(is_encrypt = True) -> str:
    string, key = user_input(is_encrypt=is_encrypt)
    text = ""
    
    for letter in string:
        if letter == " ":
            text += " "
            continue
        
        index = search_letter(letter)
        
        if index is None: 
            raise ValueError(f"Invalid input! {letter} is not a letter!")
            
        index = (index + key) if is_encrypt else (index - key)
        
        cipher_letter:str = alphabets[index % 26]
        text = text + cipher_letter
        
    return text

            
if __name__ == "__main__":
    try:
        cipher = convert(is_encrypt=True)
        print(f"Ciphertext: {cipher}")
        
        plaintext = convert(is_encrypt=False)
        print(f"Plaintext: {plaintext}")
    except ValueError as e:
        print(e)