"""
gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('===============')
print('The Sorting Hat')
print('===============')

# ~~~~~~~~~~~~~~~ Question 1 ~~~~~~~~~~~~~~~

print('Q1) Do you like Dawn or Dusk?')

print('  1) Dawn')
print('  2) Dusk')

answer = int(input('Enter answer (1-2): '))

if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin +=1
else:
  print('Wrong input.')

# ~~~~~~~~~~~~~~~ Question 2 ~~~~~~~~~~~~~~~

print("\nQ2) When I'm dead, I want people to remember me as:")

print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
  hufflepuff += 2
elif answer == 2:
  slytherin += 2
elif answer == 3:
  ravenclaw += 2
elif answer == 4:
  gryffindor += 2
else:
  print('Wrong input.')

# ~~~~~~~~~~~~~~~ Question 3 ~~~~~~~~~~~~~~~

print('\nQ3) Which kind of instrument most pleases your ear?')

print('  1) The violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
  slytherin += 4
elif answer == 2:
  hufflepuff += 4
elif answer == 3:
  ravenclaw +=4
elif answer == 4:
  gryffindor += 4
else:
  print('Wrong input.')
  
print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)

# Bonus Part

most_points = max(gryffindor, ravenclaw, hufflepuff, slytherin)   # We'll learn about the max() function in Chapter 6

if gryffindor == most_points:
  print('🦁 Gryffindor!')
elif ravenclaw == most_points:
  print('🦅 Ravenclaw!')
elif hufflepuff == most_points:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')
"""

"""
print('▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨')
print('▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨')
print('▨▨⌜                  ⌝▨▨')
print('▨▨| BANK OF CODEDEX   |▨▨')
print('▨▨⌞                  ⌟▨▨')
print('▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨')
print('▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨')

pin = int(input('\nEnter your PIN:'))

while pin != 1234:
  pin = int(input('\nIncorrect PIN. Try again: '))

if pin == 1234:
  print('\nYou have successfully logged in🤟🏻')

  """
"""
guess = 0
tries = 0

while guess != 6 and tries < 6:
  guess = int(input('Guess the number:  '))
  tries = tries + 1

if guess != 6:
  print('You ran out of tries.')
else:
  print('You got it!')


i = 0 + 1
while i < 6:
  j = 0 + 1
  while j < 6:
    print(i * j)
    j = j + 1
  i = i + 1

rating = float(input('Enter your rating: '))

if rating > 4.5:
  print('Extraordinary')
elif rating > 4:
  print('Excellent')
elif rating > 3:
  print('Good')
elif rating > 2:
  print('Fair')
else:
  print('Poor')
  """

"""
grade = int(input('Enter their grade: '))

if grade == 9:
  print('Freshman')
elif grade == 10:
  print('Sophomore')
elif grade == 11:
  print('Junior')
elif grade == 12:
  print('Senior')
else:
  print('TBD')

grade = int(input('Enter their grade: '))

if grade >= 55:
  print('You passed.')
else:    
  print('You failed.')


ph = int(input('Enter the pH level:'))

if ph > 7:
  print('Basic')
elif ph < 7:
  print('Acidic')
else:
  print('Neutral')


question = input('Question:    ')

random_number = random.ranint(1, 9)

if random_number == 1:
  print('Yes - definitely')
elif random_number == 2:
  print('It is decidedly so')
elif random_number == 3:
  print('Without a doubt')
elif random_number == 4:
  print('Reply hazy, try again')
elif random_number == 5:
  print('Ask again later')
elif random_number == 6:
  print('Better not tell you now')
elif random_number == 7:
  print('My sources say no')
elif random_number == 8:
  print('Outlook not so good')
elif random_number == 9:
  print('Very doubtful')
else:
  print('Error')


height = int(input('Enter the height: '))
credits = int(input('Enter the credits: '))

if height >= 137 and credits == 10:
  print('¡Disfruta el viaje!')
elif height < 137 and credits == 10:
  print('¡Lo siento, no cumples con la altura mínima!')
elif height < 137 and credits < 10:
  print('¡Lo siento, no tienes suficientes créditos!')
else:
  print('¡Lo siento, no cumples con la altura mínima y no tienes suficientes créditos!')


for i in range(99, 0, -1):
  print(f'{i} bottles of beer on the wall')
  print(f'{i} bottles of beer')
"""
"""
for i in range(1, 100, 1):
  if i % 3 == 0 and i % 5 == 0:
    print('FizzBuzz ')
  elif i % 3 == 0 :
    print('Fizz')
  elif i % 5 == 0:
    print('Buzz')
  else:
    print(i)

i = 1
while i < 6:
  j = 1
  while j < 6:
    print(i * j)
    print('Soy el número: i * j', i , j)
    j = j + 1
  i = i + 1
"""
"""
grocery_list = ['🥚 Eggs','🥑 Avocados','🍪 Cookies','🌶 Hot Pepper Jam','🫐 Blueberries','🥦 Broccoli']
"""
"""
playlist = [
  'Porches - rangerover',
  'Mount Eerie - You Swan, Go On',
  'Carolyn Polachek - Look at Me Now',
  'Pinegrove - Darkness',
  'LVL UP - Spirit Was',
  'Mitski - First Love / Late Spring'
]
for song in playlist:
  print(song)"
"""
"""
things_to_do = [
  '🚀 Create the dopest learn to code platform ever.',
  '⛰️ Hike the Pacific Crest Trail.',
  '🏡 Build an A-frame house and raise some goats.',
  '🌏 Live somewhere in Asia for a year.',
  '🎸 Release an album.',
  '📝 Write a book.',
  '🏆 Reach 100k subscribers on YouTube.',
  '🚐 Road trip with the fam.',
  '🍳 Open a cozy diner upstate.',
  '👴🏻 Grow old with no regrets.'
]

for dream in things_to_do:
  print(dream)"
  """""
  """""
# Funciones integradas que ya hemos visto:
# 1. print(): Imprime el mensaje en la consola.
print("Hola, este es un ejemplo de uso de funciones integradas.")

# 2. input(): Solicita al usuario que ingrese un valor.
nombre = input("¿Cuál es tu nombre? ")

# 3. int(): Convierte una cadena de texto a un número entero.
edad = int(input("¿Cuál es tu edad? "))

# 4. max(): Devuelve el valor máximo de una lista de números.
numeros = [10, 20, 30, 40, 50]
maximo = max(numeros)
print(f"El número máximo en la lista es: {maximo}")

# Nueva función integrada:
# 5. sorted(): Devuelve una lista ordenada de los elementos de cualquier iterable.
# No hemos visto esta función antes en el curso.
lista_desordenada = [5, 3, 1, 4, 2]
lista_ordenada = sorted(lista_desordenada)
print(f"Lista ordenada: {lista_ordenada}")
  """""
  """""
import random

options = [
  'Don’t pursue happiness – create it.',
  'All things are difficult before they are easy.',
  'The early bird gets the worm, but the second mouse gets the cheese.',
  'If you eat something and nobody sees you eat it, it has no calories.',
  'Someone in your life needs a letter from you.',
  'Don’t just think. Act!',
  'Your heart will skip a beat.',
  'The fortune you search for is in another cookie.',
  'Help! I’m being held prisoner in a Chinese bakery!'
]

def fortune():
  random_fortune = random.randint(0, len(options) - 1)
  print(options[random_fortune])

fortune()
fortune()
fortune()
  """""
  """"""
  """"""
  