#Python project: Vigenere cipher coder/decoder - method of encrypting alphabetic text
mode = input("Do you wish to 'code' or 'decode'? ")
text = input("Enter text: ") #'mrttaqrhknsw ih puggrur'
key = input("Enter key for coding: ") #'happycoding'


def vigenere(message, key, direction = 1):
    keyIndex = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    codedMessage = ''

    for char in message.lower():

        if not char.isalpha():
            codedMessage += char
        else:
            key_char = key[keyIndex % len(key)]
            keyIndex += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            
            new_index = (index + offset * direction) % len(alphabet)
            codedMessage += alphabet[new_index]
    return codedMessage


def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)


if mode == "code" or mode == "Code":
    encryption = encrypt(text,key)
    print(f'\nEncrypted text: {encryption}\n')
elif mode == "decode" or mode == "Decode":
    decryption = decrypt(text, key)
    print(f'\nDecrypted text: {decryption}\n')
else:
    print("\nMode not set! Choose: 'Code' or 'Decode'")