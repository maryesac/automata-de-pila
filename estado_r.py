from automata import Automata

class Estado_q(automata):

	def __init__(self, cinta, pila, tamano):
		self.cinta = cinta
		self.pila = pila
		self.tamano = tamano
		self.estado = "p"