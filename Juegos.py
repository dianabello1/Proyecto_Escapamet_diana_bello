from colored import fg, bg, attr, fore
from pyfiglet import Figlet
import requests
import time 
import random
from sympy import Symbol, cos
from Juegos_clases import Ahorcado


# Modulo 4: Juegos

#API 
url = "https://api-escapamet.vercel.app/"
response = requests.get(url)
info_cuartos = response.json()
x = info_cuartos
#print(x[0]['objects'][2]['game']['name'])


 
# Juego de Encuentra la Lógica  --- > Listo

#Información básica del juego ( extraida de la Api)
def api_encuentra_la_logica(x):
  requirement = x[2]['objects'][0]['game']['requirement']
  award = x[2]['objects'][0]['game']['award']
  rules = x[2]['objects'][0]['game']['rules']
  print(fg('red') + 'LEEME')
  print(' ')
  print(fg('white') + f'Los requerimientos para este juego son: {requirement}')
  print(f'La recompenza: {award}')
  print(f'Las reglas: {rules}')

#Función que hace que el juego funcione
def play_game(x):
  vida = 5 
  preguntas = []

  pregunta_1 = x[2]['objects'][0]['game']['questions'][0]
  pregunta_2 = x[2]['objects'][0]['game']['questions'][1]

  preguntas.append(pregunta_1)
  preguntas.append(pregunta_2)

  x = random.choice(preguntas)
  print(fg('white') + x)

  if x == pregunta_1:
    ans = input('Tu Respuesta: ')
    if  ans  == '67':
     print(fg('green') + '-----------------------------------')
     print(fg('green') + ' FELICIDADES GANASTE UN DISCO DURO ')
     print(fg('green') + '-----------------------------------')  
    else: 
     vida -= 1
     print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto #de vida')
     print(f'Te queda de vida: {vida}')
     print (fg('green') + 'GAME OVER')
  else:
    ans = input('Tu Respuesta: ')
   if  ans  == '41':
     print(fg('green') + '-----------------------------------')
     print(fg('green') + ' FELICIDADES GANASTE UN DISCO DURO ')
     print(fg('green') + '-----------------------------------')
   else: 
     vida -= 1
     print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto #de vida')
     print(f'Te queda de vida: {vida}')
     print (fg('green') + 'GAME OVER')

#Función que llama al juego 
def main_encuentra_la_logica():
   while True: 
       print(fg('green') + 'Bienvenido al juego de Encuentra la logica')
       print(' ')
       api_encuentra_la_logica(x)
       print(' ')
       print(fg('red') + 'PREGUNTA 1')
       print(' ')
       play_game(x)
       break

main_encuentra_la_logica()



#Juego de las adivinazas  --> listo 

#Información básica del juego ( extraida de la Api)
def api_adivinanzas(x):
  requirement = x[0]['objects'][2]['game']['requirement']
  if requirement == 'false':
    print('Ninguno')
  award = x[0]['objects'][2]['game']['award']
  rules = x[0]['objects'][2]['game']['rules']

  print(fg('red') + 'LEEME')
  print(' ')
  print(fg('white') + f'Los requerimientos para este juego son: {requirement}')
  print(f'La recompenza: {award}')
  print(f'Las reglas: {rules}')

