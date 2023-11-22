def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur : Division par zéro"
    else:
        return "Erreur : Opérateur non valide"


print(calcule(10, '+', 5))  
print(calcule(10, '-', 5))  
print(calcule(10, '*', 5))  
print(calcule(10, '/', 5))  
print(calcule(10, '%', 5))  
        
    

