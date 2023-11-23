liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
liste_sans_doublons = [i for n, i in enumerate(liste) if i not in liste[:n]]
print(liste_sans_doublons)