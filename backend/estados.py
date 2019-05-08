from backend.transicion import Transicion
import sys
import time


class Estados(Transicion):

    def __init__(self, estado, cinta, pila,automata):

        Transicion.__init__(self, estado, cinta, pila)
        self.automata = automata

    def transiciones_p(self):
        estado = self.estado
        cinta = self.cinta
        pila = self.pila

        temp2 = len(pila) - 1
        aux = cinta[0]
        auxc = pila[temp2]

        self.automata.activarEstado("p")
        self.automata.lienzo.update()

        if estado == "q":
            return (estado, cinta, pila)

        if aux == "a":
            if auxc == "a":
                pila = pila[:-1]
                cinta = cinta[1:]
                pila = pila + "aa"
                self.list.insert(END,"a,a/aa")
                time.sleep(1)
                self.automata.activarTransicion("a,a/aa")
                time.sleep(1)
                self.automata.desactivarTransicion("a,a/aa")
            if auxc == "b":
                pila = pila[:-1]
                cinta = cinta[1:]
                pila = pila + "ba"
                self.list.insert(END,"a,b/ba")
                time.sleep(1)
                self.automata.activarTransicion("a,b/ba")
                time.sleep(1)
                self.automata.desactivarTransicion("a,b/ba")
            if auxc == "#":
                pila = pila[:-1]
                cinta = cinta[1:]
                pila = "#a"
                self.list.insert(END,"a,#/#a")
                time.sleep(1)
                self.automata.activarTransicion("a,#/#a")
                time.sleep(1)
                self.automata.desactivarTransicion("a,#/#a")
            print(estado, cinta, pila)
            return Estados(estado, cinta, pila, self.automata).transiciones_p()

        if aux == "b":
            if auxc == "a":
                pila = pila[:-1]
                cinta = cinta[1:]
                pila = pila + "ab"
                self.list.insert(END,"b,a/ab")
                time.sleep(1)
                self.automata.activarTransicion("b,a/ab")
                time.sleep(1)
                self.automata.desactivarTransicion("b,a/ab")
            if auxc == "b":
                pila = pila[:-1]
                cinta = cinta[1:]
                pila = pila + "bb"
                self.list.insert(END,"b,b/bb")
                time.sleep(1)
                self.automata.activarTransicion("b,b/bb")
                time.sleep(1)
                self.automata.desactivarTransicion("b,b/bb")
            if auxc == "#":
                pila = pila[:-1]
                cinta = cinta[1:]
                pila = "#b"
                self.list.insert(END,"b,#/#")
                time.sleep(1)
                self.automata.activarTransicion("b,#/#b")
                time.sleep(1)
                self.automata.desactivarTransicion("b,#/#b")
            print(estado, cinta, pila)
            return Estados(estado, cinta, pila, self.automata).transiciones_p()

        if aux == "c":
            if auxc == "a":
                cinta = cinta[1:]
                pila = pila[:-1] + "a"
                self.list.insert(END,"c,a/a")
                time.sleep(1)
                self.automata.activarTransicion("c,a/a")
                time.sleep(1)
                self.automata.desactivarTransicion("c,a/a")
            if auxc == "b":
                cinta = cinta[1:]
                pila = pila[:-1] + "b"
                self.list.insert(END,"c,b/b")
                time.sleep(1)
                self.automata.activarTransicion("c,b/b")
                time.sleep(1)
                self.automata.desactivarTransicion("c,b/b")
            if auxc == "#":
                cinta = cinta[1:]
                pila = pila[:-1] + "#"
                self.list.insert(END,"c,#/#")
                self.automata.activarTransicion("c,#/#")
                time.sleep(1)
                self.automata.desactivarTransicion("c,#/#")
            estado = "q"
            print(estado, cinta, pila)
            return Estados(estado, cinta, pila, self.automata).transiciones_p()
        

    def transiciones_q(self):
        self.automata.desactivarEstado("p")
        self.automata.lienzo.update()
        self.automata.activarEstado("q")
        self.automata.lienzo.update()
        estado = self.estado
        cinta = self.cinta
        pila = self.pila

        if estado == "r":

            self.automata.desactivarEstado("q")
            self.automata.lienzo.update()
            self.automata.activarEstado("r")
            self.automata.lienzo.update()
            time.sleep(1)
            return (estado, cinta, pila)

        if pila == "#":
            pila = pila[:-1]
            estado = "r"
            print(estado, cinta, pila)
            self.list.insert(END,"*,#/#")
            self.automata.activarTransicion("*,#/#")
            time.sleep(1)
            self.automata.desactivarTransicion("*,#/#")
            return Estados(estado, cinta, pila, self.automata).transiciones_q()

        temp2 = len(pila) - 1

        aux = cinta[0]
        auxc = pila[temp2]

        if aux == "b":
            if auxc == "b":
                cinta = cinta[1:]
                pila = pila[:-1]
                self.list.insert(END,"b,b/*")
                time.sleep(1)
                self.automata.activarTransicion("b,b/*")
                time.sleep(1)
                self.automata.desactivarTransicion("b,b/*")

            return Estados(estado, cinta, pila, self.automata).transiciones_q()
        if aux == "a":
            if auxc == "a":
                cinta = cinta[1:]
                pila = pila[:-1]
                self.list.insert(END,"a,a/*")
                time.sleep(1)
                self.automata.activarTransicion("a,a/*")
                time.sleep(1)
                self.automata.desactivarTransicion("a,a/*")
            return Estados(estado, cinta, pila, self.automata).transiciones_q()

        #if aux == auxc:
         #   cinta = cinta[1:]
          #  pila = pila[:-1]
           # print(estado, cinta, pila)
            #return Estados(estado, cinta, pila, self.automata).transiciones_q()
        #else:
         #   print("Palabra no aceptada")
          #  sys.exit()