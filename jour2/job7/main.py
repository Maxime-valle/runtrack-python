chaine = "abcdefghijklmnopqrstuvwxyz" * 10
index = 0
ligne = 1

while index < len(chaine):
    print(chaine[index:index+ligne])
    index += ligne
    ligne += 1
    
