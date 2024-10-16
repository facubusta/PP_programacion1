#5. Depósito con mayor recaudación, teniendo en cuenta que disponemos de un vector
#con los valores por unidad de cada juguete. Esto se debe hacer con una función que
#reciba la lista de precios por parámetro para poder actualizarlos frente a la inflación.

def calcular_deposito_mayor_recaudacion(existencias: license, precios: list, provincias: list) ->str:
    '''
    Calcala el deposito con mayor recaudacion
    '''
    
    max_recaudacion = 0
    provincia_max = ""

    for i in range(5):
        recaudacion = 0
        for j in range(6):
            recaudacion += existencias[i][j] * precios[j]
        
        if recaudacion > max_recaudacion:
            max_recaudacion = recaudacion
            provincia_max = provincias[i]
    
    return provincia_max