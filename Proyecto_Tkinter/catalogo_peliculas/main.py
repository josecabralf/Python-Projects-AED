import tkinter as tk
from client.gui_app import Frame, barra_menu

def main():
  # Crear ventana (raíz) de donde se exe el programa:
  root = tk.Tk()
  
  # .title: cambia titulo de la ventana:
  root.title('Catálogo de Películas')
  # .iconbitmap: cambia el ícono de la ventana
  root.iconbitmap('img/icono.ico')
  
  # .resizable(x,y): si x==0, no se puede modificar ancho de ventana. Si y==0 no se puede modificar altura. Con x,y==1 se habilita.
  root.resizable(0,0)
  
  # Barra de menu:
  barra_menu(root)
  
  # Crear Frame:
  app = Frame(root=root)
  
  # Para mantener ventana abierta
  app.mainloop()

if __name__ == "__main__":
  main()