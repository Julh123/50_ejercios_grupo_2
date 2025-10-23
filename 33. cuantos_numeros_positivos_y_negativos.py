positivos = negativos = 0
while True:
    num = float(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    elif num > 0:
        positivos += 1
    else:
        negativos += 1
print("Positivos:", positivos, "Negativos:", negativos)