#Función que hace que el juego funcione
def play_game(x):
  preguntas = []
  respuestas = []
  pistas = []
  vida = 5
  
  pregunta_1 = (x[0]['objects'][2]['game']['questions'][0]['question'])
  pregunta_2 = (x[0]['objects'][2]['game']['questions'][1]['question'])
  pregunta_3 = (x[0]['objects'][2]['game']['questions'][2]['question'])
  
  respuesta_1 = (x[0]['objects'][2]['game']['questions'][0]['answers'][1])
  respuesta_2 = (x[0]['objects'][2]['game']['questions'][1]['answers'][1])
  respuesta_3 = (x[0]['objects'][2]['game']['questions'][2]['answers'][1])

  pista_1 = (x[0]['objects'][2]['game']['questions'][0]['clue_1'])
  pista_2 = (x[0]['objects'][2]['game']['questions'][0]['clue_2'])
  pista_3 = (x[0]['objects'][2]['game']['questions'][0]['clue_3'])

  pista_1_1 = (x[0]['objects'][2]['game']['questions'][1]['clue_1'])
  pista_1_2 = (x[0]['objects'][2]['game']['questions'][1]['clue_2'])
  pista_1_3 = (x[0]['objects'][2]['game']['questions'][1]['clue_3'])

  pista_1_4 = (x[0]['objects'][2]['game']['questions'][2]['clue_1'])
  pista_1_5 = (x[0]['objects'][2]['game']['questions'][2]['clue_2'])
  pista_1_6 = (x[0]['objects'][2]['game']['questions'][2]['clue_3'])

  preguntas.append(pregunta_1)
  preguntas.append(pregunta_2)
  preguntas.append(pregunta_3)

  respuestas.append(respuesta_1)
  respuestas.append(respuesta_2)
  respuestas.append(respuesta_3)

  pistas.append(pista_1)
  pistas.append(pista_2)
  pistas.append(pista_3)

  pistas.append(pista_1_1)
  pistas.append(pista_1_2)
  pistas.append(pista_1_3)
  pistas.append(pista_1_4)
  pistas.append(pista_1_5)
  pistas.append(pista_1_6)

  x = random.choice(preguntas)
  print(fg('white') + x)
  
  if x == pregunta_1:
    print(' ')
    pista = input(fg('red') + '¿ ¿Quieres una pista? (si o no) ')
    if pista.lower() == 'si' or pista.lower() == 's':
      print(fg('green') + pista_1)
      print(' ')
      segunda_pista = input(fg('red') + '¿Quieres otra pista ? (si o no) ')
      if segunda_pista.lower() == 'si' or segunda_pista.lower() == 's':
        print(fg('green') + pista_2)
        print('')
      tercera_pista = input(fg('red') + '¿Quieres otra pista? (si o no ) ')
      if tercera_pista.lower() == 'si' or tercera_pista.lower() == 's':
        print(fg('green') + pista_3)
        print('')
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_1:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto de vida')
        print(f'Te queda de vida: {vida}')
        print (fg('green') + 'GAME OVER')    
    else:
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_1:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto #de vida')
        print(f'Te queda de vida: {vida}')
        print (fg('green') + 'GAME OVER')
  elif x == pregunta_2:
    print(' ')
    pista = input(fg('red') + '¿Quieres una pista? (si o no) ')
    print(' ')
    if pista.lower() == 'si' or pista.lower() == 's':
      print(fg('green') + pista_1_1)
      print(' ')
      cuarta_pista = input(fg('red') + '¿Quieres otra pista? (si o no) ')
      if cuarta_pista.lower() == 'si' or cuarta_pista.lower() == 's':
        print(fg('green') + pista_1_2)
        print(' ')
      quinta_pista = input(fg('red') + '¿Quieres otra pista? (si o no ) ')
      if quinta_pista.lower() == 'si' or quinta_pista.lower() == 's':
        print(fg('green') + pista_1_3)
        print(' ')
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_2:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto de vida')
        print(f'Te queda de vida: {vida}')
        print (fg('green') + 'GAME OVER')        
    else:
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_2:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto de vida')
        print(f'Te queda de vida: {vida}')
        print (fg('green') + 'GAME OVER')  
  else: 
    print(' ')
    pista = input(fg('red') + '¿Desea una pista? (si o no)')
    if pista.lower() == 'si' or pista.lower() == 's':
      print(fg('green') + pista_1_4)
      print(' ')
      sexta_pista = input(fg('red') + '¿Quieres otra pista? (si o no) ')
      if sexta_pista.lower() == 'si' or sexta_pista.lower() == 's':
        print(fg('green') + pista_1_5)
        print(' ')
      septima_pista = input(fg('red') + '¿Quieres otra pista? (si o no ) ')
      if septima_pista.lower() == 'si' or septima_pista.lower() == 's':
        print(fg('green') + pista_1_6)
        print(' ')
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_3:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta')
        print (fg('green') + 'GAME OVER')    
    else:
      respuesta_input = input(fg('red') + 'Ingrese su #respuesta AQUI: ')
      if respuesta_input.lower() == respuesta_3:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto de vida')
        print(f'Te queda de vida: {vida}')
        print (fg('green') +  'GAME OVER')  

#Funcíon Principal del Juego de las api_adivinanzas
def main_adivinanzas():
  while True: 
    print(fg('green') + 'Bienvenido al juego de las Adivinanzas')
    print(' ')
   api_adivinanzas(x)
    print(' ')
   print(fg('red') + 'PREGUNTA 1')
   print(' ')
    play_game(x)
   break

