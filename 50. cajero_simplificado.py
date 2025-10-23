saldo = 1000
while True:
    print("\n--- Cajero ---")
    print("1. Consultar saldo\n2. Depositar\n3. Retirar\n4. Salir")
    opcion = input("Seleccione: ")
    if opcion == "1":
        print("Saldo actual:", saldo)
    elif opcion == "2":
        monto = float(input("Ingrese monto a depositar: "))
        saldo += monto
        print("Depósito exitoso. Nuevo saldo:", saldo)
    elif opcion == "3":
        monto = float(input("Ingrese monto a retirar: "))
        if monto <= saldo:
            saldo -= monto
            print("Retiro exitoso. Nuevo saldo:", saldo)
        else:
            print("Fondos insuficientes.")
    elif opcion == "4":
        print("Gracias por usar el cajero.")
        break
    else:
        print("Opción inválida.")
