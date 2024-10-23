from paquetes.modulo1 import *

#7. Porcentaje de juguetes de cada tipo sobre el total de juguetes almacenados. Realizar
#una función que muestre el porcentaje de cada uno.

def calcular_porcetaje_juguetes(matriz: list) ->list:
    '''
    Calcula que porcentaje ocupa 
    cada juguete dentro del deposito
    '''

    lista_porcentaje = []

    for i in range(len(matriz)):
        mayor_porcentaje = []
        for j in range(len(matriz[i])):
            mayor_porcentaje += [round((matriz[i][j] / calcular_cantidad_total_por_deposito(matriz)[i] * 100), 2)]
             
        lista_porcentaje += [mayor_porcentaje]

    return lista_porcentaje