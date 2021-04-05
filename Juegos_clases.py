import random   

class Mini_juegos():
    #Constructor 
    def __init__(self, respuestas, award, requerimiento, reglas, pistas): #Atributos 
       
        self.respuestas = respuestas
        self.award = award
        self.requerimiento = requerimiento
        self.reglas = reglas
        self.pistas = pistas
    # Metodos de la clase 

class Adivinanzas(Mini_juegos):
    def __init__(self, respuestas, award, requerimiento, pistas, reglas, tablero):
        Mini_juegos.__init__(self, respuestas, pistas, reglas, requerimiento, award)
        self.tablero = tablero 

class Ahorcado():
    def __init__(self, respuestas, award, requerimiento, pistas, reglas, tablero):
        pass
     
class sopa_de_letras():
    def __init__(self, respuestas, award, requerimiento, pistas, reglas, tablero):
        pass

class Encuentra_la_logica():
    def __init__(self, respuestas, award, requerimiento, pistas, reglas, tablero):
        pass

class Preguntas_sobre_python():
   def __init__(self, respuestas, award, requerimiento, pistas, reglas, tablero):
       pass

class Preguntas_de_matematicas():
   def __init__(self, respuestas, award, requerimiento, pistas, reglas, tablero):
       pass

class Criptograma():
    pass

class Quizizz_cultura_unimetana():
   pass

class Memoria_con_emojis():
   def __init__(self, respuestas, award, requerimiento, pistas, reglas, tablero):
       pass

class Logica_buleana():
    def __init__(self, respuestas, award, requerimiento, pistas, reglas, tablero):
        pass

class Palabra_mezcla():
    def __init__(self, respuestas, award, requerimiento, pistas, reglas, tablero):
        pass

class Escoge_un_numero_entre():
    def __init__(self, respuestas, award, requerimiento, pistas, reglas, tablero):
        pass

class Final_boss():
