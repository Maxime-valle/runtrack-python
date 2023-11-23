nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

for i in range(len(nombres)):
    if nombres[i] - int(nombres[i]) < 0.5:
        nombres[i] = int(nombres[i])
    else:
        nombres[i] = int(nombres[i]) + 1

for i in range(len(nombres)):
    for j in range(i + 1, len(nombres)):
        if nombres[i] > nombres[j]:
            nombres[i], nombres[j] = nombres[j], nombres[i]

print(nombres)