def verifier_nombre(nombre):
    if nombre >0:
     return "positif"
    elif nombre < 0:
        return"negatif"
    
resultat = verifier_nombre(-3)
print(resultat)
resultat = verifier_nombre(7)
print(resultat)
    