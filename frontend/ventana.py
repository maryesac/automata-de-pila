from tkinter import *
from tkinter import ttk
from frontend.componentes.automata import Automata
from frontend.validador import Validador

class Ventana:
    def __init__(self):
        self.validador = Validador()
        self.ventana = Tk()
        self.ventana.title("pila")
        self.ventana.geometry("1200x600")
        self.var1 = StringVar()
        self.label = Entry(self.ventana,textvariable=self.var1,relief="solid",width=100)
        self.label.pack()
        self.label.place(x=100,y=10)
        self.boton = Button(self.ventana, text="validar", command=lambda:self.validador.validar(self.automata, self.label.get()))
        self.boton.pack()
        self.boton.place(x=10,y=10)
        self.listbox = Listbox(self.ventana,width=30, height=28)
        self.listbox.pack()
        self.listbox.place(x=10,y=70)
        self.automata = Automata(self.ventana)
        self.color = "#009"
        
        self.ventana.mainloop()
        #self.raiz = Tk()
        #self.raiz.geometry("800x500")
        #self.automata = Automata(self.raiz)
        #self.entry = Entry(self.raiz,  width=80)
        #self.entry.pack()
        
        #self.button = Button(self.raiz, text="Validar", command=lambda: self.validador.validar(self.automata,self.entry.get()))
        #self.button.pack()
        #self.raiz.configure(bg = "#e0e0e0")
        #self.raiz.mainloop()

if __name__ == "__main__":
    Ventana()