def convertir_base_con_tabla(x, k):
    tabla = []
    residuos = []
    while x > 0:
        residuo = x % k
        cociente = x // k
        tabla.append((x, k, cociente, residuo))
        residuos.append(residuo)
        x = cociente

    residuos.reverse()

    base_k = ''.join(map(str, residuos))

    return base_k, tabla

def imprimir_tabla(tabla):
    print("Tabla de conversión:")
    print("Base   -   Cociente   -   Residuo")
    for paso in tabla:
        print("{:<5d}:   {:<3d}   -   {:<3d}   -   {:<3d}".format(paso[0], paso[1], paso[2], paso[3]))

x = int(input("Ingrese el número a convertir: "))
k = int(input("Ingrese la base de conversión: "))

base_k, tabla = convertir_base_con_tabla(x, k)

imprimir_tabla(tabla)

print("\nEl número", x, "en base", k, "es:", base_k)
