import _sqlite3

class ConexionDB:
  def __init__(self):
    # Busca el archivo. Si lo encuentra lo abre, sino lo crea
    self.base_datos = 'database/peliculas.db'
    # Abrir conexión
    self.conexion = _sqlite3.connect(self.base_datos)
    # Puntero de la base de datos
    self.cursor = self.conexion.cursor()
    
  def cerrar(self):
    # Realizar combios dentro de DB
    self.conexion.commit()
    # Cerrar archivo
    self.conexion.close()