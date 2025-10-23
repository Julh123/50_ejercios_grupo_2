import random
secreto = random.randint(1, 100)
intento = 0
while True:
    intento += 1
    numero = int(input("Adivine el número (1-100): "))
    if numero == secreto:
        print(f"¡Correcto! Lo lograste en {intento} intentos.")
        break
    elif numero < secreto:
        print("Demasiado bajo.")
    else:
        print("Demasiado alto.")
