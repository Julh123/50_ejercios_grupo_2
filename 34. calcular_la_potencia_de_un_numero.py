base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = 1
for i in range(exponente):
    resultado *= base
print("El resultado es:", resultado)
