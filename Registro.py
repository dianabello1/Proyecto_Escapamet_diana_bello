class Registro():
    # Constructor
    def __init__(self, username, password, edad, avatar ):
        #Atributos
        self.username  = username
        self.password = password
        self.edad = edad
        self.avatar = avatar 


    # Procedimientos y métodos de clase  
    def mostrar_datos_usuario(self, username, password):
        print(f'''
        usuario: {self.username}
        password: {self.password}
        ''')

    def mostrar_jugador(self):
        print(f'Username: {self.username} \nPassword: {self.password} \nEdad: {self.avatar} ')
