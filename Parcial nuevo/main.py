from paquetes.modulo1 import *
from paquetes.modulo2 import *
from paquetes.modulo3 import *
from paquetes.modulo4 import *
from paquetes.modulo5 import *
from paquetes.modulo6 import *
from paquetes.modulo7 import *



matriz = []
juguetes =  ["autos", "muñecas", "trenes", "peluches", "spinners", "cartas"]
provincias = ["PBA", "CABA", "Chubut", "Tucumán", "Mendoza"]
cantidades_pba = [50000, 600, 700, 800, 900, 1000]
cantidades_caba = [1100, 120000, 50 , 68, 70, 1000]
cantidades_chubut = [230, 500, 505, 800, 900, 80]
cantidades_tucuman = [2500, 5000, 28, 5000, 1011, 90]
cantidades_mendoza = [560, 2400, 99000, 450, 120, 908]

#inicializo matriz
for _ in range(len(provincias)):
    fila = [0] * len(juguetes)
    matriz += [fila]

#carga de matriz 
'''for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f"Ingrese la cantidad de {juguetes[j]}, para el deposito de {provincias[i]}: "))'''


matriz[0] = cantidades_pba
matriz[1] = cantidades_caba
matriz[2] = cantidades_chubut
matriz[3] = cantidades_tucuman
matriz[4] = cantidades_mendoza

#imprimir en patalla 
print("--------------------Ejercicio_1-------------------------")
print(f"{provincias[0]}: {matriz[0]}")
print(f"{provincias[1]}: {matriz[1]}")
print(f"{provincias[2]}: {matriz[2]}")
print(f"{provincias[3]}: {matriz[3]}")
print(f"{provincias[4]}: {matriz[4]}")
print("--------------------Ejercicio_2-------------------------")

#2
total = calcular_cantidad_total_por_deposito(matriz)
for i in range(len(total)):
    print(f"En {provincias[i]} hay {total[i]} juguetes")
print("-------------------Ejercicio_3-------------------------")

#3
juguetes_faltantes = (obtener_juguetes_reponer(matriz, juguetes))
for i in range(len(juguetes_faltantes)):
    if len(juguetes_faltantes[i]) > 0:
        print(f"En {provincias[i]} faltan: ")
        for j in range(len(juguetes_faltantes[i])):
            print(f"{juguetes_faltantes[i][j]}")
    else:
        print(f"En {provincias[i]} no hay juguetes faltantes.")
print("--------------------Ejercicio_4------------------------")

#4
juguete_maximo = encontrar_juguete_maximo(matriz, juguetes, provincias)
for i in range(len(juguete_maximo)):
    print(f"Donde hay mas {juguetes[i]} es en {juguete_maximo[i]}")
print("--------------------Ejercicio_5-----------------------")

#5
precios = [30, 55, 90, 102, 55, 69]
deposito_mayor = obtener_deposito_mayor_recaudacion(matriz, precios, provincias)
print(f"El deposito con mayor recaudacion es {deposito_mayor}")
print("-------------------Ejercicio_6------------------------")

#6
provincias_limite = calcular_limite_alcanzado(matriz, provincias)
print("Las provincias que superan los 50.000 juguetes en sus depositos son: ")
for i in range(len(provincias_limite)):
    print(f"*{provincias_limite[i]}")
print("-------------------Ejercicio_7------------------------")

#7'
porcentajes = calcular_porcetaje_juguetes(matriz)
for i in range(len(porcentajes)):
    print(f"En {provincias[i]} : ")
    for j in range(len(porcentajes[i])):
      print(f"el {porcentajes[i][j]}% son {juguetes[j]}")
print("-------------------Ejercicio_8------------------------")
recaudacion = calcular_recaudacion_por_deposito(matriz, precios, provincias)
for i in range(len(recaudacion)):
    print(f"La recaudacion de {recaudacion[i][1]} es de ${recaudacion[i][0]}")
    #for j in range(len(recaudacion[i])):
        #print(recaudacion[i][j])
    


    