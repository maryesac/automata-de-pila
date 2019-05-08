<<<<<<< HEAD
from frontend.validador import Validador
from frontend.ventana import Ventana

ventana = Ventana()
=======
from factory import Factory
if __name__ == '__main__':
	creador = Factory()
	print("hola1")
	automata = creador.get_automata("abcba")

	print(automata) 
	#Factory.transiciones(automata)
>>>>>>> 29d8c587802264f3b337f2bbdcd4d2ae6b8738ea
