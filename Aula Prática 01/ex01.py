
#Funcao de encriptacao 
def encrypt(key,string):
    encrypt_text = ""
    for char in string: 
        if char.islower(): 
            encrypt_text += chr((ord(char) - 97 + key)%26 + 97)
        elif char.isupper():
            encrypt_text += chr((ord(char) - 65 + key )%26 + 65)
        else: 
            encrypt_text += char 
    return encrypt_text 


def decrypt(key,string):
    encrypt_text = ""
    for char in string: 
        if char.islower(): 
            encrypt_text += chr((ord(char) - 97 - key)%26 + 97)
        elif char.isupper():
            encrypt_text += chr((ord(char) - 65 - key )%26 + 65)
        else: 
            encrypt_text += char
    return encrypt_text 






    