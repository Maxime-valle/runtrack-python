nom = "Produit A"
prix_unitaire = 10.0  
quantite_en_stock = 100 


print(f"livre : {nom}")
print(f"Prix unitaire : {prix_unitaire} euros")
print(f"Quantité en stock : {quantite_en_stock}")


quantite_achetee = int(input("Combien de produits souhaitez-vous acheter ? "))
quantite_en_stock -= quantite_achetee


prix_unitaire *= 1.10 # augmentation de 10%


print(f"\nNom du produit : {nom}")
print(f"Prix unitaire : {prix_unitaire} euros")
print(f"Quantité en stock : {quantite_en_stock}")

