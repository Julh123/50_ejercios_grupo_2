mes = input("Ingrese su mes de nacimiento: ").lower()
dia = int(input("Ingrese su día de nacimiento: "))
if (mes == "marzo" and dia >= 21) or (mes == "abril" and dia <= 19):
    print("Aries")
elif (mes == "abril" and dia >= 20) or (mes == "mayo" and dia <= 20):
    print("Tauro")
else:
    print("Otro signo")
