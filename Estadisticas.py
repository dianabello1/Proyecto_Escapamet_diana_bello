class Estadisticas():
    def __init__(self, usuario, tiempo, score, record, dificultad, cuartos_mas_visitados, usuarios_frecuentes, grafico ):
        self.usuario = usuario 
        self.tiempo = tiempo 
        self.score = score 
        self.record = record 
        self.dificultad = dificultad 
        self.cuartos_mas_visitados = cuartos_mas_visitados
        self.usuarios_frecuentes = usuarios_frecuentes
        self.grafico = grafico 

    def top_5(self):
        print(f"El mejor tiempo fue de {self.tiempo} \n En la dificultad {self.dificultad}")

    