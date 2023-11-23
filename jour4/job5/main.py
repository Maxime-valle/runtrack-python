def modifier_liste(L):
    
    L[3] = L[2] + L[4]
    return L


L = [1, 2, 3, 4, 5]

print("La deuxième valeur de la liste est :", L[1])


L = modifier_liste(L)
print("La liste après modification est :", L)


print("La dernière valeur de la liste est :", L[-1])

        
    

