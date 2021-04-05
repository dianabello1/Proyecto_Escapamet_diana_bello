from colored import fg, bg, attr, fore
import pickle
import os

from Registro import Registro

# Funcón que recibe los datos del archivo txt
def recibir_datos_del_txt(usuario_txt, registro_usuarios):

    lectura_binaria = open(usuario_txt,'rb')

    if os.stat(usuario_txt).st_size != 0:
        registro_usuarios = pickle.load(lectura_binaria)

    lectura_binaria.close()

    return registro_usuarios

# Funcíon que carga los datos al archivo txt
def escribir_datos_en_txt(usuario_txt, registro_usuarios):

    escritura_binaria = open(usuario_txt,'wb')

    registro_usuarios = pickle.dump(registro_usuarios, escritura_binaria)

    escritura_binaria.close()

#Modulo 1 : Registro del Jugador
def registro(usuarios_list):
    #caracteres = ['#', '$', '%', '!', '-', '+', '/', '=']

    username =  input(' Ingrese un nombre para su Usuario: ')
    edad = int(input(' Ingrese su edad: '))
    print(' ')
    print(fg('red') + ' Su contraseña debe contener: ')
    print(fg('white') + '''
     - Mínimo 8 caracteres.
     - Debe contener al menos un número. 
     - Debe contener al menos una letra.
     - Debe contener al menos un caracter especial. 
     ''')
    password = input(fg('red') + 'Ingrese su Contraseña AQUI: >>  ')

     # Validar contraseña
    while True: 
        if len(password) < 7:
            print(fg('red') + '-- Su contraseña tiene que ser mayor a 8 caracteres --')
            password = input(fg('white') +'Ingrese nuevamente su contraseña: ')
        elif password.isalpha():
            print(fg('red') + 'Contraseña invalida')
            password = input(fg('white') +'Ingrese nuevamente su contraseña: ')
        elif password.isnumeric():
            print(fg('red') + 'Contraceña invalida')
            password = input(fg('white') + 'Ingrese nuevamente su contraseña: ')
        else:
            print(fg('green') + " ------------------------------------------------- ")
            print(fg('green') + "  SU CONTRASEÑA HA SIDO RESGISTRADA EXITOSAMENTE ")
            print(fg('green') + " ------------------------------------------------- ")
            break
    print(fg('red') + 'Elija un avatar' )
    avatar = input(fg('white') + ''' 
     1. Scharifker
     2. Eugenio Mendoza
     3. Pelusa
     4. Gandhi
     5. Otro que desee agregar 
     >>> ''')

    #Validar Avatares y agregar nuevos 
    while (not  avatar.isnumeric()) or (int(avatar) not in range(1,6)):
        print("-- Ingrese una opcion válida  --")
    new_avatar = []

    if avatar == "1":
        print(' ')
        print("Tu avatar es Scharifker")
        print(' ')
    elif avatar == "2":
        print(' ')
        print("Tu avatar es Eugenio Mendoza")
        print(' ')
    elif avatar == "3":
        print(' ')
        print(" Tu avatar es Pelusa")
        print(' ')
    elif avatar == "4":
        print(' ')
        print("Tu avatar es Gandhi")
        print(' ')
    else: 
        avatar = input(fg('red') + 'Ingrese el nombre del nuevo avatar: ')
        if avatar.isnumeric():
            print("Avatar invalido, porfavor ingrese solo letras")
            avatar = input(fg('red') + 'Ingrese nuevamente el nombre de su avatar: ')
        
        print(fg('green') + " ---------------------------------------- ")
        print(fg('green') + "  SU AVATAR SE HA CREADO EXITOSAMENTE ")
        print(fg('green') + " ----------------------------------------- ")
        
    new_avatar.append(avatar)   
    
    nuevo_usuario = Registro(username, password, edad, avatar)
    usuarios_list.append(nuevo_usuario)
    print(fg('green') + " ----------------------------------------------")
    print(fg('green') + "  SU USUARIO HA SIDO RESGISTRADO EXITOSAMENTE ")
    print(fg('green') + " ----------------------------------------------- ")

    return usuarios_list

# Confirmas que el ususario ha sido creado y guardado 
def confirmar_usuario(usuarios_list):
    usuario = input(fg('white') +  'Ingrese su Usuario: ')
    if usuario in usuarios_list:
        password = input(fg('white') +  'Ingrese su contraseña: ')
        if len(password)<8:
            print(fg('red') +  'Su contraseña debe ser de minimo 8 caracteres')
            password = input(fg('white') + 'Introduzca su contraseña nuevamente: ')
        elif password.isalpha():
            print(fg('red') + 'Contraseña invalida')
            password = input(fg('white') +'Ingrese nuevamente su contraseña: ')
        elif password.isnumeric():
            print(fg('red') + 'Contraceña invalida')
            password = input(fg('white') + 'Ingrese nuevamente su contraseña: ')
    else:
        print(fg('red') + 'Para iniciar el juego debe creal un usuario')
        

   
     







