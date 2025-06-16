import random

# Lista de palabras para adivinar
palabras = ["python", "universidad", "programacion", "computadora", "algoritmo"]

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Jugar Ahorcado")
    print("2. Instrucciones")
    print("3. Salir")

def instrucciones():
    print("\n--- INSTRUCCIONES ---")
    print("Adivina la palabra letra por letra.")
    print("Tienes un número limitado de intentos.")
    print("Cada error reduce tus vidas.")
    print("¡Buena suerte!\n")

def elegir_palabra():
    return random.choice(palabras)

def jugar():
    palabra = elegir_palabra()
    letras_adivinadas = []
    intentos_restantes = 6
    palabra_oculta = ["_" for _ in palabra]

    while intentos_restantes > 0 and "_" in palabra_oculta:
        print("\nPalabra: " + " ".join(palabra_oculta))
        print(f"Intentos restantes: {intentos_restantes}")
        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor ingresa solo una letra válida.")
            continue

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_oculta[i] = letra
            print("¡Bien hecho!")
        else:
            intentos_restantes -= 1
            print("Letra incorrecta.")

    if "_" not in palabra_oculta:
        print("\n¡Felicidades! Adivinaste la palabra:", palabra)
    else:
        print("\nHas perdido. La palabra era:", palabra)

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            jugar()
        elif opcion == "2":
            instrucciones()
        elif opcion == "3":
            print("Gracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Iniciar el juego
main()
