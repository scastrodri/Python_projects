import string
import random

# A script that will encrypt the string referenced by the variable plaintext using the caesar 
# cipher with a shift of 13. Store the result in ciphertext.
def cipher(a_str:str, shift:int)-> str:
    '''Encrypt the string referenced using the caesar cipher with a giving shift
    Arguments:
        a_string: a str
        shift: an int
    '''
    letters = string.ascii_lowercase
    ciphertext = ''
    pos = None
    for char in a_str:
        pos = letters.index(char) + shift
        if pos < 26:
            ciphertext += letters[pos]
        else:
            pos = pos - 26
            ciphertext += letters[pos]
    return ciphertext

plaintext = 'thequickbrownfoxjumpsoverthelazydog'
# print(cipher(plaintext,13))


# A script that will encrypt the plaintext using a key
def encrypt(a_str:str, a_key:str)-> str:
    '''Encrypt the string referenced using a key

    Arguments:
        a_string: a str
        a_key: a str that must be 27 long characters
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    ciphertext = ''
    pos = None
    for char in a_str:
        pos = alphabet.index(char)
        ciphertext += a_key[pos]
    return ciphertext

key =      'mwgp bdzxrylacsokjfhtnueivq'
plaintext = 'of shoes and ships and sealing wax of cabbages and kings'
# print(encrypt(plaintext, key))


# A script that will decrypt the ciphertext.
def decrypt(a_str:str, a_key:str) -> str:
    '''Decrypt the string referenced using a key

    Arguments:
        a_string: a str
        a_key: a str that must be 27 long characters
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    plaintext = ''
    pos = None
    for char in a_str:
        pos = a_key.index(char)
        plaintext += alphabet[pos]
    return plaintext

key =      'mwgp bdzxrylacsokjfhtnueivq'
ciphertext = 'hz qftcqumfqfzxcxcdqscqhz qf mqfzxcxcdquxhzqmllqzxfqaxdzh'
# print(decrypt(ciphertext, key))

# A scrypt that asks the user to enter a key (scrambled alphabet) and a message to encrypt or decrypt.
def enc_dec():
    '''Encrypt or decrypt any message with an specific key'''
    answer = ''
    while True:
        choice = input('Do you want to Encrypt or Decrypt your text?[E/D]: ')
        valid_choice = 'EDed'
        if choice not in valid_choice:
            print('Please enter a value input')
        else:
            answer = choice
            break
    
    key = input('Please enter a 27 key len: ')
    plaintext = input('Please enter the message to be encrypted: ')
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    if len(key) > 27:
        print('Your key will be shorted to the first 27 characters')
        key = key[:27]
        print(key)
    else:
        print('Your key will be completed randomly until reach 27 characters')
        remain_letters = ''
        for char in alphabet:
            if char not in key:
                remain_letters += char
        key += ''.join(random.sample(remain_letters,len(remain_letters)))
    if choice == 'E' or choice == 'e':
        answer = encrypt(plaintext, key)
    else:
        answer = decrypt(plaintext, key)
    return answer
print(enc_dec())

# Password to Key
# Finally, only a few truly amazing people are going to remember a random ording of 26 letters. We would 
# like to have a way to use a password of around 7 characters. How can we use a password to scramble our
# alphabet into some order? Its not as bad as you might think at first. Do the following:

# 1- Remove any duplicate letters from the password.
# 2- Now split the alphabet into two halves The letters up to and including the last letter in the 
# password and the rest of the alphabet.
# 3- Remove any letters in your password from the the two halves of the alphabet.
# 4- The key is the concatenation of the password (without duplicate letters) followed by the second 
# part of the split alphabet followed by the first part of the alphabet.

password = 'password'
password = ''.join(dict.fromkeys(password))

alphabet = [string.ascii_lowercase[:13], string.ascii_lowercase[13:]]

alphabet[0] = ''.join([char for char in alphabet[0] if char not in password])
alphabet[1] = ''.join([char for char in alphabet[1] if char not in password])

key = ''.join([password, alphabet[1], alphabet[0]])