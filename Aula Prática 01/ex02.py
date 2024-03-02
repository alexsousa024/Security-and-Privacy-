def decryption(ciphertext, keyword = None):
    for i in range(26):
        texto_final = ""
        for char in ciphertext:
            if char.islower():
                texto_final += chr((ord(char) - 97 - i) % 26 + 97)
            elif char.isupper():
                texto_final += chr((ord(char) - 65 - i) % 26 + 65)
            else:
                texto_final += char  # Deixa caracteres não-alfabéticos inalterados.
        if keyword is None or keyword in texto_final:
            print(f"Key: {i} Texto Final: {texto_final}")

            



        

            
