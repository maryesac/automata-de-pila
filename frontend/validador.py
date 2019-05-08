import requests
import json
import time
import ast
from backend.main import Validar
class Validador:
    def validar(self, automata, palabra):
        lienzo = automata.lienzo
        for boton in automata.botones_cinta:
            lienzo.delete(boton)
        for label in automata.label_cinta:
            lienzo.delete(label)
        
        automata.botones_cinta = []
        automata.label_cinta = []
        automata.cinta = []
        self.palabra = palabra
        for c in palabra: 
            automata.cinta.append(c)
        x0 = 60
        y0 = 20
        x1 = 90
        y1 = 50
        for m in automata.cinta:
            btn = lienzo.create_rectangle(x0,y0,x1,y1,fill="gray")
            label = lienzo.create_text(x0 + 16,y0+20,text=m)
            x0 = x0 + 30
            x1 = x1 + 30
            automata.botones_cinta.append(btn)
            automata.label_cinta.append(label)
        validado = Validar(automata).transiciones("p", self.palabra, "#", len(self.palabra))
        if validado == True:
            lienzo.create_text(100, 100, text="APROBADA")
        else:
            lienzo.create_text(100, 100, text="Rechazada")
        
