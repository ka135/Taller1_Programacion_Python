print("Número o letra")
caracter = input("Ingrese un caracter ")
if caracter.isalpha():
    print("Es una letra")
elif caracter.isdigit():
    print("Es un número")
else:
    print("No es ni letra ni número.")