main_adivinanzas()



#Juego de las Preguntas de Quiz Cultura Unimetana ---> Listo 

#Información básica del juego ( extraida de la Api)
def api_preguntas_cultura_unimetana(x):
  requirement = x[2]['objects'][1]['game']['requirement']
  if requirement == 'false':
    print('Ninguno')
  award = x[2]['objects'][1]['game']['award']
  rules = x[2]['objects'][1]['game']['rules']

  print(fg('red') + 'LEEME')
  print(' ')
  print(fg('white') + f'Los requerimientos para este juego son: {requirement}')
  print(f'La recompenza: {award}')
  print(f'Las reglas: {rules}')

#Función principal del juego
def play_game(x):
  preguntas = []
  respuestas = []
  pistas = []
  vida = 5
  
  pregunta_1 = (x[2]['objects'][1]['game']['questions'][0]['question'])
  pregunta_2 = (x[2]['objects'][1]['game']['questions'][1]['question'])
  pregunta_3 = (x[2]['objects'][1]['game']['questions'][2]['question'])
  
  respuesta_1 = (x[2]['objects'][1]['game']['questions'][0]['correct_answer'])
  respuesta_2 = (x[2]['objects'][1]['game']['questions'][1]['correct_answer'])
  respuesta_3 = (x[2]['objects'][1]['game']['questions'][2]['correct_answer'])

  pista_1 = (x[2]['objects'][1]['game']['questions'][0]['clue_1'])
  pista_2 = (x[2]['objects'][1]['game']['questions'][1]['clue_1'])
  pista_3 = (x[2]['objects'][1]['game']['questions'][2]['clue_1'])

  preguntas.append(pregunta_1)
  preguntas.append(pregunta_2)
  preguntas.append(pregunta_3)

  respuestas.append(respuesta_1)
  respuestas.append(respuesta_2)
  respuestas.append(respuesta_3)

  pistas.append(pista_1)
  pistas.append(pista_2)
  pistas.append(pista_3)

  x = random.choice(preguntas)
  print(fg('white') + x)
  
  if x == pregunta_1:
    print(fg('white') + '''
    1. 22 de septiembre
    2. 22 de octubre
    3. 25 de septiembre
    4. 25 de octubre
    >> ''')
    pista = input(fg('red') + '¿Desea una pista? (si o no)')
    print(' ')
    if pista.lower() == 'si' or pista.lower() == 's':
      print(fg('green') + pista_1)
      print(' ')
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_1:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta')
        print (fg('green') + 'GAME OVER')    
    else:
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_1:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto de vida')
        print (fg('green') + 'GAME OVER')     
  elif x == pregunta_2:
    print(fg('white') +'''
    1. 1969
    2. 1980
    3. 1979
    4. 1970
    >> ''')
    pista = input(fg('red') + '¿Desea una pista? (si o no)')
    print(' ')
    if pista.lower() == 'si' or pista.lower() == 's':
      print(fg('green') + pista_2)
      print(' ')
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_2:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto de vida')
        print (fg('green') + 'GAME OVER')    
    else:
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_2:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto de vida')
        print (fg('green') + 'GAME OVER')  
  else: 
    print(fg('white') + '''
    1. Rafael Matiezo
    2. Eugenio Mendoza
    3. Luis Miguel Da Gama
    4. Lorenzo Mendoza
    >> ''')
    pista = input(fg('red') + '¿Desea una pista? (si o no)')
    print(' ')
    if pista.lower() == 'si' or pista.lower() == 's':
      print(fg('green') + pista_3)
      print(' ')
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_3.lower():
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta')
        print (fg('green') + 'GAME OVER')    
    else:
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      if respuesta_input.lower() == respuesta_3.lower():
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto de vida')
        print (fg('green') + 'GAME OVER')  

#Funcíon Principal del Juego de las Preguntas de Quizizz Cultura Unimetana
def main_preguntas_cultura_unimetana():
  while True: 
    print(fg('green') + 'Bienvenido al juego de las Preguntas de Quizizz Cultura Unimetana')
    print(' ')
    api_preguntas_cultura_unimetana(x)
    print(' ')
    print(fg('red') + 'PREGUNTA 1')
    print(' ')
    play_game(x)
    break

