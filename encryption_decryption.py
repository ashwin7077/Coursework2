def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

print('..'*38,"\n\t\t  ECNCRYPTION AND DECRYPTION\n",'..'*38)
choice = input("Enter 'E' for encryption or 'D' for decryption: ")
if choice.upper() not in ['E', 'D']:
    print("Invalid choice. Please enter 'E' or 'D'.")
else:
    text = input("Enter the text: ")
    key = int(input("Enter the key (an integer): "))

if choice.upper() == 'E':
    encrypted_text = encrypt(text, key)
    print("Encrypted text:", encrypted_text)
else:
    decrypted_text = decrypt(text, key)
    print("Decrypted text:", decrypted_text)
