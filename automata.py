class Automata(object):

	def __init__(self):
		self.cinta = None
		self.pila = None
		self.tamano = None
		self.estado = None

	def __str__(self):
		print("hello6")
		return ("Informacion del Automata:\n1. Cinta: "+self.cinta+"\n2. Pila: "+self.pila+"\n3. Tamaño: "+str(self.tamano)+"\n4. estado: "+self.estado)
		
			