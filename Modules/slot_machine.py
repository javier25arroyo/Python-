import random

list_fruits = ['🍒', '🍇', '🍉', '7️⃣']

# Obtener tres símbolos aleatorios
results = random.choices(list_fruits, k=3)

# Mostrar los resultados
print(f"{results[0]} | {results[1]} | {results[2]}")

# Verificar si ganó
if results.count('7️⃣') == 3:
    print("¡Jackpot! 💰")
else:
    print("¡Gracias por jugar!")


"""
import random

list_fruits = ['🍒', '🍇', '🍉', '7️⃣']

def play():
    # Obtener tres símbolos aleatorios
    results = random.choices(list_fruits, k=3)
    
    # Mostrar los resultados
    print(f"{results[0]} | {results[1]} | {results[2]}")
    
    # Verificar si ganó
    if results.count('7️⃣') == 3:
        print("¡Jackpot! 💰")
    else:
        print("¡Gracias por jugar!")
    
    return results

# Bucle principal del juego
def main():
    print("¡Bienvenido a la Máquina Tragamonedas!")
    
    playing = True
    while playing:
        play()
        
        # Preguntar si quiere jugar otra vez
        response = input("¿Quieres jugar otra vez? (Y/N): ").upper()
        if response != 'Y':
            playing = False
            print("¡Hasta pronto!")

if __name__ == "__main__":
    main()
"""