L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
product = 1

for num in [n for n in L if 25 <= n <= 90]:
    product *= num

print(product)
