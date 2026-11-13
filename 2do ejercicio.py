import tkinter as tk
from tkinter import messagebox

class Vendedor:

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0

    def imprimir(self):
        return (
            f"Nombre del vendedor: {self.nombre}\n"
            f"Apellidos del vendedor: {self.apellidos}\n"
            f"Edad del vendedor: {self.edad} años"
        )

    def verificar_edad(self, edad):

        if edad < 18:
            raise ValueError(
                "El vendedor debe ser mayor de 18 años."
            )

        elif edad > 120:
            raise ValueError(
                "La edad no puede ser negativa ni mayor a 120."
            )

        else:
            self.edad = edad



def registrar_vendedor():

    nombre = entrada_nombre.get().strip()
    apellidos = entrada_apellidos.get().strip()
    edad_texto = entrada_edad.get().strip()

    
    if not nombre or not apellidos or not edad_texto:
        messagebox.showwarning(
            "Campos vacíos",
            "Debe completar todos los campos."
        )
        return

    try:
        
        edad = int(edad_texto)

        
        vendedor = Vendedor(nombre, apellidos)

        
        vendedor.verificar_edad(edad)

        
        resultado.config(
            text=vendedor.imprimir()
        )

        messagebox.showinfo(
            "Registro exitoso",
            "El vendedor ha sido registrado correctamente."
        )

    except ValueError as error:
        messagebox.showerror(
            "Error de validación",
            str(error)
        )

ventana = tk.Tk()
ventana.title("Registro de vendedores")
ventana.geometry("420x430")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana,
    text="REGISTRO DE VENDEDORES",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=20)

tk.Label(
    ventana,
    text="Nombre:",
    font=("Arial", 11)
).pack()

entrada_nombre = tk.Entry(
    ventana,
    font=("Arial", 11),
    width=30
)
entrada_nombre.pack(pady=5)

tk.Label(
    ventana,
    text="Apellidos:",
    font=("Arial", 11)
).pack()

entrada_apellidos = tk.Entry(
    ventana,
    font=("Arial", 11),
    width=30
)
entrada_apellidos.pack(pady=5)

tk.Label(
    ventana,
    text="Edad:",
    font=("Arial", 11)
).pack()

entrada_edad = tk.Entry(
    ventana,
    font=("Arial", 11),
    width=30
)
entrada_edad.pack(pady=5)

boton_registrar = tk.Button(
    ventana,
    text="Registrar vendedor",
    font=("Arial", 11, "bold"),
    bg="#2196F3",
    fg="white",
    command=registrar_vendedor
)
boton_registrar.pack(pady=20)

tk.Label(
    ventana,
    text="Información del vendedor:",
    font=("Arial", 11, "bold")
).pack()

resultado = tk.Label(
    ventana,
    text="",
    font=("Arial", 11),
    justify="left"
)
resultado.pack(pady=10)

ventana.mainloop()
