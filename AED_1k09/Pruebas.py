__author__ = 'Cátedra de AED'

from tkinter import *


def bars(canvas):
    canvas.create_rectangle((100, 120, 130, 200), outline='blue')
    canvas.create_rectangle((130, 85, 160, 200), outline='red')
    canvas.create_rectangle((161, 160, 190, 200), outline='yellow')
    canvas.create_rectangle((190, 100, 220, 200), outline='lime')
    canvas.create_line((70, 200, 250, 200), fill='black')


def render():
    # configuracion inicial de la ventana principal...
    root = Tk()
    root.title('Cuestionario')

    # calculo de resolucion en pixels de la pantalla...
    maxw = root.winfo_screenwidth()
    maxh = root.winfo_screenheight()

    # ajuste de las dimensiones y coordenadas de arranque de la ventana...
    root.geometry("%dx%d+%d+%d" % (maxw, maxh, 0, 0))

    # un lienzo de dibujo dentro de la ventana...
    canvas = Canvas(root, bg='white', width=maxw, height=maxh)
    canvas.grid(column=0, row=0)

    # desarrollar la gráfica...
    bars(canvas)

    # lanzar el ciclo principal de control de eventos de la ventana...
    root.mainloop()


if __name__ == '__main__':
    render()
