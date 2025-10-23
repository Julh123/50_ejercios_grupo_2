while True:
    print("\n--- Calculadora ---")
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
    op = input("Elija una opción: ")
    if op == "5":
        break
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    if op == "1":
        print("Resultado:", a + b)
    elif op == "2":
        print("Resultado:", a - b)
    elif op == "3":
        print("Resultado:", a * b)
    elif op == "4":
        if b != 0:
            print("Resultado:", a / b)
        else:
            print("No se puede dividir entre cero")
    else:
        print("Opción inválida")
