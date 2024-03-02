

#Function that performs frequency attacks on a mono-alphabetic substitution ciphers

def frequency_attacks(ciphertext): 
    resultado = {} #Criar um dicionario 
    n_letras = 0

    for char in ciphertext: 
        if char.isalpha():
            n_letras += 1
            if char in resultado:
                resultado[char] += 1
            else: 
                resultado[char] = 1 
    
    incidence_percentage = [(letter,count/n_letras*100) for letter,count in resultado.items()]
    
    incidence_percentage.sort(key = lambda pair: pair[1], reverse = True)


    return incidence_percentage
        
               
     