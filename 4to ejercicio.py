import tkinter as tk
from tkinter import ttk, messagebox

class EquipoCompletoError(Exception):
    pass


class Programador:

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class EquipoMaratonProgramacion:

    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion

        self.tamano_equipo = 0
        self.programadores = []
        self.capacidad = 3

    def esta_lleno(self):
        return self.tamano_equipo == self.capacidad

    def validar_campo(self, campo):

        if not campo.strip():
            raise ValueError("El campo no puede estar vacio.")

        for caracter in campo:
            if caracter.isdigit():
                raise ValueError(
                    "El nombre no puede tener digitos."
                )

        if len(campo) > 20:
            raise ValueError(
                "La longitud no debe ser superior a 20 caracteres."
            )

    def agregar(self, programador):

        if self.esta_lleno():
            raise EquipoCompletoError(
                "El equipo esta completo. No se pudo agregar el programador."
            )

        self.validar_campo(programador.nombre)
        self.validar_campo(programador.apellidos)

        self.programadores.append(programador)
        self.tamano_equipo += 1


class InterfazGrafica:

    def __init__(self, ventana):

        self.ventana = ventana
        self.ventana.title("Maraton de Programacion")
        self.ventana.geometry("650x650")
        self.ventana.resizable(False, False)

        self.equipo = None

        self.crear_interfaz()

    def crear_interfaz(self):

        titulo = ttk.Label(
            self.ventana,
            text="REGISTRO - MARATON DE PROGRAMACION",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=15)

        marco_equipo = ttk.LabelFrame(
            self.ventana,
            text="Datos del equipo",
            padding=15
        )
        marco_equipo.pack(fill="x", padx=25, pady=10)

        ttk.Label(marco_equipo, text="Nombre del equipo:").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.entrada_equipo = ttk.Entry(marco_equipo, width=35)
        self.entrada_equipo.grid(row=0, column=1, pady=5)

        ttk.Label(marco_equipo, text="Universidad:").grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.entrada_universidad = ttk.Entry(
            marco_equipo, width=35
        )
        self.entrada_universidad.grid(row=1, column=1, pady=5)

        ttk.Label(marco_equipo, text="Lenguaje de programacion:").grid(
            row=2, column=0, sticky="w", pady=5
        )
        self.entrada_lenguaje = ttk.Entry(
            marco_equipo, width=35
        )
        self.entrada_lenguaje.grid(row=2, column=1, pady=5)

        marco_programador = ttk.LabelFrame(
            self.ventana,
            text="Datos del programador",
            padding=15
        )
        marco_programador.pack(fill="x", padx=25, pady=10)

        ttk.Label(marco_programador, text="Nombre:").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.entrada_nombre = ttk.Entry(
            marco_programador, width=35
        )
        self.entrada_nombre.grid(row=0, column=1, pady=5)

        ttk.Label(marco_programador, text="Apellidos:").grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.entrada_apellidos = ttk.Entry(
            marco_programador, width=35
        )
        self.entrada_apellidos.grid(row=1, column=1, pady=5)

        self.boton_agregar = ttk.Button(
            marco_programador,
            text="Agregar programador",
            command=self.agregar_programador
        )
        self.boton_agregar.grid(
            row=2, column=0, columnspan=2, pady=15
        )

        marco_lista = ttk.LabelFrame(
            self.ventana,
            text="Integrantes del equipo",
            padding=15
        )
        marco_lista.pack(fill="both", expand=True, padx=25, pady=10)

        self.lista = ttk.Treeview(
            marco_lista,
            columns=("nombre", "apellidos"),
            show="headings",
            height=5
        )

        self.lista.heading("nombre", text="Nombre")
        self.lista.heading("apellidos", text="Apellidos")

        self.lista.column("nombre", width=200)
        self.lista.column("apellidos", width=250)

        self.lista.pack(fill="both", expand=True)

        self.etiqueta_estado = ttk.Label(
            self.ventana,
            text="Integrantes registrados: 0 / 3",
            font=("Arial", 11, "bold")
        )
        self.etiqueta_estado.pack(pady=10)

    def agregar_programador(self):

        try:

            nombre = self.entrada_nombre.get().strip()
            apellidos = self.entrada_apellidos.get().strip()

            if self.equipo is None:

                nombre_equipo = self.entrada_equipo.get().strip()
                universidad = self.entrada_universidad.get().strip()
                lenguaje = self.entrada_lenguaje.get().strip()

                if not nombre_equipo or not universidad or not lenguaje:
                    raise ValueError(
                        "Debe completar todos los datos del equipo."
                    )

                self.equipo = EquipoMaratonProgramacion(
                    nombre_equipo,
                    universidad,
                    lenguaje
                )

                self.entrada_equipo.config(state="disabled")
                self.entrada_universidad.config(state="disabled")
                self.entrada_lenguaje.config(state="disabled")

            programador = Programador(nombre, apellidos)

            self.equipo.agregar(programador)

            self.lista.insert(
                "",
                "end",
                values=(programador.nombre, programador.apellidos)
            )

            self.etiqueta_estado.config(
                text=f"Integrantes registrados: "
                     f"{self.equipo.tamano_equipo} / 3"
            )

            self.entrada_nombre.delete(0, tk.END)
            self.entrada_apellidos.delete(0, tk.END)

            messagebox.showinfo(
                "Registro exitoso",
                "El programador fue agregado correctamente."
            )

            if self.equipo.esta_lleno():

                self.boton_agregar.config(state="disabled")

                messagebox.showwarning(
                    "Equipo completo",
                    "El equipo ya tiene sus tres integrantes."
                )

        except (ValueError, EquipoCompletoError) as error:

            messagebox.showerror("Error de validacion", str(error))

if __name__ == "__main__":

    ventana = tk.Tk()

    aplicacion = InterfazGrafica(ventana)

    ventana.mainloop()
