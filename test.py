estado = "p"
cinta = "abbcbba"
pila = "#"
temp = len(cinta)

print (estado, cinta, pila)

def transiciones(estado, cinta, pila, temp):
    temp2 = len(pila) - 1
    # if temp%2 != 0 :
    if estado == "p":
        aux = cinta[0]
        auxc = pila[temp2]
        if aux == "c":
            if auxc == "#" or auxc == "a" or auxc == "b":
                pila = pila[:-1]                
                if auxc == "#":
                    pila = pila + "#"
                    cinta = cinta[1:]
                if auxc == "b":
                    pila = pila + "b"
                    cinta = cinta[1:]
                if auxc == "a":
                    pila = pila + "a"
                    cinta = cinta[1:]
                print (estado, cinta, pila) 
                estado = "q"
                return transiciones(estado, cinta, pila, temp)
        if  aux == "a" or aux == "b":
            if pila == "#":
                if aux == "a":
                    pila = "#a"
                    cinta = cinta[1:]
                if aux == "b":
                    pila = "#b"
                    cinta = cinta[1:]
            else:
                aux2 = cinta[0]
                aux3 = pila[temp2]
                if aux2 == "a" or aux2 == "b" and aux3 == "a": 
                    pila = pila[:-1]
                    if aux2 == "b":
                        pila = pila + "ab"
                        cinta = cinta[1:]
                    if aux2 == "a":
                        pila = pila + "aa"
                        cinta = cinta[1:]
                if aux2 == "a" or aux2 == "b" and aux3 == "b": 
                    pila = pila[:-1]
                    if aux2 == "b":
                        pila = pila + "bb"
                        cinta = cinta[1:]
                    if aux2 == "a":
                        pila = pila + "ba"
                        cinta = cinta[1:]   

    if estado == "q":
        if not cinta:
            pila = pila[:-1]
            estado = "r"
            return transiciones(estado, cinta, pila, temp) 
        aux = cinta[0]
        auxc = pila[temp2]
        if aux == auxc:
            cinta = cinta[1:]     
            pila = pila[:-1]
            

    if estado == "r":
        return print ("Palabra aceptada")
                
 
    # if estado == "q" or pila == "#abbc":
    #     return print (estado, cinta, pila)  

    print (estado, cinta, pila) 
    return transiciones(estado, cinta, pila, temp) 
              
    # else:
    #     print ("Es par")

transiciones(estado, cinta, pila, temp)