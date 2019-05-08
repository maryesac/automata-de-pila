class Transicion(object):
    
    def __init__(self, estado, cinta, pila):
        self.estado = estado
        self.cinta = cinta
        self.pila = pila

    def __str__(self):
        return "%s, %s, %s" % (self.estado, self.cinta, self.pila)