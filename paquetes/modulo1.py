#1. Obtener existencias: para ello deberá cargar en el main la existencia de cada juguete
#en todos los depósitos. En una lista de cantidad, no uno por uno. Por lo que habrá una
#matriz con 3 columnas o filas, provincia, tipo de juguete y cantidad.
def obtener_existencias(provincias: list, juguetes: list, existencias: list) -> list:
    '''
    obtengo la existencia de los juguetes
    '''

    provincias = ["PBA", "CABA", "Chubut", "Tucumán", "Mendoza"]
    juguetes = ["autos", "muñecas", "trenes", "peluches", "spinners", "cartas"]

    existencias = []
    
    for i in range(5):
        deposito = []
       
        for j in range(6):
            cantidad = int(input(f"Ingrese la cantidad de {juguetes[j]} en el deposito de {provincias[i]}: "))
            deposito += [cantidad]
        existencias += [deposito]

    return existencias

def mostrar_juguetes_por_deposito(provincias: list, existencias: list, juguetes: list) ->None:
    '''
    Muestra en pantalla los nombre de los juguetes por deposito
    '''

    for i in range(len(provincias)):
        for j in range(len(juguetes)):
            print("Provincia:", provincias[i], "Juguete:", juguetes[j], "Cantidad:", existencias[i][j])