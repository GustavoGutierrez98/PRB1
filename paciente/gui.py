import tkinter as tk
import customtkinter as ctk
from customtkinter import *
from time import strftime
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from modelo.pacienteDao import Persona, guardarDatoPaciente, listarCondicion, listar, editarDatoPaciente, eliminarPaciente

class Frame(ctk.CTkFrame):  # Inheriting from CTkFrame for better compatibility
    def __init__(self, root):
        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.camposPacientes()
        self.lblReloj = ctk.CTkLabel(self, font=('Arial', 15, 'bold'), text_color='white')
        self.lblReloj.grid(row=0, column=7, padx=10, pady=10,columnspan=7)
        self.lblFecha = ctk.CTkLabel(self, font=('Arial', 15, 'bold'), text_color='white')
        self.lblFecha.grid(row=0, column=6, padx=10, pady=5,columnspan=6)
        self.deshabilitar()
        self.tablaPaciente()
        self.reloj()        

    def reloj(self):
        tiempo = strftime('%I:%M:%S %p')  # Formato de 12 horas
        fecha = datetime.now().strftime('%d de %B del %Y')  # Formato deseado
        self.lblReloj.configure(text=tiempo)
        self.lblFecha.configure(text=fecha)
        self.lblReloj.after(1000, self.reloj) 

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

        self.lblPeso = ctk.CTkLabel(self, text='Peso:')
        self.lblPeso.configure(font=('ARIAL', 15, 'bold'), text_color='white')
        self.lblPeso.grid(column=0, row=4, padx=10, pady=5, sticky="w")

        self.lblTalla = ctk.CTkLabel(self, text='Talla:')
        self.lblTalla.configure(font=('ARIAL', 15, 'bold'), text_color='white')
        self.lblTalla.grid(column=0, row=5, padx=10, pady=5, sticky="w")

        self.lblIMC = ctk.CTkLabel(self, text='IMC:')
        self.lblIMC.configure(font=('ARIAL', 15, 'bold'), text_color='white')
        self.lblIMC.grid(column=0, row=6, padx=10, pady=5, sticky="w")

        self.lblTelefono = ctk.CTkLabel(self, text='Teléfono:')
        self.lblTelefono.configure(font=('ARIAL', 15, 'bold'), text_color='white')
        self.lblTelefono.grid(column=0, row=7, padx=10, pady=5, sticky="w")

        self.lblAntecedentes = ctk.CTkLabel(self, text='Antecedentes:')
        self.lblAntecedentes.configure(font=('ARIAL', 15, 'bold'), text_color='white')
        self.lblAntecedentes.grid(column=0, row=8, padx=10, pady=5, sticky="w")

        # Entry fields for each label
        self.svNombre = ctk.StringVar()
        self.entryNombre = ctk.CTkEntry(self, width=200, textvariable=self.svNombre, placeholder_text="Ingrese nombre")
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5, sticky="w", columnspan=2)

        self.svApellidos = ctk.StringVar()
        self.entryApellidos = ctk.CTkEntry(self, width=200, textvariable=self.svApellidos, placeholder_text="Ingrese apellidos")
        self.entryApellidos.grid(column=1, row=1, padx=10, pady=5, sticky="w", columnspan=2)

        self.svDNI = ctk.StringVar()
        self.entryDNI = ctk.CTkEntry(self, width=200, textvariable=self.svDNI, placeholder_text="Ingrese DNI")
        self.entryDNI.grid(column=1, row=2, padx=10, pady=5, sticky="w", columnspan=2)
        self.entryDNI.bind("<KeyRelease>", lambda e: self.validate_numeric(self.entryDNI))

        self.svEdad = ctk.StringVar()
        self.entryEdad = ctk.CTkEntry(self, width=200, textvariable=self.svEdad, placeholder_text="Ingrese edad")
        self.entryEdad.grid(column=1, row=3, padx=10, pady=5, sticky="w", columnspan=2)
        self.entryEdad.bind("<KeyRelease>", lambda e: self.validate_numeric(self.entryEdad))

        self.svPeso = ctk.StringVar()
        self.entryPeso = ctk.CTkEntry(self, width=200, textvariable=self.svPeso, placeholder_text="Ingrese peso")
        self.entryPeso.grid(column=1, row=4, padx=10, pady=5, sticky="w", columnspan=2)
        self.entryPeso.bind("<KeyRelease>", lambda e: self.validate_numeric(self.entryPeso))

        self.svTalla = ctk.StringVar()
        self.entryTalla = ctk.CTkEntry(self, width=200, textvariable=self.svTalla, placeholder_text="Ingrese talla")
        self.entryTalla.grid(column=1, row=5, padx=10, pady=5, sticky="w", columnspan=2)
        self.entryTalla.bind("<KeyRelease>", lambda e: self.validate_numeric(self.entryTalla))

        self.svIMC = ctk.StringVar()
        self.entryIMC = ctk.CTkEntry(self, width=200, textvariable=self.svIMC, placeholder_text="Ingrese IMC")
        self.entryIMC.grid(column=1, row=6, padx=10, pady=5, sticky="w", columnspan=2)
        self.entryIMC.bind("<KeyRelease>", lambda e: self.validate_numeric(self.entryIMC))

        self.svTelefono = ctk.StringVar()
        self.entryTelefono = ctk.CTkEntry(self, width=200, textvariable=self.svTelefono, placeholder_text="Ingrese teléfono")
        self.entryTelefono.grid(column=1, row=7, padx=10, pady=5, sticky="w", columnspan=2)
        self.entryTelefono.bind("<KeyRelease>", lambda e: self.format_phone(self.entryTelefono))

        self.svAntecedentes = ctk.StringVar()
        self.entryAntecedentes = ctk.CTkEntry(self, width=200, textvariable=self.svAntecedentes, placeholder_text="Ingrese antecedentes")
        self.entryAntecedentes.grid(column=1, row=8, padx=10, pady=5, sticky="w", columnspan=2)

        # Buttons
        self.btnNuevo = ctk.CTkButton(self, text="NUEVO", command=self.habilitar, text_color='white')
        self.btnNuevo.configure(font=('ARIAL',16,'bold'),fg_color="#800080")
        self.btnNuevo.grid(column=0, row=9, padx=10, pady=5, sticky="w")

        self.btnGuardar = ctk.CTkButton(self, text="GUARDAR", command=self.guardarPaciente, text_color='white')        
        self.btnGuardar.configure(font=('ARIAL',16,'bold'),fg_color="#800080")
        self.btnGuardar.grid(column=1, row=9, padx=10, pady=5, sticky="w")

        self.btnCancelar = ctk.CTkButton(self, text="CANCELAR", command=self.deshabilitar, text_color='white')
        self.btnCancelar.configure(font=('ARIAL',16,'bold'),fg_color="#800080")
        self.btnCancelar.grid(column=2, row=9, padx=10, pady=5, sticky="w")

        #BUSCADOR
        #LABEL BUSCADOR
        self.lblBuscarDni = ctk.CTkLabel(self, text='Buscar el DNI:')
        self.lblBuscarDni.configure(font=('ARIAL',15,'bold'), text_color='white')
        self.lblBuscarDni.grid(column=3, row=0, padx=10, pady=5)

        self.lblBuscarApellido = ctk.CTkLabel(self, text='Buscar por apellido:')
        self.lblBuscarApellido.configure(font=('ARIAL',15,'bold'), text_color='white')
        self.lblBuscarApellido.grid(column=3, row=1, padx=10, pady=5)

        #ENTRYS BUSCADOR
        self.svBuscarDni = ctk.StringVar()
        self.entryBuscarDni = ctk.CTkEntry(self, textvariable=self.svBuscarDni)
        self.entryBuscarDni.configure(width=200, font=('ARIAL',15, 'bold'), text_color='white')
        self.entryBuscarDni.grid(column=4, row=0, padx=10, pady=5, columnspan=3)

        self.svBuscarApellido = ctk.StringVar()
        self.entryBuscarApellido = ctk.CTkEntry(self, textvariable=self.svBuscarApellido)
        self.entryBuscarApellido.configure(width=200, font=('ARIAL',15, 'bold'), text_color='white')
        self.entryBuscarApellido.grid(column=4, row=1, padx=10, pady=5, columnspan=3)

        #BUTTON BUSCADOR
        self.btnBuscarCondicion = ctk.CTkButton(self, text='BUSCAR', command = self.buscarCondicion)
        self.btnBuscarCondicion.configure(font=('ARIAL',16,'bold'),fg_color="#800080", text_color='white')
        self.btnBuscarCondicion.grid(column=4,row=2, padx=10, pady=5, columnspan=1)

        self.btnLimpiarBuscador = ctk.CTkButton(self, text='LIMPIAR', command = self.limpiarBuscador)
        self.btnLimpiarBuscador.configure(font=('ARIAL',16,'bold'),fg_color="#800080", text_color='white')
        self.btnLimpiarBuscador.grid(column=4,row=3, padx=10, pady=5, columnspan=1)

    def validate_numeric(self, entry):
        # Get the current text from the entry
        value = entry.get()
        # Validate that the text is numeric
        if not value.isdigit() and value != "":
            entry.delete(len(value) - 1)

    def format_phone(self, entry):
        # Format the phone number (example: 123-456-7890)
        value = entry.get().replace("-", "").replace(" ", "")
        if value.isdigit() or value == "":
            if len(value) >= 3:
                formatted = f"{value[:3]}-{value[3:6]}-{value[6:]}"
            else:
                formatted = value
            entry.delete(0, "end")
            entry.insert(0, formatted)

    def limpiarBuscador(self):
        self.svBuscarApellido.set('')
        self.svBuscarDni.set('')
        self.tablaPaciente()

    def buscarCondicion(self):
        if len(self.svBuscarDni.get()) > 0 or len(self.svBuscarApellido.get()) > 0:
            where = "WHERE 1=1"
            if (len(self.svBuscarDni.get())) > 0:
                where = "WHERE dni = " + self.svBuscarDni.get() + "" #WHERE dni = 87878787
            if (len(self.svBuscarApellido.get())) > 0:
                where = "WHERE apellidos LIKE '" + self.svBuscarApellido.get()+"%' AND activo = 1"
            
            self.tablaPaciente(where)
        else:
            self.tablaPaciente()


    def habilitar(self):
        self.svNombre.set('')
        self.svApellidos.set('')
        self.svDNI.set('')
        self.svEdad.set('')
        self.svPeso.set('')
        self.svTalla.set('')
        self.svIMC.set('')
        self.svTelefono.set('')
        self.svAntecedentes.set('')

        self.entryNombre.configure(state='normal')
        self.entryApellidos.configure(state='normal')
        self.entryDNI.configure(state='normal')
        self.entryEdad.configure(state='normal')
        self.entryPeso.configure(state='normal')
        self.entryTalla.configure(state='normal')
        self.entryIMC.configure(state='normal')
        self.entryTelefono.configure(state='normal')
        self.entryAntecedentes.configure(state='normal')

        self.btnGuardar.configure(state='normal')
        self.btnCancelar.configure(state='normal')

    def deshabilitar(self):
        self.idPersona = None
        self.svNombre.set('')
        self.svApellidos.set('')
        self.svDNI.set('')
        self.svEdad.set('')
        self.svPeso.set('')
        self.svTalla.set('')
        self.svIMC.set('')
        self.svTelefono.set('')
        self.svAntecedentes.set('')

        self.entryNombre.configure(state='disabled')
        self.entryApellidos.configure(state='disabled')
        self.entryDNI.configure(state='disabled')
        self.entryEdad.configure(state='disabled')
        self.entryPeso.configure(state='disabled')
        self.entryTalla.configure(state='disabled')
        self.entryIMC.configure(state='disabled')
        self.entryTelefono.configure(state='disabled')
        self.entryAntecedentes.configure(state='disabled')

    def tablaPaciente(self, where=""):
        if len(where) > 0:
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = listar()

        self.tabla = ttk.Treeview(self, column=('Nombre', 'Apellidos', 'Dni', 'Edad', 'Peso', 'Talla', 'IMC', 'Telefono', 'Antecedentes'))
        self.tabla.grid(column=0, row=10, columnspan=10, sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=10, column=11, sticky='nse')

        self.tabla.configure(yscrollcommand=self.scroll.set)

        # Configurar colores de la tabla
        self.tabla.tag_configure('evenrow', background='#2B2B2B', foreground='white')
        self.tabla.tag_configure('oddrow', background='#1F1F1F', foreground='white')

        # Encabezados de la tabla
        self.tabla.heading('#0', text='ID', anchor=W)
        self.tabla.heading('#1', text='Nombre', anchor=W)
        self.tabla.heading('#2', text='Apellidos', anchor=W)
        self.tabla.heading('#3', text='DNI', anchor=W)
        self.tabla.heading('#4', text='Edad', anchor=W)
        self.tabla.heading('#5', text='Peso', anchor=W)
        self.tabla.heading('#6', text='Talla', anchor=W)
        self.tabla.heading('#7', text='IMC', anchor=W)
        self.tabla.heading('#8', text='Telefono', anchor=W)
        self.tabla.heading('#9', text='Antecedentes', anchor=W)

        # Definir el ancho de las columnas
        self.tabla.column("#0", anchor=W, width=50)    # ID
        self.tabla.column("#1", anchor=W, width=150)   # Nombre
        self.tabla.column("#2", anchor=W, width=150)   # Apellidos
        self.tabla.column("#3", anchor=W, width=100)   # DNI
        self.tabla.column("#4", anchor=W, width=50)    # Edad
        self.tabla.column("#5", anchor=W, width=70)    # Peso
        self.tabla.column("#6", anchor=W, width=70)    # Talla
        self.tabla.column("#7", anchor=W, width=70)    # IMC
        self.tabla.column("#8", anchor=W, width=120)   # Teléfono
        self.tabla.column("#9", anchor=W, width=300)   # Antecedentes

    # Insertar datos en la tabla
        for index, p in enumerate(self.listaPersona):
            tag = 'evenrow' if index % 2 == 0 else 'oddrow'  # Alternar filas
            self.tabla.insert('', 'end', text=p[0], values=(p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]), tags=(tag,))

    # Configuración de botones
        button_color = "#800080"  # Color púrpura
        self.btnEditarPaciente = ctk.CTkButton(self, text="EDITAR", fg_color=button_color, command=self.editarPaciente)
        self.btnEditarPaciente.configure(font=('Arial', 16, 'bold'))
        self.btnEditarPaciente.grid(row=11, column=0, padx=10, pady=5, sticky='w', columnspan=2)

        self.btnEliminarPaciente = ctk.CTkButton(self, text="ELIMINAR", fg_color=button_color, command=self.eliminarDatoPaciente)
        self.btnEliminarPaciente.configure(font=('Arial', 16, 'bold'))
        self.btnEliminarPaciente.grid(column=1, row=11, padx=10, pady=5, sticky="w", columnspan=2)

        self.btnHistorialPaciente = ctk.CTkButton(self, text='HISTORIAL', fg_color=button_color)
        self.btnHistorialPaciente.configure(font=('Arial', 16, 'bold'))
        self.btnHistorialPaciente.grid(row=11, column=2, padx=10, pady=5, sticky='w', columnspan=2)

        self.btnSalir = ctk.CTkButton(self, text='SALIR', command=self.root.destroy, fg_color=button_color)
        self.btnSalir.configure(font=('Arial', 16, 'bold'))
        self.btnSalir.grid(row=11, column=3, padx=10, pady=5, sticky='w', columnspan=2)

    def guardarPaciente(self):
        persona = Persona(
            self.svNombre.get(), self.svApellidos.get(), self.svDNI.get(),
            self.svEdad.get(), self.svPeso.get(), self.svTalla.get(), self.svPeso.get(),
            self.svTelefono.get(), self.svAntecedentes.get()
        )

        if self.idPersona == None:
            guardarDatoPaciente(persona)
        else:
            editarDatoPaciente(persona, self.idPersona)

    
    def editarPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text'] #Trae el ID
            self.nombrePaciente = self.tabla.item(self.tabla.selection())['values'][0]
            self.apellidosPaciente = self.tabla.item(self.tabla.selection())['values'][1]
            self.dniPaciente = self.tabla.item(self.tabla.selection())['values'][2]
            self.edadPaciente = self.tabla.item(self.tabla.selection())['values'][3]
            self.pesoPaciente = self.tabla.item(self.tabla.selection())['values'][4]
            self.tallaPaciente = self.tabla.item(self.tabla.selection())['values'][5]
            self.imcPaciente = self.tabla.item(self.tabla.selection())['values'][6]
            self.telefonoPaciente = self.tabla.item(self.tabla.selection())['values'][7]
            self.antecedentesPaciente = self.tabla.item(self.tabla.selection())['values'][8]

            self.habilitar()

            self.entryNombre.insert(0, self.nombrePaciente)
            self.entryApellidos.insert(0, self.apellidosPaciente)
            self.entryDNI.insert(0, self.dniPaciente)
            self.entryEdad.insert(0, self.edadPaciente)
            self.entryPeso.insert(0, self.pesoPaciente)
            self.entryTalla.insert(0,self.tallaPaciente)
            self.entryIMC.insert(0,self.imcPaciente)
            self.entryTelefono.insert(0,self.telefonoPaciente)
            self.entryAntecedentes.insert(0,self.antecedentesPaciente)
        except:
            title = 'Editar Paciente'
            mensaje = 'Error al editar paciente'
            messagebox.showerror(title, mensaje)
    
    def eliminarDatoPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text']
            eliminarPaciente(self.idPersona)
            
            self.tablaPaciente()
            self.idPersona = None
        except:
            title = 'Eliminar Paciente'
            mensaje = 'No se pudo eliminar paciente'
            messagebox.showinfo(title, mensaje)

        
        self.deshabilitar()
        self.tablaPaciente()

