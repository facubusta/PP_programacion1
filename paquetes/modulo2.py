#2. Calcular por cada depósito la cantidad total de juguetes almacenados 
#entre todos los tipos.

def calcular_juguetes_por_deposito(existencias: list) -> list:
    '''
    Calcula la cantidad de juguetes por deposito 
    '''
   
    
    totales = []

    for i in range(5):
        total = 0
        for j in range(6):
            total += existencias[i][j]
        totales += [total] 

    return totales   

def mostrar_juguetes_almacenados(provincias: list, existencias: list) ->None:
    '''
    Muestra en pantalla los juguetes almacenados
    '''

    for i in range(len(provincias)):
        print("Provincia:", provincias[i], "Cantidad total de juguetes :", existencias[i])




