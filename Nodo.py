class Transcion(object):
    def __init__(self, estado, cinta, pila, impar):
        self.estado = estado
        self.cinta = cinta
        self.pila = pila
        self.impar = impar
    def __str__(self):
        return (str(self.estado, self.cinta, self.pila), self.impar)