import tkinter as tk
from tkinter import scrolledtext


class PruebaExcepciones:

    def __init__(self, ventana):

        self.ventana = ventana
        self.ventana.title("Prueba de excepciones")
        self.ventana.geometry("550x450")
        self.ventana.resizable(False, False)

        
        titulo = tk.Label(
            ventana,
            text="Manejo de excepciones",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        
        self.area_texto = scrolledtext.ScrolledText(
            ventana,
            width=60,
            height=15,
            font=("Consolas", 11),
            state="disabled"
        )
        self.area_texto.pack(padx=15, pady=10)

        
        boton = tk.Button(
            ventana,
            text="Ejecutar programa",
            font=("Arial", 12),
            command=self.ejecutar
        )
        boton.pack(pady=15)

    def imprimir(self, mensaje):

        self.area_texto.config(state="normal")
        self.area_texto.insert(tk.END, mensaje + "\n")
        self.area_texto.config(state="disabled")

    def ejecutar(self):

        self.area_texto.config(state="normal")
        self.area_texto.delete("1.0", tk.END)
        self.area_texto.config(state="disabled")

        
        try:

            self.imprimir("Ingresando al primer try")

            cociente = 10000 / 0

        except ZeroDivisionError:

            self.imprimir("División por cero")

        finally:

            self.imprimir("Ingresando al primer finally")

        
        try:

            self.imprimir("Ingresando al segundo try")

            objeto = None
            objeto.toString()

            self.imprimir("Imprimiendo objeto")

        except ZeroDivisionError:

            self.imprimir("División por cero")

        except Exception:

            self.imprimir("Ocurrió una excepción")

        finally:

            self.imprimir("Ingresando al segundo finally")


if __name__ == "__main__":

    ventana = tk.Tk()

    aplicacion = PruebaExcepciones(ventana)

    ventana.mainloop()
