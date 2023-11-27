def affiche_tapis(n):
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                print("\\", end="#")
            else:
                print(" ", end="#")
        print()


taille = int(input("Veuillez entrer la taille du tapis : "))
affiche_tapis(taille)

            
             
