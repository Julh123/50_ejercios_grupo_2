numeros = []
for i in range(10):
    numeros.append(float(input("Ingrese un número: ")))
promedio = sum(numeros) / len(numeros)
print("El promedio es:", promedio)
