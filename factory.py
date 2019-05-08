from estadop import Estadop


class Factory(object):

	def get_automata(self, cinta):
		print("hola2")
		if (cinta[0] is ''): 
			print("hola3")
			return (print("palabra no aceptada"))
		elif (len(cinta)%2 == 0):
			print("hola4")
			return (print("palabra no aceptada"))
		elif (cinta[0] != ""):
			print("hola5")
			return Estadop(cinta)

	def transiciones(cinta, pila, tamano, estado):
		aux = cinta[0]
		cinta = cinta[1:]
		auxc = pila[tamano] 
		validar(aux, auxc, pila, estado)
		transiciones(cinta, pila, tamano, estado)

	def validar(aux, auxc, pila, estado):
		pila = pila[:-1]
		if (estado == "p"):
			if(aux == "a" and auxc == "a"):
				pila = pila + "aa"
				return (aux, auxc, pila, estado)
			if(aux == "a" and auxc == "b"):
				pila = pila + "ba"
				return (aux, auxc, pila, estado)
			if(aux == "b" and auxc == "a"):
				pila = pila + "ab"
				return (aux, auxc, pila, estado)
			if(aux == "b" and auxc == "b"):
				pila = pila + "bb"
				return (aux, auxc, pila, estado)
			if(aux == "a" and auxc == "#"):
				pila = pila + "#a"
				return (aux, auxc, pila, estado)
			if(aux == "b" and auxc == "#"):
				pila = pila + "#b"
				return (aux, auxc, pila, estado)
			if(aux == "c" and auxc == "#"):
				pila = pila + "#"
				estado = "q"
				return (aux, auxc, pila, estado)
			if(aux == "c" and auxc == "a"):
				pila = pila + "a"
				estado = "q"
				return (aux, auxc, pila, estado)
			if(aux == "c" and auxc == "b"):
				pila = pila + "b"
				estado = "q"
				return (aux, auxc, pila, estado)
		
		elif (estado == "q"):
			if(aux == "a" and auxc == "a"):
				pila = pila + ""
				return (aux, auxc, pila, estado)
			if(aux == "b" and auxc == "b"):
				pila = pila + ""
				return (aux, auxc, pila, estado)
			if(aux == "" and auxc == "#"):
				pila = pila + "#"
				estado = "r"
				return (aux, auxc, pila, estado)
		
		elif (estado == "r"):
			print("palabra aceptada")
			return 0