main_preguntas_cultura_unimetana()



#Juego de las Preguntas de matematicas ------>> Falta 

#Información básica del juego ( extraida de la Api)
def api_preguntas_matematicas(x):
  requirement = x[1]['objects'][1]['game']['requirement']
  if requirement == 'false':
    print('Ninguno')
  award = x[1]['objects'][1]['game']['award']
  rules = x[1]['objects'][1]['game']['rules']

  print(fg('red') + 'LEEME')
  print(' ')
  print(fg('white') + f'Los requerimientos para este juego son: {requirement}')
  print(f'La recompenza: {award}')
  print(f'Las reglas: {rules}')

#Función que hace que el juego funcione
def play_game(x):
  preguntas = []
  respuestas = []
  pistas = []
  vida = 5
  
  pregunta_1 = (x[1]['objects'][1]['game']['questions'][0]['question'])
  pregunta_2 = (x[1]['objects'][1]['game']['questions'][1]['question'])
  pregunta_3 = (x[1]['objects'][1]['game']['questions'][2]['question'])
  
  pista_1 = (x[0]['objects'][2]['game']['questions'][0]['clue_1'])
  pista_2 = (x[0]['objects'][2]['game']['questions'][1]['clue_1'])
  pista_3 = (x[0]['objects'][2]['game']['questions'][2]['clue_1'])

  preguntas.append(pregunta_1)
  preguntas.append(pregunta_2)
  preguntas.append(pregunta_3)

  pistas.append(pista_1)
  pistas.append(pista_2)
  pistas.append(pista_3)

  x = random.choice(preguntas)
  print(fg('white') + x)
  
  if x == pregunta_1:
    print(' ')
    pista = input(fg('red') + '¿ ¿Quieres una pista? (si o no) ')
    if pista.lower() == 'si' or pista.lower() == 's':
      print(fg('green') + pista_1)
      print(' ')
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      #print(' ')
      if respuesta_input.lower() == respuesta_1:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto de vida')
        print(f'Te queda de vida: {vida}')
        print (fg('green') + 'GAME OVER')    
    else:
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_1:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto de vida')
        print(f'Te queda de vida: {vida}')
        print (fg('green') + 'GAME OVER')

  elif x == pregunta_2:
    print(' ')
    pista = input(fg('red') + '¿Quieres una pista? (si o no) ')
    print(' ')
    if pista.lower() == 'si' or pista.lower() == 's':
      print(fg('green') + pista_1_1)
      print(' ')
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_2:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto de vida')
        print(f'Te queda de vida: {vida}')
        print (fg('green') + 'GAME OVER')        
    else:
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_2:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto #de vida')
        print(f'Te queda de vida: {vida}')
        print (fg('green') + 'GAME OVER')  
  else: 
    print(' ')
    pista = input(fg('red') + '¿Desea una pista? (si o no)')
    if pista.lower() == 'si' or pista.lower() == 's':
      print(fg('green') + pista_1_4)
      print(' ')
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_3:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta')
        print (fg('green') + 'GAME OVER')    
    else:
      respuesta_input = input(fg('red') + 'Ingrese su #respuesta AQUI: ')
      if respuesta_input.lower() == respuesta_3:
        print(fg('green') + '----------------------')
       print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto #de vida')
        print(f'Te queda de vida: {vida}')
        print (fg('green') +  'GAME OVER')  

#Funcíon Principal del Juego de las preguntas de Matemáticas
def main_preguntas_matematica():
  while True: 
    print(fg('green') + 'Bienvenido al juego de las Preguntas de Matematicas ')
    print(' ')
    api_preguntas_matematicas(x)
    print(' ')
    print(fg('red') + 'PREGUNTA 1')
    print(' ')
    play_game(x)
    break

main_preguntas_matematica()




#Juego del Criptograma  ---> Falta arregar un problema con las preguntas

#Información básica del juego ( extraida de la Api)
def api_criptograma(x):
  requirement = x[1]['objects'][2]['game']['requirement']
  award = x[1]['objects'][2]['game']['award']
  rules = x[1]['objects'][2]['game']['rules']

  print(fg('red') + 'LEEME')
  print(' ')
  print(fg('white') + f'Los requerimientos para este juego son: {requirement}')
  print(f'La recompenza: {award}')
  print(f'Las reglas: {rules}')

