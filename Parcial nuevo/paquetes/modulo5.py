#6. Cantidad de depósitos que hayan almacenado más de 50.000 unidades entre los 6
#juguetes. Mostrar provincias.

def calcular_limite_alcanzado(matriz: list,  provincias: list) ->list:
    '''
    Calcula que deposito tiene mas de 50.000 juguetes
    '''

    deposito_mayor_limite = []
    
    for i in range(len(matriz)):
        suma = 0
        
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
        if suma > 50000:
            deposito_mayor_limite += [provincias[i]]
    
    return deposito_mayor_limite
           
        

