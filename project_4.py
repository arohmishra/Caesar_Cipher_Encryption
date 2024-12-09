# CAESAR CIPHER ENCRYPTION 

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key)%26
            cipher_text = cipher_text + alphabet[new_position]
        else :
            cipher_text += char
    
    print(f"Here is the encrypted text: {cipher_text}")


def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) %26
            plain_text = plain_text + alphabet[new_position]
        else:
            plain_text += char
    
    print(f"Here is the decrypted text: {plain_text}")


flag = True

while  flag:

    what_to_do = input("Type 'encrypt' for encryption and 'decrypt' for decryption\n")
    message = input("Type your message\n")
    shift = int(input("Enter the shift number: "))

    if what_to_do == 'encrypt':
        encryption(message, shift)
    elif what_to_do == 'decrypt':
        decryption(message, shift)
    else:
        print("Invalid choice!")
    
    flag = input("Do you want to continue? (yes/no)\n").lower()=='yes'

print("Bye! Have a nice day")