import tkinter as tk
from tkinter import messagebox, scrolledtext
from gramatica import Gramatica

class Interfaz:
    def __init__(self, master):
        self.master = master
        master.title("Generador de arboles y verificador de palabras")

    
        tk.Label(master, text="Simbolos Terminales (separados por comas):").pack()
        self.entry_terminales = tk.Entry(master)
        self.entry_terminales.pack()

        tk.Label(master, text="Simbolos No Terminales (separados por comas):").pack()
        self.entry_no_terminales = tk.Entry(master)
        self.entry_no_terminales.pack()

        tk.Label(master, text="Producciones (A->B, separadas por comas):").pack()
        self.entry_producciones = tk.Entry(master)
        self.entry_producciones.pack()

        tk.Label(master, text="Simbolo Inicial:").pack()
        self.entry_simbolo_inicial = tk.Entry(master)
        self.entry_simbolo_inicial.pack()

        tk.Label(master, text="Palabra a Verificar (w):").pack()
        self.entry_palabra = tk.Entry(master)
        self.entry_palabra.pack()

        tk.Label(master, text="Nivel Máximo del arbol General:").pack()
        self.entry_nivel_maximo = tk.Entry(master)  
        self.entry_nivel_maximo.pack()

   
        btn_verificar = tk.Button(master, text="Verificar Palabra", command=self.verificar_palabra)
        btn_verificar.pack()


        self.text_area = scrolledtext.ScrolledText(master, width=60, height=20)
        self.text_area.pack()

    def verificar_palabra(self):
        terminales = self.entry_terminales.get().split(',')
        no_terminales = self.entry_no_terminales.get().split(',')
        producciones = self.entry_producciones.get().split(',')
        simbolo_inicial = self.entry_simbolo_inicial.get()
        palabra = self.entry_palabra.get()
        max_nivel = int(self.entry_nivel_maximo.get()) 

        
        if len(terminales) < 2:
            messagebox.showerror("Error", "Se deben ingresar al menos 2 símbolos terminales.")
            return
        if len(no_terminales) < 3:
            messagebox.showerror("Error", "Se deben ingresar al menos 3 símbolos no terminales.")
            return
        if len(producciones) < 3:
            messagebox.showerror("Error", "Se deben ingresar al menos 3 producciones.")
            return

        gramatica = Gramatica(terminales, no_terminales, producciones, simbolo_inicial)

        pertenece = gramatica.pertenece_al_lenguaje(palabra)
        resultado_text = f"w='{palabra}' {': W1 ∈ L -> pertenece' if pertenece else ': NO pertenece'} al lenguaje.\n"
        resultado_text += "Árbol de derivación particular (horizontal):\n"
        resultado_text += gramatica.mostrar_arbol_derivacion()  
        resultado_text += "\nÁrbol de derivación general:\n" + gramatica.mostrar_arbol_general(max_nivel=max_nivel)

        
        self.text_area.delete(1.0, tk.END)  
        self.text_area.insert(tk.END, resultado_text)

 
ventana = tk.Tk()
interfaz = Interfaz(ventana)

ventana.mainloop()
