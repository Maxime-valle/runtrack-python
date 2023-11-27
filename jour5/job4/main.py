def affiche_tapis(n):
    for i in range(n+1):
        ligne = "|"
        for j in range(n+1):
            if j == n  - i:
                ligne += " "
               
            else:
                ligne += "#"
        ligne += "|"
                
        print(ligne)

taille = int(input("Veuillez entrer la taille du tapis : "))
affiche_tapis(taille)
   