#Función que hace que el juego funcione
def play_game(x):
  preguntas = []
  respuestas = []
  pistas = []
  vida = 5
  text_cifrado_1 = []
  text_cifrado_2 = []
  text_cifrado_3 = []

  texto = 'Si te graduas pisas el samán'.lower() 
  n = 2
  abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 Cifrando el mensaje 
  for letra in texto:
    if letra in abc: 
      n_letra = abc.index(letra)
      nueva_letra = (n_letra + n) % len(abc)
      text_cifrado_1 += abc[nueva_letra]
    else:
      text_cifrado_1 += letra
  print("Mensaje cifrado:", text_cifrado_1)

  texto = 'Si te graduas pisas el samán'.lower() 
  n = 4
  abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 Cifrando el mensaje 
  for letra in texto:
    if letra in abc: 
      n_letra = abc.index(letra)
      nueva_letra = (n_letra + n) % len(abc)
      text_cifrado_2 += abc[nueva_letra]
    else:
      text_cifrado_2 += letra
  print("Mensaje cifrado:", text_cifrado_2)


  texto = 'Si te graduas pisas el samán'.lower() 
  n = 5
  abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 Cifrando el mensaje 
  for letra in texto:
    if letra in abc: 
      n_letra = abc.index(letra)
      nueva_letra = (n_letra + n) % len(abc)
      text_cifrado_3 += abc[nueva_letra]
    else:
      text_cifrado_3 += letra
  print("Mensaje cifrado:", text_cifrado_3)

  respuesta_1 = x[1]['objects'][2]['game']['questions'][0]['question']
  respuesta_2 = x[1]['objects'][2]['game']['questions'][1]['question']
  respuesta_3 = x[1]['objects'][2]['game']['questions'][2]['question']
  
  pista_1 = x[1]['objects'][2]['game']['questions'][0]['desplazamiento']
  pista_2 = x[1]['objects'][2]['game']['questions'][1]['desplazamiento']
  pista_3 = x[1]['objects'][2]['game']['questions'][2]['desplazamiento']

  preguntas.append(text_cifrado_1)
  preguntas.append(text_cifrado_2)
  preguntas.append(text_cifrado_3)

  respuestas.append(respuesta_1)
  respuestas.append(respuesta_2)
  respuestas.append(respuesta_3)

  pistas.append(pista_1)
  pistas.append(pista_2)
  pistas.append(pista_3)

  x = random.choice(preguntas)
  print(fg('white') + x )

  if x == text_cifrado_1:
    print(' ')
    print(fg('white') + '''
              A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
              Y Z A B C D E F G H I J K L M N O P Q R S T U V W X   

    Descubre el mensaje cifrado:        
    ''')
    pista = input(fg('red') + '¿ ¿Quieres una pista? (si o no) ')
    if pista.lower() == 'si' or pista.lower() == 's':
      print(fg('green') + f' El abecedario posee {pista_1} desplazamientos')
      print(' ')
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_1:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta. Pierdes un cuarto de vida')
        print(f'Te queda de vida: {vida}')
        print (fg('green') + 'GAME OVER')    
    else:
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_1:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto de vida')
        print(f'Te queda de vida: {vida}')
        print (fg('green') + 'GAME OVER')  
  elif x == text_cifrado_2:
    print(' ')
    print(fg('white') + '''
              A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  
              W X Y Z A B C D E F G H I J K L M N O P Q R S T U V  

    Descubre el mensaje cifrado:        
    ''')
    pista = input(fg('red') + '¿ ¿Quieres una pista? (si o no) ')
    if pista.lower() == 'si' or pista.lower() == 's':
      print(fg('green') + f' El abecedario posee {pista_2} desplazamientos')
      print(' ')
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_2:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta. Pierdes un cuarto de vida')
        print(f'Te queda de vida: {vida}')
        print (fg('green') + 'GAME OVER')    
    else:
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_2:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto de vida')
        print(f'Te queda de vida: {vida}')
        print (fg('green') + 'GAME OVER')
  else:
    print(' ')
    print(fg('white') + '''
              A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  
              V W X Y Z A B C D E F G H I J K L M N O P Q R S T U 

    Descubre el mensaje cifrado:        
    ''')
    pista = input(fg('red') + '¿ ¿Quieres una pista? (si o no) ')
    if pista.lower() == 'si' or pista.lower() == 's':
      print(fg('green') + f' El abecedario posee {pista_3} desplazamientos')
      print(' ')
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_3:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta. Pierdes un cuarto de vida')
        print(f'Te queda de vida: {vida}')
        print (fg('green') + 'GAME OVER')    
    else:
      respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
      print(' ')
      if respuesta_input.lower() == respuesta_2:
        print(fg('green') + '----------------------')
        print(fg('green') + ' GANASTE, FELICIDADES ')
        print(fg('green') + '----------------------')
      else:
        vida -= 1/4
        print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto de vida')
        print(f'Te queda de vida: {vida}')
        print (fg('green') + 'GAME OVER')

