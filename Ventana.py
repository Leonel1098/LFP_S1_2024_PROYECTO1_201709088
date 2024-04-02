from tkinter import ttk, filedialog, messagebox
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from Analizador_lexico import Analizador_lexico
from ErrorReporte import reporterror
from TokenReporte import reportoken
import webbrowser

class Ventana:

    def __init__(self, raiz) -> None:
        self.raiz = raiz
        self.raiz.title ("Traductor de Código")
        self.raiz.geometry(("1000x800+350+10"))
        self.raiz.resizable(0,0)

        self.ventana = tk.Frame(raiz)
        self.ventana.config(background="red")
        self.ventana.pack(fill=tk.BOTH, expand=True)

        self.contenedor_texto1 = tk.Text(self.ventana)
        self.contenedor_texto1.pack(side="left")
        self.contenedor_texto1.place(x = "20", y = "40", width=480, height=740)
        

        self.barra_numeros = tk.Text(self.contenedor_texto1, width=3, padx = 4, takefocus = 0, border = 3, background = 'lightblue', state ='disabled')
        self.barra_numeros.pack(side = tk.LEFT, fill = tk.Y)

        self.barra_scroll = ScrolledText(self.contenedor_texto1, wrap = tk.WORD)
        self.barra_scroll.pack(expand=True, fill= "both")

        self.barra_scroll.bind('<Key>', self.columna_numeros)
        self.barra_scroll.bind('<MouseWheel>', self.columna_numeros)

        self.linea_actual = 1

        self.contenedor_texto2 = tk.Text(self.ventana)
        self.contenedor_texto2.pack(side="right")
        self.contenedor_texto2.place(x= "510", y = "40", width=480, height=740)

        self.barra_numeros2 = tk.Text(self.contenedor_texto2, width=3, padx= 4, takefocus= 0, border= 3, background= "lightblue", state= "disabled"  )
        self.barra_numeros2.pack(side= tk.LEFT, fill= tk.Y )

        self.barra_scroll2 = ScrolledText(self.contenedor_texto2, wrap = tk.WORD)
        self.barra_scroll2.pack(expand=True, fill= "both")

        self.boton_cargar_archivo = tk.Button(raiz, text="Cargar Archivo", command= self.abrir_archivo, foreground = "white")
        self.boton_cargar_archivo.pack()
        self.boton_cargar_archivo.config(bg = "black")
        self.boton_cargar_archivo.place(x = "20", y = "10", width= 120, height=25)

        self.boton_guardar = tk.Button(raiz, text="Guardar", command= self.guardar_archivo, foreground = "white")
        self.boton_guardar.pack()
        self.boton_guardar.config(bg = "black")
        self.boton_guardar.place(x = "145", y = "10", width= 120, height=25)



        self.boton_traducir = tk.Button(raiz, text="Traducir Archivo", command= self.mostrar_archivo, foreground = "white")
        self.boton_traducir.pack()
        self.boton_traducir.config(bg = "black")
        self.boton_traducir.place(x = "510", y = "10", width= 120, height=25)

        self.combo = ttk.Combobox (raiz, values = ["Reporte de Tokens","Reporte de Errores","Manual de Usuario","Manual Técnico"])
        self.combo.pack()
        self.combo.config(background = "black")
        self.combo.current(0)
        self.combo.place(x=715, y = 10, width = 125, height = 25)

        self.boton_abrir = tk.Button(raiz, text="Seleccionar Reporte",command = self.Reportando, foreground = "white")
        self.boton_abrir.pack()
        self.boton_abrir.config(bg = "black")
        self.boton_abrir.place(x= 850, y=10, width = 130, height = 25)

    Data = ""
    def abrir_archivo(self):
        archivo = filedialog.askopenfilename()
        if archivo:
            with open(archivo, 'r') as file:
                contenido = file.read()
                self.barra_scroll.delete(1.0, tk.END)
                global Data
                Data = contenido
                Data = self.barra_scroll.insert(tk.INSERT, Data)
                Data = self.barra_scroll.get("1.0","end-1c")
                print("===================================================")
                print(Data)
            self.columna_numeros()
    
    def Analizando(self):
        global Data 
        Data = self.barra_scroll.get("1.0","end-1c")
        print(Data)
        entry = Analizador_lexico()
        entry.analizador(Data)
        f = open ("Analizador.lfp","w")
        f.write(Data)
        f.close()

    def Reportando(self):
        reportes = self.combo.get()
        global Data

        Data = self.barra_scroll.get("1.0","end-1c")
        lexema = Analizador_lexico()
        lexema.analizador(Data)

        if reportes == "Reporte de Tokens":
            lexema.ErrorToken()

        elif reportes == "Reporte de Errores":
            lexema.ErrorReporte()

        elif reportes == "Manual de Usuario":
            webbrowser.open("Manual de Usuario.pdf")

        elif reportes == "Manual Técnico":
            webbrowser.open("Manual Tecnico.pdf")

    def guardar_archivo(self):
        archivo = filedialog.asksaveasfilename(defaultextension = ".lfp")
        if archivo:
            contenido = self.barra_scroll.get(1.0, tk.END)
            with open(archivo, "w") as file:
                file.write(contenido)
            messagebox.showinfo("Guardado", "Archivo Guardado")

    def columna_numeros(self, event = None):
        contador_linea = self.barra_scroll.get("1.0", tk.END).count("\n")
        if contador_linea != self.linea_actual:
            self.barra_numeros.config(state= tk.NORMAL)
            self.barra_numeros.delete(1.0, tk.END)
            for linea in range(1, contador_linea + 1):
                self.barra_numeros.insert(tk.END, f"{linea}\n")
            self.barra_numeros.config(state = tk.DISABLED)
            self.linea_actual = contador_linea

    def mostrar_archivo(self):
        texto = self.barra_scroll.get(1.0, tk.END)
        self.barra_scroll2.config(state= "normal")
        self.barra_scroll2.delete(1.0, tk.END)
        self.barra_scroll2.insert(tk.END, texto)
        self.barra_scroll2.tag_configure("green", foreground="green")
        self.barra_scroll2.tag_add("green", "1.0", "end")
        self.barra_scroll2.config(state='disabled')



        

if __name__ == "__main__":
    root = tk.Tk()
    app = Ventana(root)
    root.mainloop()
