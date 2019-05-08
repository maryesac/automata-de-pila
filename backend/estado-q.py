from Transicion import Nodo

class EstadoQ(Transicion):
    def __init__(self, estado, cinta, pila, impar):
        Transicion.__init__(self, estado, cinta, pila, impar)