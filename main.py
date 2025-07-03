import random

def descubrir_palabras(palabras_secretas, palabra_secreta):
    print('Hay ', len(palabras_secretas), 'palabras secretas.')
    if len(palabras_secretas) == 1:
        print('Todas las palabras han sido descubiertas.')
    if palabra_secreta in palabras_secretas:
        palabras_secretas.remove(palabra_secreta)

def seleccionar_palabra(palabras_secretas):
    palabra_secreta = random.choice(palabras_secretas)
    return palabra_secreta

def vida(intentos):
    if intentos == 6:
        return('''
     +---+
     |   |
         |
         |
         |
         |
         |
         |
         |
    ========''')
    elif intentos == 5:
       return('''
     +---+
     |   |
     O   |
         |
         |
         |
         |
         |
         |
    ========''')
    elif intentos == 4:
        return('''
     +---+
     |   |
     O   |
     |   |
     |   |
         |
         |
         |
         |
    ========''')
    elif intentos == 3:
        return('''
     +---+
     |   |
     O   |
     |   |
    /|   |
     |   |
         |
         |
         |
    ========''')
    elif intentos == 2:
        return('''
     +---+
     |   |
     O   |
     |   |
    /|\  |
     |   |
         |
         |
         |
    ========''')
    elif intentos == 1:
        return('''
     +---+
     |   |
     O   |
     |   |
    /|\  |
     |   |
    /    |
         |
         |
    ========''')
    else:
        return('''
     +---+
     |   |
     O   |
     |   |
    /|\  |
     |   |
    / \  |
         |
         |
    ========''')
       

def palabra_secreta(palabra):
    letras_adivinadas = []
    palabra_oculta = ['_' for _ in palabra]
    intentos = 6
    print('Adivina la palabra secreta letra por letra.')
    
    while intentos > 0 and '_' in palabra_oculta:
        print(vida(intentos))
        print('Palabra secreta:')
        print(' '.join(palabra_oculta))
        letra = input('Introduce una letra: ').lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print('Por favor, introduce solo una letra.')
            continue
        
        if letra in letras_adivinadas:
            print('Ya has adivinado esa letra. Intenta con otra.')
            continue
        
        letras_adivinadas.append(letra)
        
        if letra in palabra:
            for i, l in enumerate(palabra):
                if l == letra:
                    palabra_oculta[i] = letra
            print('¡Correcto!')
        else:
            intentos -= 1
            print(f'Incorrecto.')
    
    if intentos == 0:
        print('Has agotado tus intentos.')
        print(vida(intentos))
        print('La palabra era:', palabra)

def main():

    palabras_secretas = [
        'python',
        'programacion',
        'desarrollo',
        'algoritmo',
        'funcion',
        'variable',
        'condicional',
        'bucle',
        'lista',
        'diccionario'
    ]

    print('_' * 50)
    print('¡Bienvenido al juego del ahorcado!')
    print('_' * 50)

    while len(palabras_secretas) != 0:
        salir = input('¿Quieres jugar? (s/n): ').lower()
        if salir == 'n':
            break
        elif salir != 's':
            print('Por favor, responde con "s" o "n".')
            continue
        
        palabra_seleccionada = seleccionar_palabra(palabras_secretas)
        
        descubrir_palabras(palabras_secretas, palabra_seleccionada)
        
        print(palabra_seleccionada)
        palabra_secreta(palabra_seleccionada)
        
    
    print('¡Gracias por jugar!')

    

if __name__ == "__main__":
    main()