#Funcíon Principal del Juego de las api_adivinanzas
def main_criptograma():
  while True: 
    print(fg('green') + 'Bienvenido al juego del Criptograma')
    print(' ')
    api_criptograma(x)
    print(' ')
    print(fg('red') + 'PREGUNTA 1')
    print(' ')
    play_game(x)
    break

main_criptograma()




#Juego de las Preguntas Sobre Python ------> Falta 

#Información básica del juego ( extraida de la Api)
def api_preguntas_python(x):
  requirement = x[0]['objects'][1]['game']['requirement']
  award = x[0]['objects'][1]['game']['award']
  rules = x[0]['objects'][1]['game']['rules']

  print(fg('red') + 'LEEME')
  print(' ')
  print(fg('white') +  f'Los requerimientos para este juego son: {requirement}')
  print(f'La recompenza: {award}')
  print(f'Las reglas: {rules}')

#Función que imprime las preguntas
def play_game(x):
  preguntas = []
  respuestas = []
  vida = 5
  pistas = []
    
  pregunta_1 = (x[0]['objects'][1]['game']['questions'][0]['question'])
  pregunta_2 = (x[0]['objects'][1]['game']['questions'][1]['question'])
  
  respuesta_1 = '("Extracción de " + frase[18:21])'

  pista_1 = (x[0]['objects'][1]['game']['questions'][0]['clue_1'])
  pista_2 = (x[0]['objects'][1]['game']['questions'][0]['clue_2'])
  pista_3 = (x[0]['objects'][1]['game']['questions'][0]['clue_3'])

  pista_1_1 = (x[0]['objects'][1]['game']['questions'][1]['clue_1'])
 
 
  preguntas.append(pregunta_1)
  preguntas.append(pregunta_2)

  pistas.append(pista_1)
  pistas.append(pista_2)
  pistas.append(pista_3)

  pistas.append(pista_1_1)
  

  x = random.choice(preguntas)
  print(fg('white') + x)

  if x == pregunta_1:
    print(' ')
    pista = input(fg('red') + '¿ ¿Quieres una pista? (si o no) ')
    if pista.lower() == 'si' or pista.lower() == 's':
      print(fg('green') + pista_1)
      print(' ')
    segunda_pista = input(fg('red') + '¿Quieres otra pista ? (si o no) ')
    if segunda_pista.lower() == 'si' or segunda_pista.lower() == 's':
      print(fg('green') + pista_2)
      print('')
    tercera_pista = input(fg('red') + '¿Quieres otra pista? (si o no ) ')
    if tercera_pista.lower() == 'si' or tercera_pista.lower() == 's':
      print(fg('green') + pista_3)
      print('')
    respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
    print(' ')
    if respuesta_input.lower() == respuesta_1:
      print(fg('green') + '----------------------')
      print(fg('green') + ' GANASTE, FELICIDADES ')
      print(fg('green') + '----------------------')
    else:
      vida -= 1/4
      print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto de vida')
      print(f'Te queda de vida: {vida}')
      print (fg('green') + 'GAME OVER')    
  else:
    respuesta_input = input(fg('red') + 'Ingrese su respuesta AQUI: ')
    print(' ')
    if respuesta_input.lower() == respuesta_1:
      print(fg('green') + '----------------------')
      print(fg('green') + ' GANASTE, FELICIDADES ')
      print(fg('green') + '----------------------')
    else:
      vida -= 1/4
      print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto #de vida')
      print(f'Te queda de vida: {vida}')
      print (fg('green') + 'GAME OVER')

#Intento de validación: segunda pregunta 
def invertir_cadena(cadena):
   return cadena[::-1]

def invertir_cadena_manual(cadena):
   cadena_invertida = ""
   for letra in cadena:
       cadena_invertida = letra + cadena_invertida
   return cadena_invertida

