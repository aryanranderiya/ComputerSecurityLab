
alphabets=[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
  'm', 'n', 'o', 'p', 'q', 'r',  's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]


def user_input(is_encrypt: bool = True) -> tuple:
    while True:
        try:
            string = input(f"Enter a string to {'encrypt' if is_encrypt else 'decrypt' }: ").lower()
            key1 = int(input("Enter a number for the key 1: "))
            key2 = int(input("Enter a number for the key 2: "))
            return string, key1, key2
        except ValueError:
            print("Invalid input! Please enter a valid integer for the key.")
        

def search_letter(character: str) -> None | int:
    for index, letter in enumerate(alphabets):
        if letter == character:
            return index
    return None

def convert(is_encrypt = True) -> str:
    string, key1, key2 = user_input(is_encrypt=is_encrypt)
    text = ""
    
    for position, letter in enumerate(string):
        if letter == " ":
            text += " "
            continue
        
        index = search_letter(letter)
        
        if index is None: 
            raise ValueError(f"Invalid input! {letter} is not a letter!")
        
        if position % 2 == 0:
            index = (index + key1) if is_encrypt else (index - key1)
        else:
            index = (index + key2) if is_encrypt else (index - key2)
        
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