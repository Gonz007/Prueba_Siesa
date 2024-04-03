def division_enteros(numero1, numero2):
    if numero2 == 0:
        print("Error: No se puede dividir por cero.")
        return None
    else:
        resultado = numero1 / numero2
        return resultado

num1 = 10
num2 = 2
resultado_division = division_enteros(num1, num2)
print("El resultado de la división es:", resultado_division)