print(invertir_cadena("Hola"))
print(invertir_cadena('diana'))

#Funcíon Principal del Juego de Preguntas de Python  
def main_preguntas_python():
 while True: 
   print(fg('green') + 'Bienvenido al juego de las Preguntas sobre Python')
   print(' ')
    api_preguntas_python(x)
    print(' ')
    print(fg('red') + 'PREGUNTA 1')
    print(' ')
    play_game(x)
    break

main_preguntas_python()



#Juego Escoge un número entre

#Información básica del juego ( extraida de la Api)
def api_escoge_entre(x):
   requirement = x[4]['objects'][2]['game']['requirement']
   award = x[4]['objects'][2]['game']['award']
   rules = x[4]['objects'][2]['game']['rules']
   print(fg('red') + 'LEEME')
   print(' ')
   print(fg('white') + f'Los requerimientos para este juego son: {requirement}')
   print(f'La recompenza: {award}')
   print(f'Las reglas: {rules}')

#Función que Hace que el juego funcione
def play_game(x):
   vida = 5
   contador = 0

    pregunta_1 = x[4]['objects'][2]['game']['questions'][0]['question']
    respuesta = range(1,15)
   pista_1 = (fg('green') + ' ¡Estas cerca! Un poco mas abajo ')
   pista_2 = (fg('green') + ' ¡Estas cerca! Un poco mas arriba ')
   pista_3 = (fg('green') + ' ¡Estas muy arriba! ')
   pista_4 = (fg('green') + ' ¡Estas muy abajo! ')

    respuesta = x
    x = random.randint(1,15)
    print(fg('white') +  pregunta_1)

    ans = input(fg('red') + ' Tu Respuesta: ')
    if ans < respuesta :
        if ans < respuesta - 3:
            print(pista_4)
            contador += 1 
            if contador == '1':
                print('Te quedan 2 intentos')
                ans = input(fg('red') + ' Tu Respuesta: ')
            elif contador =='2':
                print('Te queda 1 intento')
                ans = input(fg('red') + ' Tu Respuesta: ')
            else:
                vida -= 1
                print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto #de vida')
                print(f'Te queda de vida: {vida}')
                print (fg('green') + 'GAME OVER')     
        else:
            print(pista_2)
            contador += 1 
            if contador == '1':
                print('Te quedan 2 intentos')
                ans = input(fg('red') + ' Tu Respuesta: ')
            elif contador =='2':
                print('Te queda 1 intento')
                ans = input(fg('red') + ' Tu Respuesta: ')
            else:
                vida -= 1
                print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto #de vida')
                print(f'Te queda de vida: {vida}')
                print (fg('green') + 'GAME OVER') 
    elif ans > respuesta :
        if ans > respuesta + 3:
            print(pista_3)
            contador += 1 
            if contador == '1':
                print('Te quedan 2 intentos')
                ans = input(fg('red') + ' Tu Respuesta: ')
            elif contador =='2':
                print('Te queda 1 intento')
                ans = input(fg('red') + ' Tu Respuesta: ')
            else:
                vida -= 1
                print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto #de vida')
                print(f'Te queda de vida: {vida}')
                print (fg('green') + 'GAME OVER')
        else:
            print(pista_1)
            contador += 1 
            if contador == '1':
                print('Te quedan 2 intentos')
                ans = input(fg('red') + ' Tu Respuesta: ')
            elif contador =='2':
                print('Te queda 1 intento')
                ans = input(fg('red') + ' Tu Respuesta: ')
            else:
                vida -= 1
                print(fg('white') + 'Respuesa incorecta, Pierdes un cuarto #de vida')
                print(f'Te queda de vida: {vida}')
                print (fg('green') + 'GAME OVER')

    else:
        ans == respuesta
        print(fg('green') + '----------------------------------------------')
        print(fg('green') + ' FELICIDADES GANASTE UN TITULO UNIVERSITARIO ')
        print(fg('green') + '-----------------------------------------------')  

# Función principal
def main_escoge_entre():
   while True:
       print(fg('green') + 'Bienvenido al juego de Encuentra la logica')
       print(' ')
       api_escoge_entre(x)
       print(' ')
       print(fg('red') + 'PREGUNTA 1')
       print(' ')
       play_game(x)
       break
main_escoge_entre()

