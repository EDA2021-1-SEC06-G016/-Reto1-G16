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
    print("1- Cargar información en el catálogo.")
    print("2- REQ1 Listar cronológicamente los artistas")
    print("ant2 3real- REQ2/GRUPAL/- Ordenar catalogo de obras por año de adquisición")
    print("4- Clasificar obras de un artista por tecnica")
    print("5- Clasificar obras por nacionalidad de creadores")
    print("6- Transportar obras de un departamento")
    print("ant6 7real- REQ6/BONO/- Proponer un nueva exposición en el museo NO SE HA EMPEZADO")
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
    
def puente(catalog, artist):
    return controller.filterArtist(catalog, artist)
    
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

        typelist = "SINGLE_LINKED" 
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog(typelist)   
        loadData(catalog)

        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        #books -> artist 
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
        #authors->artwork

    elif int(inputs[0]) == 4:
        inputArtist = input('Ingrese un artista: ')

        artists = catalog['artists']
        artworks = catalog['artworks']

        for artist in lt.iterator(artists):
            if (artist[1] == inputArtist):
                constituentID = artist[0]
        controller.printTecnics(inputArtist,artworks,constituentID)
            
    elif int(inputs[0]) == 6:
        departament = input('Ingrese un departamento: ')
        artworks = catalog['artworks']
        controller.printDepartamet(departament, artworks)
    else:
        sys.exit(0)
sys.exit(0)