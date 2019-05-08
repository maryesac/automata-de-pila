from automata import Automata

class Estadop(Automata):

	def __init__(self, cinta):
		self.cinta = cinta
		self.pila = "#"
		self.tamano = len(cinta)
		self.estado = "p"