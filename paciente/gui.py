import customtkinter as ctk

class Frame(ctk.CTkFrame):  # Inheriting from CTkFrame for better compatibility
    def __init__(self, root):
        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.camposPacientes()

    def camposPacientes(self):
        # Labels for each field
        self.lblNombre = ctk.CTkLabel(self, text='Nombre:')
        self.lblNombre.configure(font=('ARIAL', 15, 'bold'), text_color='white')
        self.lblNombre.grid(column=0, row=0, padx=10, pady=5, sticky="w")

        self.lblApellidos = ctk.CTkLabel(self, text='Apellidos:')
        self.lblApellidos.configure(font=('ARIAL', 15, 'bold'), text_color='white')
        self.lblApellidos.grid(column=0, row=1, padx=10, pady=5, sticky="w")

        self.lblDNI = ctk.CTkLabel(self, text='DNI:')
        self.lblDNI.configure(font=('ARIAL', 15, 'bold'), text_color='white')
        self.lblDNI.grid(column=0, row=2, padx=10, pady=5, sticky="w")

        self.lblEdad = ctk.CTkLabel(self, text='Edad:')
        self.lblEdad.configure(font=('ARIAL', 15, 'bold'), text_color='white')
        self.lblEdad.grid(column=0, row=3, padx=10, pady=5, sticky="w")

        self.lblTelefono = ctk.CTkLabel(self, text='Teléfono:')
        self.lblTelefono.configure(font=('ARIAL', 15, 'bold'), text_color='white')
        self.lblTelefono.grid(column=0, row=4, padx=10, pady=5, sticky="w")

        self.lblAntecedentes = ctk.CTkLabel(self, text='Antecedentes:')
        self.lblAntecedentes.configure(font=('ARIAL', 15, 'bold'), text_color='white')
        self.lblAntecedentes.grid(column=0, row=5, padx=10, pady=5, sticky="w")

        self.lblMotivo = ctk.CTkLabel(self, text='Motivo:')
        self.lblMotivo.configure(font=('ARIAL', 15, 'bold'), text_color='white')
        self.lblMotivo.grid(column=0, row=6, padx=10, pady=5, sticky="w")

        self.lblTratamiento = ctk.CTkLabel(self, text='Tratamiento:')
        self.lblTratamiento.configure(font=('ARIAL', 15, 'bold'), text_color='white')
        self.lblTratamiento.grid(column=0, row=7, padx=10, pady=5, sticky="w")

        # Entry fields for each label
        self.entryNombre = ctk.CTkEntry(self, width=200, placeholder_text="Ingrese nombre")
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5, sticky="w")

        self.entryApellidos = ctk.CTkEntry(self, width=200, placeholder_text="Ingrese apellidos")
        self.entryApellidos.grid(column=1, row=1, padx=10, pady=5, sticky="w")

        self.entryDNI = ctk.CTkEntry(self, width=200, placeholder_text="Ingrese DNI")
        self.entryDNI.grid(column=1, row=2, padx=10, pady=5, sticky="w")

        self.entryEdad = ctk.CTkEntry(self, width=200, placeholder_text="Ingrese edad")
        self.entryEdad.grid(column=1, row=3, padx=10, pady=5, sticky="w")

        self.entryTelefono = ctk.CTkEntry(self, width=200, placeholder_text="Ingrese teléfono")
        self.entryTelefono.grid(column=1, row=4, padx=10, pady=5, sticky="w")

        self.entryAntecedentes = ctk.CTkEntry(self, width=200, placeholder_text="Ingrese antecedentes")
        self.entryAntecedentes.grid(column=1, row=5, padx=10, pady=5, sticky="w")

        self.entryMotivo = ctk.CTkEntry(self, width=200, placeholder_text="Ingrese motivo")
        self.entryMotivo.grid(column=1, row=6, padx=10, pady=5, sticky="w")

        self.entryTratamiento = ctk.CTkEntry(self, width=200, placeholder_text="Ingrese tratamiento")
        self.entryTratamiento.grid(column=1, row=7, padx=10, pady=5, sticky="w")

# Aquí puedes inicializar tu aplicación como lo hiciste antes.
        self.btnNuevo=ctk.CTkButton(self, text="Nuevo", fg_color="#2ECC71", hover_color="#27AE60")
        self.btnNuevo.grid(column=0, row=8, padx=10, pady=5, sticky="w")