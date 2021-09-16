#lógica gruesa
"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from os import times
from typing import Awaitable
from Test.sorting.test_shell_linked import cmpfunction
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog(typelist): #Va "typelist" como parametro
#REVISAR PORQUE NEWCATALOG NO PUEDE TENER PARAMETROS
    #type = ""
    #if typelist == "SINGLE_LINKED":
    #    type = "SINGLE_LINKED"
    #elif typelist == "ARRAY_LIST":
    #    type = "ARRAY_LIST"
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'artists': None,  #books->artist
               'artworks': None,}    #authors->artworks

    catalog['artists'] = lt.newList(typelist) #USANDO "type" con el código comentado en vez del tipo de lista
    catalog['artworks'] = lt.newList(typelist)

    return catalog
# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    """
    Adiciona un artist a la lista de artists
    """
    t = (artist['ConstituentID'], artist['DisplayName'], artist['ArtistBio'], #newArtist al inicio si algo 
    artist['Nationality'], artist['Gender'], artist['BeginDate'], artist['EndDate'], 
    artist['Wiki QID'], artist['ULAN'])
    lt.addLast(catalog['artists'], t)

def addArtwork(catalog, artwork):
    """
    Adiciona un tag a la lista de tags
    """
    t = (artwork['ObjectID'], artwork['Title'], artwork['ConstituentID'], #newArtwork al inicio
    artwork['Date'], artwork['Medium'], artwork['Dimensions'], 
    artwork['CreditLine'], artwork['AccessionNumber'], artwork['Classification'], 
    artwork['Department'], artwork['DateAcquired'], artwork['Cataloged'], 
    artwork['URL'], artwork['Circumference (cm)'], artwork['Depth (cm)'], 
    artwork['Diameter (cm)'], artwork['Height (cm)'], artwork['Length (cm)'], 
    artwork['Weight (kg)'], artwork['Width (cm)'], artwork['Seat Height (cm)'], 
    artwork['Duration (sec.)'])
    lt.addLast(catalog['artworks'], t)
# Funciones para creacion de datos

# Funciones de consulta
###primeras dos funciones de REQ1 de Reto1
def getLastsartists (catalog):
    lastsartists = lt.newList()
    u = lt.size(catalog["artists"])
    for i in range(u-2, u+1): #revisar rango
        firstartist = lt.getElement(catalog["artists"], i)
        secondartist = lt.getElement(catalog["artists"], i)
        thirdartist = lt.getElement(catalog["artists"], i)
        lt.addLast(lastsartists, firstartist)
        lt.addLast(lastsartists, secondartist)
        lt.addLast(lastsartists, thirdartist)
    return lastsartists

def getFirstsartists (catalog):
    firstsartists = lt.newList()
    for i in range(1,4):
        firstartist = lt.getElement(catalog["artists"], i)
        secondartist = lt.getElement(catalog["artists"], i)
        thirdartist = lt.getElement(catalog["artists"], i)
        lt.addLast(firstsartists, firstartist)
        lt.addLast(firstsartists, secondartist)
        lt.addLast(firstsartists, thirdartist)
    return firstsartists
"""
#Para REQ1 de Reto1
#def getReq1 (catalog, startyear, endyear): ###falta implementar getFirstartist and getlastartists
#    artists = catalog["artists"]
#    begind = lt.isPresent(artists["BeginDate"], startyear)
#    endd = lt.isPresent(artists["EndDate"], endyear)
#    if (begind > 0) and (endd > 0):
#        #hacer lista con rango ó tener lista momentanea
#        req1list = lt.size(req1lt)
        #buscar en lista ordenada artistas/// usar for i in range usando de range como primero la start year y de último el endyear
        ###Aquí

#    posartist = lt.isPresent(artists, )

"""
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def cmpArtworkByDateAcquired (catalog, artwork, artwork1, artwork2):
    artwork= catalog["artworks"]
    presart1 = lt.isPresent(catalog['artworks'], artwork1)
    presart2 = lt.isPresent(catalog['artworks'], artwork2)
    if ((presart1 > 0) and (presart2 > 0)):
        date1 = lt.isPresent(artwork["DateAcquired"], artwork1)
        date2 = lt.isPresent(artwork["DateAcquired"], artwork2)
        if date1 < date2:
            return True
        else:
            return False
    else:
        print("Alguna de las obras dadas no se encuentra en la base de datos\n verifique los datos ingresados")
    pass
        ###Últimos cambios para ordenamiento de comparación
#FUNCIONES PARA COMPARAR DENTRO DE UNA LISTA

def insertionSort(catalog):
    X = int(lt.size(catalog["artworks"]))
    for i in range(1, X):
        key = catalog["artworks"][i]
  
        j = i-1
        while j >=0 and comparedates(key, catalog["artworks"][j]):
                catalog["artworks"][j+1] = catalog["artworks"][j]
                j -= 1
        catalog["artworks"][j+1] = key

def shellSort(catalog):
  
    n = int(len(catalog))
    gap = int(n/2)
  
    while gap > 0:
        for i in range(int(gap),int(n)):
            temp = catalog[i]
            j = i
            while  j >= gap and catalog[j-gap]['DateAcquired'] >temp['DateAcquired']:
                catalog[j] = catalog[j-gap]
                j -= gap
            catalog[j] = temp
        gap /= 2

def comparedates(artwork1, artwork2):

    return (float(artwork1['DateAcquired']) < float(artwork2['DateAcquired']))

###Dar a elegir el ordenamiento al usuario
def typeord (catalog, ord):

    if ord == "Insertion":
        insertionSort(catalog)
    elif ord == "Shell":
        shellSort(catalog)
    elif ord == "Merge":
        print("")
    elif ord == "QuickSort":
        print("")
    else:
        print("No ha seleccionado un tipo de ordenamiento válido, porfavor intentelo de nuevo")