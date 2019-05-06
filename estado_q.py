from automata import Automata

class Estado_q(automata):

	def __init__(self, cinta):
		self.cinta = cinta
		self.pila = "#"
		self.tamano = len(cinta)
		self.estado = "q"