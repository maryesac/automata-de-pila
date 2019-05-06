from factory import Factory
if __name__ == '__main__':
	creador = Factory()
	print("hola1")
	automata = creador.get_automata("abcba")

	print(automata) 
	#Factory.transiciones(automata)
