#!/usr/bin/env python3
"""
Assignment 1
CSSE1001/7030
Semester 2, 2018
"""

from a1_support import is_word_english

__author__ = "Sannidhi Bosamia - 45101618"

def encrypt(text, offset):
    """Encrypts text inputted by user with some fixed number of positions (offset) down the alphabet.

    Parameters:
        text (str): The text inputted by the user.
        offset (int): The offset entered by the user.

    Return:
        str: The encrypted text using the offset given by the user (case sensitive).
    """
    encrypted_text = ""
    for char in text:
        if ord(char) <= 64:
            encrypted_character = chr(ord(char))
        elif ord(char) < 90:
            encrypted_character = ord(char) + offset
            if encrypted_character > 90:
                encrypted_character -= 26
            encrypted_character = chr(encrypted_character)
        else:
            encrypted_character = ord(char) + offset
            if encrypted_character > 122:
                encrypted_character -= 26
            encrypted_character = chr(encrypted_character)
        encrypted_text += encrypted_character

    return encrypted_text

def decrypt(text, offset):
    """Decrypts text inputted by user with some fixed number of positions (offset) down the alphabet.

    Parameters:
        text (str): The text inputted by the user.
        offset (int): The offset entered by the user.

    Return:
        str: The decrypted text using the offset given by the user (case sensitive).
    """
    decrypted_text = ""
    for char in text:
        if ord(char) <= 64:
            decrypted_character = chr(ord(char))
        elif ord(char) <= 90:
            decrypted_character = ord(char) - offset
            if decrypted_character < 65:
                decrypted_character += 26
            decrypted_character = chr(decrypted_character)
        else:
            decrypted_character = ord(char) - offset
            if decrypted_character < 97:
                decrypted_character += 26
            decrypted_character = chr(decrypted_character)
        decrypted_text += decrypted_character

    return decrypted_text   

def find_encryption_offsets(encrypted_text):
    """Returns a tuple containing all possible offsets that could have been used if to encrypt some English text into encrypted_text.

    Parameters:
        encrypted_text (str): The encrypted text the user wishes to decrypt.

    Return:
        tuple: Possible offset(s) of the given encrypted text, if any, otherwise an empty tuple is returned.
    """
    encrypted_text = encrypted_text.lower()
    possible_offset = ()
    has_apostrophe = bool
    
    for offset in range(1, 26):
        decrypted_text = decrypt(encrypted_text, offset)
        for char in decrypted_text:
            if ord(char) < 64 and char not in ("-", " ", range(48,58)):
                decrypted_text = decrypted_text.replace(char, "")
            if char == "-":
                decrypted_text = decrypted_text.replace(char, " ")
            if char == "'":
                has_apostrophe = True
        decrypted_words = decrypted_text.split(" ")
        for i in range(0, len(decrypted_words)):
            if is_word_english(decrypted_words[i]) == True:
                possible_offset += (offset, )


    if len(possible_offset) > 0 and len(decrypted_words) > 1:
        actual_offset = max(possible_offset, key = possible_offset.count)
        if has_apostrophe == True:
            possible_offset = (actual_offset, )
        elif len(decrypted_words) > 1:
            if possible_offset.count(actual_offset) == len(decrypted_words):
                possible_offset = (actual_offset, )
            else:
                possible_offset = ()

    return possible_offset

def print_possible_offset(possible_offset):
    """Prints the encryption offsets based off the 'find_encryption_offset' function.

    Parameters:
        possible_offset (tuple): The tuple of possible offset(s) for the encrypted text from the find_encryption_offset function.

    Return:
        str: Prints the possible offset(s) of the encrypted message.
        bool: True is sent to the 'main' function if there is a single possible offset, where the encrypted message is decrypted.
    """
    offset_string = ''

    for i in range(0, len(possible_offset)):
        offset_string += str(possible_offset[i])
        if possible_offset[i] != possible_offset[-1]:
            offset_string += ', '
            
    if len(possible_offset) == 0:
        print("No valid encryption offset")
    elif len(possible_offset) > 1:
        print("Multiple encryption offsets:", offset_string)
    else:
        print("Encryption offset:", offset_string)
        decrypt_message = True
        return decrypt_message

def print_encrypt_or_decrypt(option, offset, text):
    """Prints the encrypted or decrypted text based on whether the user selected the encrypt or decrypt option.

    Parameters:
        option (str): The option the user entered, from main()
        offset (int): The offset the user entered, from main()
        text (str): The text the user wanted to encrypt or decrypt, from main()
    """
    if option == "e":
        encrypt_or_decrypt = "encrypted "
        function = encrypt
    else:
        encrypt_or_decrypt = "decrypted "
        function = decrypt
        
    if offset == 0:
        print("The " + encrypt_or_decrypt + "text is:")
        for offset in range(1, 26):
            print("  " + format(offset, '02') + ": " + function(text, offset))
    else:
        print("The " + encrypt_or_decrypt + "text is: " + function(text, offset))

def main():
    """Handles the top-level interactions with the user.

    The user is prompted to choose between Encrypt (e), Decrypt(d), Automatically decrypt English text (a), and Quit (q). 
    """
    print("Welcome to the simple encryption tool!")

    while True:
        print("\nPlease choose an option [e/d/a/q]:\n"
              "  e) Encrypt some text\n"
              "  d) Decrypt some text\n"
              "  a) Automatically decrypt English text\n"
              "  q) Quit")
    
        option = str(input("> "))

        if option == "e":
            text = input("Please enter some text to encrypt: ")
            offset = int(input("Please enter a shift offset (1-25): "))
            print_encrypt_or_decrypt(option, offset, text)
            
        elif option == "d":
            text = input("Please enter some text to decrypt: ")
            offset = int(input("Please enter a shift offset (1-25): "))
            print_encrypt_or_decrypt(option, offset, text)
            
        elif option == "a":
            encrypted_text = input("Please enter some encrypted text: ")
            possible_offset = find_encryption_offsets(encrypted_text)
            decrypt_message = print_possible_offset(possible_offset)
            if decrypt_message == True:
                print("Decrypted message:", decrypt(encrypted_text, possible_offset[0]))
            
        elif option == "q":
            print("Bye!")
            break

        else:
            print("Invalid command")
    


##################################################
# !! Do not change (or add to) the code below !! #
#
# This code will run the main function if you use
# Run -> Run Module  (F5)
# Because of this, a "stub" definition has been
# supplied for main above so that you won't get añ
# NameError when you are writing and testing your
# other functions. When you are ready please
# change the definition of main above.
###################################################

if __name__ == '__main__':
    main()

