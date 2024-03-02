

def mono_alphabetic_substitution(ciphertext, substitution):
    
    resultado = ""
    
    for char in ciphertext: 
        
        if char in substitution: 
            resultado += substitution[char]
        else: 
            resultado += char.upper()

    return resultado 




        
            