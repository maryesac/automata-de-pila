from backend.estados import Estados
import time
class Validar:
    def __init__(self, automata):
        self.automata = automata
    def transiciones(self, estado, cinta, pila, impar):
        if not impar % 2 != 0:
            return print("Solo palindromos impares")

        if estado == "p":
            estado, cinta, pila = Estados(estado, cinta, pila, self.automata).transiciones_p()
            
            return self.transiciones(estado, cinta, pila, impar)

        if estado == "q":
            
            estado, cinta, pila = Estados(estado, cinta, pila, self.automata).transiciones_q()
            
            return self.transiciones(estado, cinta, pila, impar)

        if estado == "r":
            self.automata.activarEstado("r")
            self.automata.lienzo.update()
            time.sleep(1)
            self.automata.desactivarEstado("r")
            self.automata.lienzo.update()
            print("Palabra aceptada")
            return True



if __name__ == "__main__":
    estado = "p"
    cinta = "aaaaaabbcbbaaaaaa"
    pila = "#"
    impar = len(cinta)

    print(estado, cinta, pila)


    transiciones(estado, cinta, pila, impar)
