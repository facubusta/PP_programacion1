#2. Calcular por cada depósito la cantidad total de juguetes almacenados entre todos los
#tipos.

def calcular_cantidad_total_por_deposito(matriz: list) ->list:
    '''
    Calcula la cantidad total de juguetes por deposito 
    '''

    matriz_cantidad = []
    for i in range(len(matriz)):
        cantidad = 0
        for j in range(len(matriz[i])):
            cantidad += matriz[i][j]
        matriz_cantidad += [cantidad]
        
    return matriz_cantidad

