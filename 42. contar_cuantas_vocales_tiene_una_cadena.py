texto = input("Ingrese una cadena de texto: ").lower()
vocales = sum(1 for c in texto if c in "aeiou")
print("Cantidad de vocales:", vocales)
