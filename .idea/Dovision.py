print("Divisor")
print("Ingrese el dividendo y el divisor")
divd = float(input())
divs = float(input())
dividir = divd / divs
residuo = divd % divs
if residuo != 0.0:
    print("La división no es exacta.")
else:
    print("La división es exacta.")

print("cociente:", dividir)
print("Residuo:", residuo)