from paquetes.modulo1 import *
from paquetes.modulo2 import *
from paquetes.modulo3 import *
from paquetes.modulo4 import *
from paquetes.modulo5 import *

#1
provincias = ["PBA", "CABA", "Chubut", "Tucumán", "Mendoza"]
juguetes = ["autos", "muñecas", "trenes", "peluches", "spinners", "cartas"]
existencias =[]
existencias = obtener_existencias(provincias, juguetes, existencias)
mostrar_juguetes_por_deposito(provincias, existencias, juguetes)


#2
almacenados = calcular_juguetes_por_deposito(existencias)
mostrar_juguetes_almacenados(provincias, almacenados)


#3
menor_juguete = obtener_juguetes_a_reponer(juguetes, existencias)
mostrar_juguetes_a_reponer(provincias, menor_juguete)

#4
maximo = calcular_maxima_cantidad(existencias, provincias, juguetes)
motrar_maximo_jueguetes(maximo)

#5
precios = [200, 350, 450, 400, 500, 600]
print("La provincia con mayor recaudacion es: ", calcular_deposito_mayor_recaudacion(existencias, precios, provincias))