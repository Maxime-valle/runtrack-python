def tri_bulles(liste):
    n = 0
    for _ in liste:
        n += 1

    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1] :
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

print(tri_bulles([34, 12, 8, 5, 33, 65, 3, 20]))