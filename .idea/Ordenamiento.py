print("Ordenamiento")
print("Ingrese cuatro números")

areg = []
for i in range(4):
    num = int(input())
    areg.append(num)

fin = sorted(areg)
print("Los números son: ")

for num in fin:
    print(num)