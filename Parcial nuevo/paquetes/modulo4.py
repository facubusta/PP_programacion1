#5. Depósito con mayor recaudación, teniendo en cuenta que disponemos de un vector
#con los valores por unidad de cada juguete. Esto se debe hacer con una función que
#reciba la lista de precios por parámetro para poder actualizarlos frente a la inflación

def obtener_deposito_mayor_recaudacion(matriz: list, precios: list, provincias: list) ->str:
    '''
    Devuelve el deposito con mayor recaudacion
    '''

    deposito_mayor_recaudacion = ""
    
    for i in range(len(matriz)):
        total = 0
        for j in range(len(matriz[i])):
            mayor = matriz[i][j] * precios[i]
            if mayor > total:
                total = mayor
        deposito_mayor_recaudacion = provincias[i]
        

    return  deposito_mayor_recaudacion
               

