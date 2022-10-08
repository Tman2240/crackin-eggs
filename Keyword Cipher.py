# Variable initialization
Alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
Changing_Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Keyword_Alphabet = []
Special_Characters = [" ", ".", "!", "?", ",", "\'", "-", "~", ":", ";", "\"", "/", "\\", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "="]
plaintext = ""
keyword = ""
ciphertext = ""
play_again = True

def intro():
    print("Welcome to the Keyword Cipher Program. Press D to decrypt or E to encrypt.")
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

def retrieve_keyword():
    # Global variable retrieval and variable initialization
    global keyword

    print("What is the keyword? All capitals only.")
    keyword = input("> ")

def check_special_characters(letter):
    # Global variable retrieval and variable initialization
    special_flag = False

    for x in Special_Characters:
        if x == letter:
            special_flag = True

    return special_flag

def alphabet_rearrange(keyword):
    # Begins Changing_Alphabet by retrieving keyword letters from Alphabet
    for letter in keyword:
        for x in range(0, len(Keyword_Alphabet)):
            if Keyword_Alphabet[x] == letter:
                break
        for x in range(0, len(Changing_Alphabet)):
            if Changing_Alphabet[x] == letter:
                Keyword_Alphabet.append(Changing_Alphabet[x])
                Changing_Alphabet.remove(Changing_Alphabet[x])
                break

    # Finishes Keyword_Alphabet by adding the rest of Changing_Alphabet
    for x in range(0, len(Changing_Alphabet)):
        Keyword_Alphabet.append(Changing_Alphabet[0])
        Changing_Alphabet.remove(Changing_Alphabet[0])

def solve_ciphertext(plaintext_letter):
    # Global variable retrieval and variable initialization
    global ciphertext

    # Finds index of plaintext letter in Alphabet
    for x in range(0, 26):
        if Alphabet[x] == plaintext_letter:

            # Appends ciphertext based upon previously found index
            ciphertext = ciphertext + Keyword_Alphabet[x]
            break

def solve_plaintext(ciphertext_letter):
    # Global variable retrieval and variable initialization
    global plaintext

    # Finds index of ciphertext letter in Keyword_Alphabet
    for x in range(0, 26):
        if Keyword_Alphabet[x] == ciphertext_letter:

            # Appends plaintext based upon previously found index
            plaintext = plaintext + Alphabet[x]
            break

def alphabet_reset():
    # Resets Changing_Alphabet and Keyword_Alphabet to initial state for multiple program uses
    for x in range(0, 26):
        Changing_Alphabet.append(Alphabet[x])
        Keyword_Alphabet.remove(Keyword_Alphabet[0])

def encryption_program():
    global ciphertext
    retrieve_plaintext()
    retrieve_keyword()
    alphabet_rearrange(keyword)
    for letter in plaintext:
        if check_special_characters(letter) == True:
            ciphertext = ciphertext + letter
        else:
            solve_ciphertext(letter)
    print(f"Your ciphertext is: {ciphertext}")

def decryption_program():
    global plaintext
    retrieve_ciphertext()
    retrieve_keyword()
    alphabet_rearrange(keyword)
    for letter in ciphertext:
        if check_special_characters(letter) == True:
            plaintext = plaintext + letter
        else:
            solve_plaintext(letter)
    print(f"Your plaintext is: {plaintext}")

while play_again == True:
    player_choice = intro()
    if player_choice == "e" or player_choice == "E":
        encryption_program()
    elif player_choice == "d" or player_choice == "D":
        decryption_program()
    else:
        print("That's not a valid answer! Try again.")
    print("Would you like to use the program again?")
    play_again = input("> ")
    if play_again == "Y" or play_again == "y" or play_again == "Yes" or play_again == "yes":
        play_again = True
        alphabet_reset()
    else:
        play_again = False