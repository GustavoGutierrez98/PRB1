from .conexion import ConexionDB
from tkinter import messagebox

def listarHistoria(idPersona):
    conexion = ConexionDB()
    sql = f'SELECT h.idHistoriaMedica, p.nombre || " " || p.apellidos AS Apellidos, h.fechaHistoria, h.motivo, h.fc, h.fr, h.ta, h.peso, h.talla, h.imc, h.ant_pat, h.ant_nopat, h.ant_ginec, h.imp_diag, h.tratamiento, h.detalle FROM historiaMedica h INNER JOIN Persona p ON p.idPersona = h.idPersona WHERE p.idPersona = {idPersona}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title='Registro Historia Medica'
        mensaje='Historia registrada exitosamente'
    except:
        title = 'LISTAR HISTORIA'
        mensaje = 'Error al listar historia medica'
        messagebox.showerror(title, mensaje)

def guardarHistoria(idPersona, fechaHistoria, motivo, fc, fr, ta, peso, talla, imc, ant_pat, ant_nopat, ant_ginec, imp_diag, tratamiento, detalle):
    conexion = ConexionDB()
    sql = f"""INSERT INTO historiaMedica (idPersona, fechaHistoria, motivo, fc, fr, ta, peso, talla, imc, ant_pat, ant_nopat, ant_ginec, imp_diag, tratamiento, detalle) VALUES
            ({idPersona},'{fechaHistoria}','{motivo}', {fc}, {fr}, '{ta}', {peso}, {talla}, {imc}, '{ant_pat}', '{ant_nopat}', '{ant_ginec}', '{imp_diag}', '{tratamiento}', '{detalle}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registro Historia Medica'
        mensaje = 'Historia registrada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registro Historia Medica'
        mensaje = 'Error al registrar historia'
        messagebox.showerror(title, mensaje)

def eliminarHistoria(idHistoriaMedica):
    conexion = ConexionDB()
    sql = f'DELETE FROM historiaMedica WHERE idHistoriaMedica = {idHistoriaMedica}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Historia'
        mensaje = 'Historia medica eliminada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Historia'
        mensaje = 'Error al eliminar historia medica'
        messagebox.showerror(title, mensaje)

def editarHistoria(fechaHistoria, motivo, fc, fr, ta, peso, talla, imc, ant_pat, ant_nopat, ant_ginec, imp_diag, tratamiento, detalle, idHistoriaMedica):
    conexion = ConexionDB()
    sql = f"""UPDATE historiaMedica SET fechaHistoria = '{fechaHistoria}', motivo = '{motivo}', fc = {fc}, fr = {fr}, ta = '{ta}', peso = {peso}, talla = {talla}, imc = {imc}, ant_pat = '{ant_pat}', ant_nopat = '{ant_nopat}', ant_ginec = '{ant_ginec}', imp_diag = '{imp_diag}', tratamiento = '{tratamiento}', detalle = '{detalle}' WHERE idHistoriaMedica = {idHistoriaMedica}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Historia'
        mensaje = 'Historia medica editada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Editar Historia'
        mensaje = 'Error al editar historia medica'
        messagebox.showerror(title, mensaje)

class historiaMedica:
    def __init__(self, idPersona, fechaHistoria, motivo, fc, fr, ta, peso, talla, imc, ant_pat, ant_nopat, ant_ginec, imp_diag, tratamiento, detalle):
        self.idHistoriaMedica = None
        self.idPersona = idPersona
        self.fechaHistoria = fechaHistoria
        self.motivo = motivo
        self.fc = fc
        self.fr = fr
        self.ta = ta
        self.peso = peso
        self.talla = talla
        self.imc = imc
        self.ant_pat = ant_pat
        self.ant_nopat = ant_nopat
        self.ant_ginec = ant_ginec
        self.imp_diag = imp_diag
        self.tratamiento = tratamiento
        self.detalle = detalle
    
    def __str__(self):
        return f'historiaMedica[{self.idPersona}, {self.fechaHistoria}, {self.motivo}, {self.fc}, {self.fr}, {self.ta}, {self.peso}, {self.talla}, {self.imc}, {self.ant_pat}, {self.ant_nopat}, {self.ant_ginec}, {self.imp_diag}, {self.tratamiento}, {self.detalle}]'
