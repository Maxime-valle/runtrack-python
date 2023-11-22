def verifier_nombre(n):
    if isinstance(n, int) and n >= 0:
        if n % 2 == 0:
            print(n, "est un nombre pair.")
        else:
            print(n, "est un nombre impair.")

print("Erreur : Veuillez entrer un nombre entier positif.")


verifier_nombre(10)  
verifier_nombre(15)  
verifier_nombre(45)
verifier_nombre(12)
verifier_nombre(-5)
verifier_nombre(-10)
verifier_nombre(-25)