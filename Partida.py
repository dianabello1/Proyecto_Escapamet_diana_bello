class Partida():
    # Constructor 
    def __init__(self, nombre, avatar, vida, tiempo, score, ganar, pistas, dificultad):
        #Atributos 
        self.nombre = nombre
        self.avatar = avatar
        self.vida = vida 
        self.tiempo = tiempo 
        self.score = score
        self.ganar = ganar  
        self.dificultad = dificultad
        self.pistas = pistas

# Procedimientos y metodos de clase 
    def partida_facil(self):
        self.vida = 5 
        self.pistas = 5
        print(f'Tienes {self.vida} vidas')
        print(f'Tienes {self.pistas} pistas')
        if self.vida == 0:
            print('GAME OVER')

    def partida_medio(self):
        self.vida = 3
        self.pistas = 3
        print(f' Tienes { self.vida} Vidas ')
        print(f' Tienes {self.pistas} Pistas')
        if self.vida == 0:
            print('GAME OVER')

    def partida_dificil(self):
        self.vida = 1
        self.pistas = 2 
        print(f' Tienes {self.vida} Vidas ')
        print(f' Tienes {self.pistas} Pistas')
        if self.vida == 0:
            print('GAME OVER')

    