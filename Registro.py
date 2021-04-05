class Registro():
    # Constructor
    def __init__(self, username, password, edad, avatar ):
        #Atributos
        self.username  = username
        self.password = password
        self.edad = edad
        self.avatar = avatar 

    # Procedimientos y métodos de clase     
    def mostrar_jugador(self):
        print(f'Username: {self.username} \nPassword: {self.password} \nEdad: {self.avatar} ')

    def mostrar_nombre(self):
        pass