import tkinter as tk
from tkinter import messagebox

class Nodo:
    def __init__(self, pregunta, si=None, no=None):
        self.pregunta = pregunta
        self.si = si
        self.no = no

def construir_arbol_de_decision():
    raiz = Nodo("¿Tiene fiebre?")
    raiz.si = Nodo("¿Tiene dolor de garganta?")
    raiz.no = Nodo("¿Tiene tos seca?")

    raiz.si.si = Nodo("Gripe")
    raiz.si.no = Nodo("Amigdalitis")

    raiz.no.si = Nodo("¿Tiene secreción nasal?")
    raiz.no.no = Nodo("Resfriado común")

    raiz.no.si.si = Nodo("Rinitis alérgica")
    raiz.no.si.no = Nodo("Sinusitis")

    return raiz

def hacer_diagnostico(nodo_actual):
    respuesta = messagebox.askyesno("Pregunta", nodo_actual.pregunta)
    if respuesta:
        siguiente_nodo = nodo_actual.si
    else:
        siguiente_nodo = nodo_actual.no

    if siguiente_nodo:
        hacer_diagnostico(siguiente_nodo)
    else:
        messagebox.showinfo("Diagnóstico", nodo_actual.pregunta)

def iniciar_diagnostico():
    arbol = construir_arbol_de_decision()
    hacer_diagnostico(arbol)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de diagnóstico de enfermedades")

# Etiqueta de bienvenida
etiqueta_bienvenida = tk.Label(ventana, text="Bienvenido al sistema de diagnóstico de enfermedades")
etiqueta_bienvenida.pack()

# Botón de iniciar diagnóstico
boton_iniciar = tk.Button(ventana, text="Iniciar diagnóstico", command=iniciar_diagnostico)
boton_iniciar.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()