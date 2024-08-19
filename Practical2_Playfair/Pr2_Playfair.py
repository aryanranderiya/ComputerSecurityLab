alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def search_letter(letter: str, list = alphabets) -> bool:
    for index, character in enumerate(alphabets):
        if character == letter:
            del list[index]
            return True
    return False

def create_matrix(plaintext: str):
    matrix = []
    character_list = []
    
    for letter in plaintext:
        letter = letter.strip().lower()

        if letter == "i" or letter == "j":
            letter = "i"  # Treat 'i' and 'j' as the same
        
        if letter == "" or not search_letter(letter):
            continue

        if letter not in character_list: # To ensure a unique character list
            character_list.append(letter)
    
    character_list.extend(alphabets)
    rowcount = 0
    
    for index, character in enumerate(character_list):
        if index % 5 == 0:
            matrix.append([])
            rowcount += int(index != 0) 
        matrix[rowcount].append(character)
    
    print(matrix)
    return matrix

def user_input():
    keystring: str = input("Enter a key string to generate the matrix: ")
    plaintext: str = input("Enter a sentence to encrypt: ")
    return keystring, plaintext

def insert_x_for_repeated_letters(word):
    result = []
    for index, letter in enumerate(word):
        result.append(letter)
        if index < len(word) - 1 and letter == word[index + 1]:
            result.append('x')
    return ''.join(result)

def get_digraphs(plaintext: str) -> list:
    digraphs = []
    digraph = ""
    plaintext = plaintext.replace(" ", "").lower()
    plaintext = insert_x_for_repeated_letters(plaintext)

    if len(plaintext) % 2 != 0:
        plaintext += "x"
        
    for index, letter in enumerate(plaintext):
        digraph += letter            
        if (index + 1) % 2 == 0:
            digraphs.append(digraph)
            digraph = ""
    
    return digraphs

def find_position(matrix, char):
    for row_index, row in enumerate(matrix):
        if char in row:
            return (row_index, row.index(char))
    return None

def encrypt(matrix: list, digraphs: list) -> str:
    encrypted_text = ""
    
    for digraph in digraphs:
        pos1 = find_position(matrix, digraph[0])
        pos2 = find_position(matrix, digraph[1])
        
        if pos1 and pos2:
            row1, col1 = pos1
            row2, col2 = pos2
            
            if row1 == row2:
                # Same row: shift columns to the right
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                # Same column: shift rows downwards
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                # Rectangle: swap columns
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]
    
    return encrypted_text

if __name__ == "__main__":
    keystring, plaintext = user_input()
    matrix: list = create_matrix(keystring)
    digraphs: list = get_digraphs(plaintext)
    encrypted_text = encrypt(matrix, digraphs)
    print("Encrypted text:", encrypted_text)
