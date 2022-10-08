# Variable initialization
Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Changing_Alphabet = []
Special_Characters = [" ", ".", "!", "?", ",", "\'", "-", "~", ":", ";", "\"", "/", "\\", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "="]
plaintext = ""
keyword = ""
keystream = ""
ciphertext = ""

def intro():
    print("Welcome to the Vigenere Cipher Program. Press D to decrypt or E to encrypt.")
    return input("> ")

def retrieve_plaintext():
    # Global variable retrieval
    global plaintext

    print("What is the plaintext? All capitals only.")
    plaintext = input("> ")

def retrieve_ciphertext():
    # Global variable retrieval and variable initialization
    global ciphertext

    print("What is the ciphertext? All capitals only.")
    ciphertext = input("> ")

def retrieve_keystream(text):
    # Global variable retrieval and variable initialization
    global keyword
    global keystream
    index = 0

    # Retrieves keyword
    print("What is the keyword? All capitals only.")
    keyword = input("> ")

    # Retrieves keystream based upon keyword
    for x in range(0, len(text)):
        keystream = keystream + keyword[index]
        index += 1
        if index == len(keyword):
            index = 0

def check_special_characters(letter):
    # Global variable retrieval and variable initialization
    special_flag = False

    for x in Special_Characters:
        if x == letter:
            special_flag = True

    return special_flag

def alphabet_rearrange(letter):
    # Global variable retrieval and variable initialization
    alphabet_index = 0

    # Retrieve index (letter) to begin transcription of Alphabet to Changing_Alphabet from
    for x in range(0, 26):
        if Alphabet[x] == letter:
            alphabet_index = x - 26

    # Transcription of Alphabet to Changing_Alphabet based upon previously retrieved index
    for x in range(0, 26):
        Changing_Alphabet.append(Alphabet[alphabet_index])
        alphabet_index += 1

def solve_ciphertext(keystream_letter):
    # Global variable retrieval
    global ciphertext

    # Find index based upon keystream letter in Alphabet
    for x in range(0, 26):
        if Alphabet[x] == keystream_letter:
            index = x

    # Appends ciphertext based upon index found previously
    ciphertext = ciphertext + Changing_Alphabet[index]

def solve_plaintext(ciphertext_letter):
    # Global variable retrieval and variable initialization
    global plaintext

    # Find index based upon keystream letter in Alphabet
    for x in range(0, 26):
        if Changing_Alphabet[x] == ciphertext_letter:
            index = x

    # Appends plaintext based upon index found previously
    plaintext = plaintext + Alphabet[index]

def alphabet_erase():
    # Clears Changing_Alphabet for next iteration
    for x in range(0, 26):
        Changing_Alphabet.remove(Changing_Alphabet[0])

def encryption_program():
    retrieve_plaintext()
    retrieve_keystream(plaintext)
    plain_index = 0
    key_index = 0
    global ciphertext
    for index in range(0, len(plaintext)):
        if check_special_characters(plaintext[plain_index]) == True:
            ciphertext = ciphertext + plaintext[plain_index]
            plain_index += 1
        else:
            alphabet_rearrange(plaintext[plain_index])
            solve_ciphertext(keystream[key_index])
            alphabet_erase()
            plain_index += 1
            key_index += 1

    print(f"Your ciphertext is: {ciphertext}")

def decryption_program():
    retrieve_ciphertext()
    retrieve_keystream(ciphertext)
    cipher_index = 0
    key_index = 0
    global plaintext
    for index in range(0, len(ciphertext)):
        if check_special_characters(ciphertext[cipher_index]) == True:
            plaintext = plaintext + ciphertext[cipher_index]
            cipher_index += 1
        else:
            alphabet_rearrange(keystream[key_index])
            solve_plaintext(ciphertext[cipher_index])
            alphabet_erase()
            cipher_index += 1
            key_index += 1

    print(f"Your plaintext is: {plaintext}")

player_choice = intro()
if player_choice == "e" or player_choice == "E":
    encryption_program()
elif player_choice == "d" or player_choice == "D":
    decryption_program()