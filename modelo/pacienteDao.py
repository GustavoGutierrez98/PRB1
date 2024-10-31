from .conexion import ConexionDB
from tkinter import messagebox

def editarDatoPaciente(persona, idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET nombre = '{persona.nombre}', apellidos = '{persona.apellidos}',
            dni = '{persona.dni}', edad = '{persona.edad}', peso = '{persona.peso}',
            talla = {persona.talla}, imc = '{persona.imc}', telefono = '{persona.telefono}', antecedentes = '{persona.antecedentes}', activo = 1 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Paciente'
        mensaje = 'Paciente Editado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Editar Paciente'
        mensaje = 'Error al editar paciente'
        messagebox.showinfo(title, mensaje)


def guardarDatoPaciente(persona):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Persona (nombre, apellidos, dni,
            edad, peso, talla, imc, telefono, antecedentes, activo) VALUES
            ('{persona.nombre}','{persona.apellidos}','{persona.dni}',
            '{persona.edad}','{persona.peso}',{persona.talla},'{persona.imc}',
            '{persona.telefono}','{persona.antecedentes}',1)"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Paciente'
        mensaje = 'Paciente Registrado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registrar Paciente'
        mensaje = 'Error al registrar paciente'
        messagebox.showerror(title,mensaje)


def listar():
    conexion = ConexionDB()

    listaPersona = []
    sql = 'SELECT * FROM Persona WHERE activo = 1'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Registros no existen'
        messagebox.showwarning(title, mensaje)
    return listaPersona


def listarCondicion(where):
    conexion = ConexionDB()
    listaPersona = []
    sql = f'SELECT * FROM Persona {where}'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Registros no existen'
        messagebox.showwarning(title, mensaje)
    return listaPersona


def eliminarPaciente(idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET activo = 0 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Paciente'
        mensaje = 'Paciente eliminado exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Paciente'
        mensaje = 'Error al eliminar Paciente'
        messagebox.showwarning(title, mensaje)


class Persona:
    def __init__(self, nombre, apellidos, dni, edad, peso, talla, imc, telefono, antecedentes):
        self.idPersona = None
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.edad = edad
        self.peso=peso
        self.talla=talla
        self.imc=imc
        self.telefono = telefono
        self.antecedentes = antecedentes        

    def __str__(self):
        return f'Persona[{self.nombre},{self.apellidos}, {self.dni}, {self.edad},{self.peso},{self.talla},{self.imc},{self.telefono},{self.antecedentes}]'