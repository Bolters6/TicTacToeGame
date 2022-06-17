from tkinter import *
from PIL import ImageTk

class Gato:
    def __init__(self, root):
        self.root = root
        self.inicio()
    
    def inicio(self):
        self.root.title("Juego del Gato")
        self.marcoinicio = Frame(self.root)
        self.marcoinicio.grid()
        
        imagen = ImageTk.PhotoImage(file = "C:/Users/Jessica/Downloads/lol.jpg")
        bienvenida = Label(self.marcoinicio, image = imagen)
        bienvenida.grid(row = 0, column = 0)
        bienvenida.image = imagen
        
        nuevapartida = Button(self.marcoinicio, text = "Nueva Partida", font = ('Times', '10', 'italic'), fg = 'blue', bg = 'white', 
                              command = lambda:self.cambiarpantalla('a'), anchor = 'w').grid(row = 1, column = 0, sticky = 'ew')
        
        records = Button(self.marcoinicio, text = "Records", font = ('Times', '10', 'italic'), fg ='blue', bg = 'white', anchor = 'w',
                         command = self.btnrecords).grid(row = 2, column = 0, sticky = 'ew')
                         
        salir = Button(self.marcoinicio, text = 'Salir', font = ('Times', '10', 'italic'), command = self.root.quit(), anchor = 'w').grid(row = 3,
                                                                                                                                          column = 0,
                                                                                                                                      sticky = 'ew')
                       
        
    def datos(self):
        self.root.title("Jugadores")
        self.marconombres = Frame(self.root)
        self.marconombres.grid()
        
        jugador1 = Label(self.marconombres, text = "Jugador 1", font = ('Times', '12', 'Italic'), fg ='blue', bg = 'white').grid(row = 0, column = 0)
        jugador2 = Label(self.marconombres, text = "Jugador 2", font = ('Times', '12', 'Italic'), fg ='blue', bg = 'white').grid(row = 1, column = 0)
        
        nombre1 = Entry(self.marconombres, width = 40, textvariable = self.jug1)
        nombre1.grid(row = 0, column = 1, sticky = 'nsew')
        nombre2 = Entry(self.marconombres, width = 40, textvariable = self.jug2)
        nombre2.grid(row = 1, column = 1, sticky = 'nsew')
        
        comenzar = Button(self.marconombres, text = "Comenzar", font = ('Times', '10', 'Italic'), fg = 'blue', bg = 'white', 
                              command = lambda:self.cambiarpantalla('b'), anchor = 'w').grid(row = 2, column = 0, sticky = 'ew', colummnspan = 2)
        
        regresar = Button(self.marconombres, text = "Regresar", font = ('Times', '10', 'Italic'), fg = 'blue', bg = 'white', 
                              command = lambda:self.cambiarpantalla('c'), anchor = 'w').grid(row = 3, column = 0, sticky = 'ew', columnspan = 2)
    
        salir = Button(self.marconombres, text = "Salir", font = ('Times', '10', 'Italic'), fg = 'blue', bg = 'white', 
                              command = lambda:self.root.quit(), anchor = 'w').grid(row = 4, column = 0, sticky = 'ew', columnspan = 2)
    
    
    
    def partida(self):
        
        self.root.title('Partida')
        self.marcopartida = Frame(self.root)
        self.marcopartida.grid()
        
        self.casillas = []
        k = 0
        for i in range(3):
            for j in range(3):
                self.casillas.append(Button(self.marcopartida, font = ("Times", "50", "Italic"), fg = "blue", bg = "white",
                                            bd = 1, width = 5, command = lambda e = k:self.mostrarcasilla(e)))
                self.casillas[k].grid(row = i, column = j)
                k += 1
        
        jugaragain = Button(self.marcopartida, text = "Jugar De Nuevo", font = ("Times", "10", "Italic"), fg = "blue",
                            bg = "white", command = lambda:self.cambiarpantalla('d'), anchor = 'w').grid(row = 4, column = 0, sticky = 'ew',
                                                                                                         columnspan = 3)
        salir = Button(self.marconombres, text = "Salir", font = ('Times', '10', 'Italic'), fg = 'blue', bg = 'white', 
                              command = lambda:self.root.quit(), anchor = 'w').grid(row = 5, column = 0, sticky = 'ew', columnspan = 3)
                    
                      
                
root = Tk()
juegogato = Gato(root)
root.mainloop()
        