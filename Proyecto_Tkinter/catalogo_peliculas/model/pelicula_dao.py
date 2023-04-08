from .conexion_db import ConexionDB
from tkinter import messagebox

# Crear tabla
def crear_tabla():
  conexion = ConexionDB()
  
  # Usar SQL para crear una base de datos:
  sql = '''
  CREATE TABLE peliculas(
    id_pelicula INTEGER,
    nombre VARCHAR(100),
    duracion VARCHAR(10),
    genero VARCHAR(100),
    PRIMARY KEY(id_pelicula AUTOINCREMENT)
  )
  '''
  try:
    conexion.cursor.execute(sql)
    conexion.cerrar()
    titulo = 'Crear Registro'
    msj = 'Se creo la tabla en la DB'
    messagebox.showinfo(titulo, msj)
  except:
    titulo = 'Crear Registro'
    msj = 'La tabla ya está creada'
    messagebox.showwarning(titulo, msj)
  
# Borrar tabla
def borrar_tabla():
  conexion = ConexionDB()
  
  sql = 'DROP TABLE peliculas'
  
  try:
    conexion.cursor.execute(sql)
    conexion.cerrar()
    titulo = 'Borrar Registro'
    msj = 'La tabla en la DB se borró con éxito'
    messagebox.showinfo(titulo, msj)
  except:
    titulo = 'Borrar Registro'
    msj = 'No hay tabla para borrar'
    messagebox.showerror(titulo, msj)
    
class Pelicula:
  def __init__(self, name, dur, gen):
    self.id = None
    self.name = name
    self.dur = dur
    self.gen = gen
  
  def __str__(self) -> str:
    return f'Película[{self.name}, {self.dur}, {self.gen}]'
  
def guardar(pelicula):
  conexion = ConexionDB()
  
  sql = f"""INSERT INTO peliculas (nombre, duracion, genero)
  VALUES('{pelicula.name}', '{pelicula.dur}', '{pelicula.gen}')"""
  
  try:
    conexion.cursor.execute(sql)
    conexion.cerrar()
  except:
    titulo = 'Conexión al Registro'
    msj = 'La tabla películas no está creada en la DB'
    messagebox.showerror(titulo, msj)

def listar():
  conexion = ConexionDB()
  lista_p = []
  sql = 'SELECT * FROM peliculas'
  
  try:
    conexion.cursor.execute(sql)
    lista_p = conexion.cursor.fetchall()
    conexion.cerrar()
  except:
    titulo = 'Conexión al Registro'
    msj = 'Crea la tabla en la DB'
    messagebox.showwarning(titulo, msj)
    
  return lista_p

def editar(pelicula, id_pelicula):
  conexion = ConexionDB()
  
  sql = f"""UPDATE peliculas
  SET nombre = '{pelicula.name}', duracion = '{pelicula.dur}', genero = '{pelicula.gen}'
  WHERE id_pelicula = {id_pelicula}"""
  
  try:
    conexion.cursor.execute(sql)
    conexion.cerrar()
  except:
    titulo = 'Edición de Datos'
    msj = 'No se ha podido editar este registro'
    messagebox.showwarning(titulo, msj)
    
def eliminar(id_pelicula):
  conexion = ConexionDB()
  sql = f'DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}'
  
  try:
    conexion.cursor.execute(sql)
    conexion.cerrar()
  except:
    titulo = 'Eliminar Datos'
    msj = 'No se ha podido eliminar este registro'
    messagebox.showwarning(titulo, msj)  