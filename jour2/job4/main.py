try:
    N = int(input(" nombre entier positif : "))
    if N <= 0:
        print("  un nombre entier supérieur à zéro.")
    else:
        for i in range(1, N+1):
            for j in range(1, 11):
                print(f"{i} * {j} = {i*j}")
            print("-" * 20)
except ValueError:
    print(" Veuillez entrer un nombre entier.")
   