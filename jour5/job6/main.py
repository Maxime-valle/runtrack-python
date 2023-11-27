def calcul_distance(marches, hauteur_marche):
    
    return 2 * 5 * 7 * marches * hauteur_marche / 100

marches = int(input("Nombre de marches : "))
hauteur_marche = int(input("Hauteur de chaque marche (cm) : "))
print(f"Le gardien parcourt {calcul_distance(marches, hauteur_marche):.2f} m par semaine.")