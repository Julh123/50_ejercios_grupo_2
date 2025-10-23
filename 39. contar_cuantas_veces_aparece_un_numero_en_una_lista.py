numeros = [int(input("Ingrese un número: ")) for _ in range(10)]
buscar = int(input("Ingrese el número a buscar: "))
print("El número aparece", numeros.count(buscar), "veces")
