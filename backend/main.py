from estados import Estados

estado = "p"
cinta = "aaaaaabbcbbaaaaaa"
pila = "#"
impar = len(cinta)

print(estado, cinta, pila)
def transiciones(estado, cinta, pila, impar):
    if not impar % 2 != 0:
        return print("Solo palindromos impares")

    if estado == "p":
        estado, cinta, pila = Estados(estado, cinta, pila).transiciones_p()
        return transiciones(estado, cinta, pila, impar)

    if estado == "q":
        estado, cinta, pila = Estados(estado, cinta, pila).transiciones_q()
        return transiciones(estado, cinta, pila, impar)

    if estado == "r":
        return print("Palabra aceptada")


transiciones(estado, cinta, pila, impar)
