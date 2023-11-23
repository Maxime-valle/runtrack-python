
liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
liste_sans_doublons = []

for i in liste:
    
    if i not in liste_sans_doublons:
        liste_sans_doublons.append(i)

print(liste_sans_doublons)