print("Año bisiesto")
print("Ingrese el año")
año = int(input())
if ((año % 4 != 0 or año % 100 == 0) and (año % 100 != 0 or año % 400 != 0)):
    print(str(año) + " no es bisiesto")
else:
    print(str(año) + " es bisiesto")