class Nodo:
    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self, raiz):
        self.raiz = raiz

    def calcular_peso_total(self, nodo):
        if nodo is None:
            return 0
        return nodo.peso + self.calcular_peso_total(nodo.izquierda) + self.calcular_peso_total(nodo.derecha)

    def calcular_altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self.calcular_altura(nodo.izquierda), self.calcular_altura(nodo.derecha))

    def obtener_peso_promedio(self):
        peso_total = self.calcular_peso_total(self.raiz)
        cantidad_nodos = self.contar_nodos(self.raiz)
        if cantidad_nodos == 0:
            return 0
        return peso_total / cantidad_nodos

    def contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.contar_nodos(nodo.izquierda) + self.contar_nodos(nodo.derecha)

nodo1 = Nodo(1, 10)
nodo2 = Nodo(2, 20)
nodo3 = Nodo(3, 30)
nodo4 = Nodo(4, 40)
nodo5 = Nodo(5, 50)

arbol1 = Arbol(nodo1)
arbol2 = Arbol(nodo2)
arbol3 = Arbol(nodo3)

nodo1.izquierda = nodo2
nodo1.derecha = nodo3
nodo2.izquierda = nodo4
nodo2.derecha = nodo5

print("Tabla de árboles:")
print("Árbol\tPeso Total\tPeso Promedio\tAltura")
for i, arbol in enumerate([arbol1, arbol2, arbol3], 1):
    peso_total = arbol.calcular_peso_total(arbol.raiz)
    peso_promedio = arbol.obtener_peso_promedio()
    altura = arbol.calcular_altura(arbol.raiz)
    print(f"{i}\t{peso_total}\t\t{peso_promedio:.2f}\t\t{altura}")
