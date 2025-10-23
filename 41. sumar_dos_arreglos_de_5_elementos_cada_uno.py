A = [int(input("Ingrese número de la lista A: ")) for _ in range(5)]
B = [int(input("Ingrese número de la lista B: ")) for _ in range(5)]
suma = [A[i] + B[i] for i in range(5)]
print("Suma de listas:", suma)
