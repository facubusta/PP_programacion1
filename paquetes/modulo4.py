#4. Máxima cantidad de juguetes almacenados de cada tipo. Devolver en qué provincia se
#encuentran.

def calcular_maxima_cantidad(existencias: list, provincias: list, juguetes: list) ->list:
    '''
    Calcula la maxima cantidad de juguetes de cada tipo
    y a que provincia pertenece
    '''

    maxima_cantidad = []
    
    for j in range(6):
        max_cantidad = -1
        provincia_max = ""
        for i in range(5):
            if existencias[i][j] > max_cantidad:
                max_cantidad = existencias[i][j]
                provincia_max = provincias[i]
        maxima_cantidad += [[juguetes[j], provincia_max]]
    
    return maxima_cantidad

def motrar_maximo_jueguetes(juguetes: list) ->None:
    '''
    Muestra por pantalla el juguete de mas cantidad
    y la provincia a la que pertenece.
    '''

    for i in range(len(juguetes)):
        print("Juguete: ")
        for j in range(len(juguetes[i])):
            print(juguetes[i][j])
