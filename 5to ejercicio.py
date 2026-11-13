import tkinter as tk
from tkinter import filedialog, messagebox


class LeerArchivo:

    def __init__(self, ventana):

        self.ventana = ventana
        self.nombreArchivo = ""

        self.ventana.title("Lector de archivos")
        self.ventana.geometry("600x450")
        self.ventana.resizable(False, False)

        tk.Label(
            ventana,
            text="LECTOR DE ARCHIVOS",
            font=("Arial", 18, "bold")
        ).pack(pady=15)

        tk.Button(
            ventana,
            text="Seleccionar archivo",
            command=self.seleccionarArchivo,
            width=20
        ).pack(pady=5)

        self.etiqueta = tk.Label(
            ventana,
            text="Ningun archivo seleccionado",
            font=("Arial", 10)
        )
        self.etiqueta.pack(pady=5)

        tk.Button(
            ventana,
            text="Leer archivo",
            command=self.leerArchivo,
            width=20
        ).pack(pady=5)

        marco = tk.Frame(ventana)
        marco.pack(padx=20, pady=15, fill="both", expand=True)

        barra = tk.Scrollbar(marco)
        barra.pack(side="right", fill="y")

        self.areaTexto = tk.Text(
            marco,
            font=("Arial", 10),
            yscrollcommand=barra.set,
            wrap="word"
        )
        self.areaTexto.pack(side="left", fill="both", expand=True)

        barra.config(command=self.areaTexto.yview)

    def seleccionarArchivo(self):

        self.nombreArchivo = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[("Archivos de texto", "*.txt")]
        )

        if self.nombreArchivo:

            self.etiqueta.config(
                text=self.nombreArchivo
            )

            self.areaTexto.delete("1.0", tk.END)

    def leerArchivo(self):

        if self.nombreArchivo == "":
            messagebox.showwarning(
                "Advertencia",
                "Primero debe seleccionar un archivo."
            )
            return

        try:

            with open(
                self.nombreArchivo,
                "r",
                encoding="utf-8-sig"
            ) as archivo:

                contenido = archivo.read()

                self.areaTexto.delete("1.0", tk.END)

                if contenido == "":
                    messagebox.showinfo(
                        "Informacion",
                        "El archivo esta vacio."
                    )
                else:
                    self.areaTexto.insert(tk.END, contenido)

        except FileNotFoundError:
            messagebox.showerror(
                "Error",
                "No se encontro el archivo."
            )

        except PermissionError:
            messagebox.showerror(
                "Error",
                "No tiene permisos para leer el archivo."
            )

        except UnicodeDecodeError:
            messagebox.showerror(
                "Error",
                "No se pudo interpretar el contenido del archivo."
            )

        except OSError as error:
            messagebox.showerror(
                "Error",
                f"No se pudo leer el archivo: {error}"
            )

ventana = tk.Tk()
aplicacion = LeerArchivo(ventana)
ventana.mainloop()


        