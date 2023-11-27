def chiffrement_cesar(message, decalage):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_chiffre = ''

    for lettre in message:
        if lettre in alphabet:
            
            index = (alphabet.index(lettre) + decalage) % len(alphabet)
            message_chiffre += alphabet[index]
        else:
            message_chiffre += lettre

    return message_chiffre


message = input("Veuillez entrer le message à chiffrer : ")
decalage = int(input("Veuillez entrer le décalage : "))
print(chiffrement_cesar(message, decalage))
    
