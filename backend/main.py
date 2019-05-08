estado = "p"
cinta = "abbacabb"
pila = "#"
impar = len(cinta)

print(estado, cinta, pila)
def transiciones(estado, cinta, pila, impar):
    if not impar % 2 != 0:
        return print("Solo palindromos impares")

    temp2 = len(pila) - 1
    if estado == "p":
        aux = cinta[0]
        auxc = pila[temp2]

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
            print( estado, cinta, pila)
            return transiciones(estado, cinta, pila, impar)

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
            print (estado, cinta, pila)
            return transiciones(estado, cinta, pila, impar)

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
            print (estado, cinta, pila)
            return transiciones(estado, cinta, pila, impar)

    if estado == "q":
        if not cinta:
            pila = pila[:-1]
            estado = "r"
            print (estado, cinta, pila)
            return transiciones(estado, cinta, pila, impar)
        aux = cinta[0]
        auxc = pila[temp2]
        if aux == auxc:
            cinta = cinta[1:]
            pila = pila[:-1]
            print (estado, cinta, pila)
            return transiciones(estado, cinta, pila, impar)

    if estado == "r":
        return print("Palabra aceptada")
    else:
        return print("Palabra no aceptada")


transiciones(estado, cinta, pila, impar)
