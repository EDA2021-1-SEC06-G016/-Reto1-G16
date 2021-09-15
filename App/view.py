#view llama a controller para imp
"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo, en tipo Array_list o Linked_list")
    print("Pre2/lab4/- GUIAAAA BORRAR, cmpartwork... punto de Lab4, darle a elegir al usuario la muestra y verificar que no exceda lo cargado en memoria")
    print("2- REQ2/GRUPAL/- Ordenar catalogo de obras por año de adquisición \n /Debe elegir el tipo de algortimo de ordenamiento/")
    print("3- REQ3/INDIVIDUAL/- Clasificar obras de un artista por tecnica NO SE HA EMPEZADO")
    print("4- REQ4/INDIVIDUAL/- Clasificar obras por nacionalidad de creadores NO SE HA EMPEZADO")
    print("5- REQ5/GRUPAL/- Transportar obras de un departamento NO SE HA EMPEZADO")
    print("6- REQ6/BONO/- Proponer un nueva exposición en el museo NO SE HA EMPEZADO")
    print("0- Salir")

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)
    
catalog = None

"""
#revisar el input de función printreq1
def printReq1():
    size = ###Aquí
"""
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:

        #typelist = input("Indique el tipo de lista para cargar los datos/ARRAY_LIST;SINGLE_LINKED/: ")
        #if typelist == "SINGLE_LINKED" or "ARRAY_LIST":
        #    print("Cargando información de los archivos ....")
        #    catalog = controller.initCatalog(typelist)   
        #    loadData(catalog)
        #    print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
            #books -> artist 
        #    print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
            #authors->artwork
        #else:
        #    print("No ha ingresado una opción válida, por favor ingrese una opción válida")
        #pass

        #Código original para dar funcionamiento por defecto con "SINGLE_LINKED"
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
       #books -> artist 
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
       #authors->artwork
        #Código original para cargar archivos termina

    #Para REQ1 de Reto1
    #elif int(inputs[0]) == 2:
    #    startyear = input("Año de inicio de rango a buscar: ")
    #    endyear = input("Año final de rango a buscar: ")
    #    req1 = controller.getReq1(catalog, int(startyear), int(endyear))
    #    printReq1(req1)
    #    pass

    else:
        sys.exit(0)
sys.exit(0)
