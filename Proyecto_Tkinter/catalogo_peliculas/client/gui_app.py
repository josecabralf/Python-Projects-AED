import tkinter as tk
from tkinter import ttk, messagebox
from model.pelicula_dao import crear_tabla, borrar_tabla
from model.pelicula_dao import Pelicula, guardar, listar, editar, eliminar

# Crear un frame: para permitir cajas adentro de ventana
class Frame(tk.Frame):
  def __init__(self,root=None):
    super().__init__(root, width=480,height=320)
    self.root = root
    
    # .pack: empaqueta la ventana == ventana toma el tamaño del frame
    self.pack()
    
    self.id_pelicula = None
    """
    .config: permite configurar características del frame
    width y height: para tamaño de ventana.
    bg: color de fondo
    """
    #self.config(bg='white')
    self.campos_peliculas()
    self.deshabilitar_campos()
    self.tabla_peliculas()
    
  # Labels del frame:
  def campos_peliculas(self):
    self.label_nombre = tk.Label(self, text='Nombre: ')
    # Configurar:
    self.label_nombre.config(font=('Arial', 12, 'bold'))
    self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
    
    self.label_duration = tk.Label(self, text='Duración: ')
    self.label_duration.config(font=('Arial', 12, 'bold'))
    self.label_duration.grid(row=1, column=0, padx=10, pady=10)
    
    self.label_genre = tk.Label(self, text='Género: ')
    self.label_genre.config(font=('Arial', 12, 'bold'))
    self.label_genre.grid(row=2, column=0, padx=10, pady=10)
    
    
    # Entrys de cada campo:
    self.my_name = tk.StringVar()
    self.entry_name = tk.Entry(self, textvariable=self.my_name)
    self.entry_name.config(width=50, font=('Arial', 12))
    self.entry_name.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
    
    self.my_duration = tk.StringVar()
    self.entry_duration = tk.Entry(self,textvariable=self.my_duration)
    self.entry_duration.config(width=50, font=('Arial', 12))  
    self.entry_duration.grid(row=1, column=1, padx=10, pady=10, columnspan=2)    

    self.my_genre = tk.StringVar()
    self.entry_genre = tk.Entry(self, textvariable=self.my_genre)
    self.entry_genre.config(width=50, font=('Arial', 12))
    self.entry_genre.grid(row=2, column=1, padx=10, pady=10, columnspan=2)
  
    # Botones
    self.boton_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
    self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg= '#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
    self.boton_nuevo.grid(row=3, column=0)
    
    self.boton_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
    self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'), fg= '#DAD5D6', bg='#1658A2', cursor='hand2', activebackground='#3586DF')
    self.boton_guardar.grid(row=3, column=1)
    
    self.boton_cancel = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
    self.boton_cancel.config(width=20, font=('Arial', 12, 'bold'), fg= '#DAD5D6', bg='#BD152E', cursor='hand2', activebackground='#E15370')
    self.boton_cancel.grid(row=3, column=2)

  def vaciar_campos(self):
    self.my_name.set('')
    self.my_duration.set('')
    self.my_genre.set('')

  def habilitar_campos(self):
    self.vaciar_campos()
    
    self.entry_name.config(state='normal')
    self.entry_duration.config(state='normal')
    self.entry_genre.config(state='normal')
      
    self.boton_guardar.config(state='normal')
    self.boton_cancel.config(state='normal')
    
  def deshabilitar_campos(self):
    self.vaciar_campos()
    
    self.entry_name.config(state='disable')
    self.entry_duration.config(state='disable')
    self.entry_genre.config(state='disable')
      
    self.boton_guardar.config(state='disable')
    self.boton_cancel.config(state='disable')

  def guardar_datos(self):
    pelicula = Pelicula(
      self.my_name.get(),
      self.my_duration.get(),
      self.my_genre.get()
    )
    
    if self.id_pelicula == None: 
      guardar(pelicula)
    else:
      editar(pelicula, self.id_pelicula)
      self.id_pelicula = None
    
    self.tabla_peliculas()
    
    self.deshabilitar_campos()
  
  # Crear tabla de registros
  def tabla_peliculas(self):
    # Recuperar la lista de peliculas
    self.lista_p = listar()
    self.lista_p.reverse()
    
    self.tabla = ttk.Treeview(self, columns=('Nombre', 'Duración', 'Género'))
    self.tabla.grid(row=4, column=0, columnspan=4, sticky='nse')
    
    # Scrollbar:
    self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
    self.scroll.grid(row=4, column=4, sticky='nse')
    self.tabla.configure(yscrollcommand=self.scroll.set)

    self.tabla.heading('#0', text='ID')
    self.tabla.heading('#1', text='NOMBRE')
    self.tabla.heading('#2', text='DURACIÓN')
    self.tabla.heading('#3', text='GÉNERO')
    
    # Iterar lista de peliculas:
    for p in self.lista_p:
    # Insert: agrega registros
    # '',0 es la base
      self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3]))
    
    self.boton_editar = tk.Button(self, text='Editar', command=self.editar_datos)
    self.boton_editar.config(width=20, font=('Arial', 12, 'bold'), fg= '#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
    self.boton_editar.grid(row=5, column=0)
    
    self.boton_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_datos)
    self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'), fg= '#DAD5D6', bg='#BD152E', cursor='hand2', activebackground='#E15370')
    self.boton_eliminar.grid(row=5, column=1)

  def editar_datos(self):
    try:
      self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
      self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
      self.duracion_pelicula = self.tabla.item(self.tabla.selection())['values'][1]
      self.genero_pelicula = self.tabla.item(self.tabla.selection())['values'][2]
      
      self.habilitar_campos()
      self.entry_name.insert(0, self.nombre_pelicula)
      self.entry_duration.insert(0, self.duracion_pelicula)
      self.entry_genre.insert(0, self.genero_pelicula)
      
    except:
      titulo = 'Edición de Datos'
      msj = 'No se ha seleccionado ningún registro'
      messagebox.showerror(titulo,msj)
  
  def eliminar_datos(self):
    try:
      self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
      eliminar(self.id_pelicula)
      
      self.tabla_peliculas()
      self.id_pelicula = None
    except:
      titulo = 'Eliminar Datos'
      msj = 'No ha seleccionado ningún registro'
      messagebox.showwarning(titulo, msj)
#  Barra de menu
def barra_menu(root):
  # Crear barra de menú de opciones
  
  # Se ancla al root
  barra_menu = tk.Menu(root)
  root.config(menu=barra_menu, width=300, height=300)
  
  # Crear un elemento del menu: 'Inicio'
  # Se ancla a la barra de menu
  menu_inicio = tk.Menu(barra_menu, tearoff=0)
  barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
  
  # Funciones Menu de 'Inicio'
  # command: indica qué hará al oprimir la opción
  menu_inicio.add_command(label='Crear Registro en DB', command=crear_tabla)
  menu_inicio.add_command(label='Eliminar Registro en DB', command=borrar_tabla)
  menu_inicio.add_command(label='Salir', command = root.destroy)
  
  # Otros menus:
  menu_consultas = tk.Menu(barra_menu, tearoff=0)
  barra_menu.add_cascade(label='Consultas', menu=menu_consultas)
  
  menu_config = tk.Menu(barra_menu, tearoff=0)
  barra_menu.add_cascade(label='Configuración', menu=menu_config)
  
  menu_help = tk.Menu(barra_menu, tearoff=0)
  barra_menu.add_cascade(label='Ayuda', menu=menu_help)
