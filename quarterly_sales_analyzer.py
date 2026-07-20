#Universidad Fidelitas
#Rafael Angel Brenes Quirós
#Programación Básica
#Caso Evaluado II

ventas = []

for tienda in range(4):
    fila = []
    for mes in range(4):
        venta =float(input(f"Ingrese la venta de la tienda {tienda +1},mes {mes +1}: "))
        fila.append(venta)
    ventas.append(fila)


print("\nVentas en forma de Matriz:")
for fila in ventas:
    for valor in fila:
        print(f"{valor:10.2f}", end=" ")
    print()


total_ventas=0
contador_menores=0
contador_mayores=0

for fila in ventas:
    for venta in fila:
        total_ventas += venta
        if venta <= 2000:
            contador_menores +=1
        else:
            contador_mayores +=1
promedio_ventas = total_ventas / 16


print("\nEmpresa: MercaFide")
print(f"Total de ventas del cuatrimestre:${total_ventas:.2f}")
print(f"Promedio de ventas del cuatrimestre:${promedio_ventas:.2f}")
print(f"Cantidad de ventas menores o iguales a $2000: {contador_menores}")
print(f"Cantidad de ventas mayores a $2000: {contador_mayores}")


