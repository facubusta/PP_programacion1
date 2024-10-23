#8. Generar un informe con la recaudación de cada depósito, ordenada de mayor a menor
#usando insertion sort o quick sort. Justificar la elección del algoritmo. Para ello la
#función deberá recibir una matriz de ventas, y una lista de precios.
#voy a usar insertion sort ya que es mejor cuando la lista es mas pequeña

def calcular_recaudacion_por_deposito(matriz: list, precios: list, provincias: list) ->list:
    '''
    Calcula la recaudacion de cada deposito y ordena 
    de mayor a menor utilizando isertion sort
    '''

    recaudaciones = []
    
    
    for i in range(len(matriz)):
        recaudacion_deposito = 0 
        
        for j in range(len(matriz[i])):            
            recaudacion_deposito += matriz[i][j] * precios[j]

        provincia = [recaudacion_deposito]
        provincia += [provincias[i]]
        recaudaciones += [provincia]
        
    for i in range(1, len(recaudaciones)):
        auxiliar = recaudaciones[i]
        j = i

        while j > 0 and recaudaciones[j - 1] < auxiliar:
            recaudaciones[j] = recaudaciones[j - 1]
            j -= 1

        recaudaciones[j] = auxiliar
   

    return recaudaciones
    
        
        
    


