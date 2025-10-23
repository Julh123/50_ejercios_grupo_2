notas = [float(input("Ingrese una nota: ")) for _ in range(5)]
print("Promedio:", sum(notas) / len(notas))
print("Nota mayor:", max(notas))
print("Nota menor:", min(notas))
