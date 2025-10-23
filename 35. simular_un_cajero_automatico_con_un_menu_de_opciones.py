saldo = 1000
while True:
    print("\n--- Cajero Automático ---")
    print("1. Consultar saldo")
    print("2. Consignar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Saldo actual:", saldo)
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad a consignar: "))
        saldo += cantidad
        print("Consignación exitosa. Nuevo saldo:", saldo)
    elif opcion == "3":
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        if cantidad <= saldo:
            saldo -= cantidad
            print("Retiro exitoso. Nuevo saldo:", saldo)
        else:
            print("Fondos insuficientes.")
    elif opcion == "4":
        print("Gracias por usar el cajero.")
        break
    else:
        print("Opción inválida.")
