from transicion import Transicion
import sys


class Estados(Transicion):

    def __init__(self, estado, cinta, pila):

        Transicion.__init__(self, estado, cinta, pila)

    def transiciones_p(self):
        estado = self.estado
        cinta = self.cinta
        pila = self.pila

        temp2 = len(pila) - 1
        aux = cinta[0]
        auxc = pila[temp2]

        if estado == "q":
            return (estado, cinta, pila)

        if aux == "a":
            if auxc == "a":
                pila = pila[:-1]
                cinta = cinta[1:]
                pila = pila + "aa"
            if auxc == "b":
                pila = pila[:-1]
                cinta = cinta[1:]
                pila = pila + "ba"
            if auxc == "#":
                pila = pila[:-1]
                cinta = cinta[1:]
                pila = "#a"
            print(estado, cinta, pila)
            return Estados(estado, cinta, pila).transiciones_p()

        if aux == "b":
            if auxc == "a":
                pila = pila[:-1]
                cinta = cinta[1:]
                pila = pila + "ab"
            if auxc == "b":
                pila = pila[:-1]
                cinta = cinta[1:]
                pila = pila + "bb"
            if auxc == "#":
                pila = pila[:-1]
                cinta = cinta[1:]
                pila = "#b"
            print(estado, cinta, pila)
            return Estados(estado, cinta, pila).transiciones_p()

        if aux == "c":
            if auxc == "a":
                cinta = cinta[1:]
                pila = pila[:-1] + "a"
            if auxc == "b":
                cinta = cinta[1:]
                pila = pila[:-1] + "b"
            if auxc == "#":
                cinta = cinta[1:]
                pila = pila[:-1] + "#"
            estado = "q"
            print(estado, cinta, pila)
            return Estados(estado, cinta, pila).transiciones_p()

    def transiciones_q(self):
        estado = self.estado
        cinta = self.cinta
        pila = self.pila

        if estado == "r":
            return (estado, cinta, pila)

        if pila == "#":
            pila = pila[:-1]
            estado = "r"
            print(estado, cinta, pila)
            return Estados(estado, cinta, pila).transiciones_q()

        temp2 = len(pila) - 1

        aux = cinta[0]
        auxc = pila[temp2]

        if aux == auxc:
            cinta = cinta[1:]
            pila = pila[:-1]
            print(estado, cinta, pila)
            return Estados(estado, cinta, pila).transiciones_q()
        else:
            print("Palabra no aceptada")
            sys.exit()