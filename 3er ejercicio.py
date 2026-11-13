import tkinter as tk
from tkinter import messagebox
import math

class ArithmeticException(Exception):
    pass


class InputMismatchException(Exception):
    pass

class CalculosNumericos:

    def calcularLogaritmoNeperiano(self, valor):

        if valor <= 0:
            raise ArithmeticException(
                "El valor debe ser un número positivo para calcular el logaritmo."
            )

        return math.log(valor)

    def calcularRaizCuadrada(self, valor):

        if valor < 0:
            raise ArithmeticException(
                "El valor debe ser positivo para calcular la raíz cuadrada."
            )

        return math.sqrt(valor)

class InterfazCalculos:

    def __init__(self, ventana):

        self.ventana = ventana
        self.ventana.title("Cálculos Numéricos")
        self.ventana.geometry("430x350")
        self.ventana.resizable(False, False)

        self.calculos = CalculosNumericos()

        titulo = tk.Label(
            ventana,
            text="CÁLCULOS NUMÉRICOS",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=20)

        etiqueta = tk.Label(
            ventana,
            text="Ingrese un valor numérico:",
            font=("Arial", 12)
        )
        etiqueta.pack(pady=5)

        self.entrada = tk.Entry(
            ventana,
            font=("Arial", 14),
            justify="center"
        )
        self.entrada.pack(pady=10)

        boton_logaritmo = tk.Button(
            ventana,
            text="Calcular logaritmo neperiano",
            font=("Arial", 11),
            width=30,
            command=self.calcularLogaritmo
        )
        boton_logaritmo.pack(pady=8)

        boton_raiz = tk.Button(
            ventana,
            text="Calcular raíz cuadrada",
            font=("Arial", 11),
            width=30,
            command=self.calcularRaiz
        )
        boton_raiz.pack(pady=8)

        self.resultado = tk.Label(
            ventana,
            text="Resultado:",
            font=("Arial", 13, "bold"),
            fg="blue"
        )
        self.resultado.pack(pady=20)

    def obtenerValor(self):

        try:
            valor = float(self.entrada.get())
            return valor

        except ValueError:
            raise InputMismatchException(
                "Debe ingresar un valor numérico."
            )

    def calcularLogaritmo(self):

        try:
            valor = self.obtenerValor()

            resultado = self.calculos.calcularLogaritmoNeperiano(valor)

            self.resultado.config(
                text=f"Resultado: {resultado:.6f}",
                fg="blue"
            )

        except ArithmeticException as e:
            messagebox.showerror("Error aritmético", str(e))

        except InputMismatchException as e:
            messagebox.showerror("Error de entrada", str(e))

    def calcularRaiz(self):

        try:
            valor = self.obtenerValor()

            resultado = self.calculos.calcularRaizCuadrada(valor)

            self.resultado.config(
                text=f"Resultado: {resultado:.6f}",
                fg="blue"
            )

        except ArithmeticException as e:
            messagebox.showerror("Error aritmético", str(e))

        except InputMismatchException as e:
            messagebox.showerror("Error de entrada", str(e))


if __name__ == "__main__":

    ventana = tk.Tk()

    aplicacion = InterfazCalculos(ventana)

    ventana.mainloop()

