print("Índice de masa corporal")
print("Ingrese su estatura, peso(kg) y edad")
estatura = int(input())
peso = float(input())
edad = int(input())
altura = estatura * estatura
calculo = peso / altura
if edad < 45:
    if calculo < 22.0:
        print("Bajo")
    else:
        print("Medio")
else:
    if calculo < 22.0:
        print("Medio")
    else:
        print("Alto")