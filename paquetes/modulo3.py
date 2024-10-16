#3. Obtener los nombres de los juguetes que es necesario reponer en cada depósito.
#Crear una función que devuelva todos los juguetes con menos de 500 unidades.

def obtener_juguetes_a_reponer(juguetes: list, existencias: list) -> list:
    '''
    Obtiene los nombres de los juegues a reponer
    '''
    
    reponer = []
    for i in range(5):
        sin_juguetes = []
        for j in range(6):
            if existencias[i][j] < 500:
                sin_juguetes += [juguetes[j]]
        reponer +=[sin_juguetes]

    return reponer 

def mostrar_juguetes_a_reponer(provincias: list, existencias : list) ->None:
    '''
    imprimer por pantalle los juguetes a reponer
    '''       
    for i in range(5):
        if len(existencias[i]) > 0:
            print("Para la provincia:", provincias[i], "hay que reponer:")
            for j in range(len(existencias[i])):
                print(existencias[i][j])
