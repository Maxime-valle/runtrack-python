hauteur = int(input("Veuillez entrer la hauteur du triangle : "))

for i in range(hauteur):
    print(' ' * (hauteur - i - 1) + '/' + ' ' * (2 * i) + '\\' + ' ' * (hauteur - i - 1))
print('-' * (2 * hauteur))
