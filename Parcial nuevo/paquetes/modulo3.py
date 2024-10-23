#4. Máxima cantidad de juguetes almacenados de cada tipo. Devolver en qué provincia se encuentran.

def encontrar_juguete_maximo(matriz: list, juguetes: list, provincias: list) ->list:
    '''
    Encuentra el tipo de jueguete con mas cantidad por deposito
    '''

    lista_juguetes = []

    for i in range(len(juguetes)):
        juguete_maximo = float("-inf")
        nombre_provincia = ""
        for j in range(len(matriz)):
            if matriz[j][i] > juguete_maximo:
                juguete_maximo = matriz[j][i]
                nombre_provincia = provincias[j]
        lista_juguetes += [nombre_provincia]
    
    return lista_juguetes


