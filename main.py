from colored import fg, bg, attr, fore
from datetime import date, time, datetime
from terminaltables import AsciiTable
import emoji
from pyfiglet import Figlet



from Funciones import escribir_datos_en_txt, recibir_datos_del_txt, registro, confirmar_usuario
from Registro import Registro
from Escenarios import cuarto_de_servidores
from Escenarios import puerta_para_laboratorio
from Escenarios import laboratorio_SL001
from Escenarios import Biblioteca
from Escenarios import puerta_para_laboratorio
from Escenarios import plaza_rectorado
from Partida import Partida


    

def main():
    usuarios_list = []
  
    usuarios_list = recibir_datos_del_txt('/Users/dianabello/Work/Proyecto/Usuario.txt', usuarios_list )
    print(usuarios_list)
    while True:
        try:
            f = Figlet(font='big') 
            print(f.renderText(' Escapamet '))
            print(fg('green') + '¿Es tu primera vez jugando Escapamet? --> ¡Crea tu usuario!')
            menu = input(fg('white') + ''' 
                1. Crear Usuario 
                2. Iniciar Partida
                3. Records 
                4. Usuarios
                5. Salir
            >> ''')

            while (not menu.isnumeric()) or (int(menu) not in range(1,6)):
                print("-- Ingrese una opcion valida --")


            if menu == "1":
                usuarios_list = registro(usuarios_list)
                escribir_datos_en_txt('/Users/dianabello/Work/Proyecto/Usuario.txt', usuarios_list)

            elif menu == "2":
                confirmar_usuario(usuarios_list)
                print('¿En que dificultad desea jugar?')
                dificultad = input('''
                1. Fácil
                2. Medio
                3. Difícil 
                >> ''')
                while (not dificultad.isnumeric()) or (int(dificultad) not in range(1,4)):
                    print("-- Ingrese una opcion valida --")
                if dificultad == "1":
                    print(' COMENCEMOS ')
                    print()
                    print(fg('green') + ' Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos que nos ayudes a recuperar el disco, antes de que el servidor se caiga y no se pueda hacer más nada. ¿Aceptas el reto?')
                    aux = input(fg('red') + 'Tu Respuesta: (si o no )')
                    print()
                    if aux == 'si' or aux == 's':
                        print(fg('green ') + f'Bienvenido {self.username}, gracias por tu disposición a ayudarnos a resolver este inconveniente,  te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué acciones puedes realizar. Recuerda que el tiempo corre más rápido que un trimestre en este reto')
                        print()
                        partida_facil()
                        print(Biblioteca())
                        print(fg('white') + '¿Qué desea Hacer?')
                        opcion = input(fg('white') + ''' 
                        1. Ir al Mueble de sentarse
                        2. Ir al Mueble de libros
                        3. Ir al Mueble con cabetas
                        4. Ir al Samán 
                        5. Ir al la puerta del laboratorio
                        >>>  ''')
                        while (not opcion.isnumeric()) or (int(opcion) not in range(1,4)):
                            print(fg('red') + " Ingrese una opcion valida ")
                        if opcion == '1':
                            pass
                        elif opcion == '2':
                            pass
                        elif opcion == '3':
                            pass
                        elif opcion == '4':
                            print(plaza_rectorado)
                            opcion = input(''' ¿Qué desea Hacer?
                            1. Ir al Banco 1 
                            2. Ir al Banco 2
                            3. Ir al Samán 
                            4. Ir a la Biblioteca
                            >>>  ''')
                            if opcion == '1':
                                pass
                            elif opcion == '2':
                                pass
                            elif opcion == '3':
                                pass
                            else:
                                break
                        else:
                            print(puerta_para_laboratorio)
                            opcion = input(''' ¿Qué desea Hacer?
                            1. Abrir puerta 
                            2. Volver a la biblioteca
                            >>>  ''')
                            if opcion == '1':
                                pass
                            else:
                                break
                elif dificultad == "2":
                    pass
                else:
                    pass
            elif menu == "3":
                pass
            elif menu == "4":
                if len(usuarios_list) == 0:
                    print("Todavía no hay Usuarios registrados")
                else:
                    #jugador = Registro(username, password, edad, avatar)
                    #mostrar_jugador()
                    pass 
            else:
                break 
        except:
                print(fg('green') + "-- GRACIAS POR JUGAR --")
                print(' ')
                break
main()




