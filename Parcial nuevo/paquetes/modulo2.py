#3. Obtener los nombres de los juguetes que es necesario reponer en cada depósito.
#Crear una función que devuelva todos los juguetes con menos de 500 unidades.

def obtener_juguetes_reponer(matriz: list, juguetes: list) ->list:
    '''
    Obtiene los nombres de juguetes que hay que reponer por deposito
    '''
    
    lista_reponer= []

    for i in range(len(matriz)):
        repo_provincia = []
        for j in range(len(matriz[i])):
            if matriz[i][j] < 500:
                repo_provincia += [juguetes[j]]
        lista_reponer += [repo_provincia]
    
    return lista_reponer
            

            







