#Variable initialization
Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Defines function that returns new alphabet based on shift (key)
def cipher_list(shift):
    if shift < 0:
        cipher_list = [Alphabet[x + shift] for x in range(0, 26)]
    #Sets cipher_list to Alphabet[x - 26 + shift] if shift is positive, because if the end result is over 26 an error occurs. It does not if it is below 0, and still functions properly.
    else:
        cipher_list = [Alphabet[x - 26 + shift] for x in range(0, 26)]
    return cipher_list

#Introduction
print("Welcome to the Caesar Cipher Program! Press D to decrypt or E to encrypt.")
#User choice
choice = input("> ")
if choice == "E" or choice == "e":
    print("What is the shift (key)? Must be a number.")
    #Initializes shift
    shift = int(input("> "))
    #Sets cipher_list to Alphabet[x + shift] if shift is negative
    cipher_list = cipher_list(shift)
    #Initializes plaintext and ciphertext
    print("What is the plaintext? All capitals only.")
    plaintext = input("> ")
    ciphertext = ""
    #Starts a for loop for x in plaintext
    for x in range(0, len(plaintext)):
        if plaintext[x] != " " and plaintext[x] != "!" and plaintext[x] != "?" and plaintext[x] != "." and plaintext[x] != "," and plaintext[x] != "\'":
            #Finds the current letter in plaintext in Alphabet, and adds the corresponding ciphered letter to ciphertext and starts next plaintext letter
            for i in range(0, 26):
               if plaintext[x] == Alphabet[i]:
                   ciphertext = f"{ciphertext}{cipher_list[i]}"
        else:
            ciphertext = f"{ciphertext}{plaintext[x]}"
    print("Your ciphertext is: " + ciphertext)
elif choice == "D" or choice == "d":
    print("What is the shift (key)? Must be a number.")
    shift = int(input("> "))
    cipher_list = cipher_list(shift)
    print("What is the ciphertext? All capitals only.")
    ciphertext = input("> ")
    plaintext = ""
    for x in range(0, len(ciphertext)):
        if ciphertext[x] != " " and ciphertext[x] != "!" and ciphertext[x] != "?" and ciphertext[x] != "." and ciphertext[x] != "," and ciphertext[x] != "\'":
            for i in range(0, 26):
                if ciphertext[x] == cipher_list[i]:
                    plaintext = f"{plaintext}{Alphabet[i]}"
        else:
            plaintext = f"{plaintext}{ciphertext[x]}"
    print("Your plaintext is :" + plaintext)
