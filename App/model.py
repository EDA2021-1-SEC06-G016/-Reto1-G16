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


from os import error, times
from typing import Awaitable
from Test.sorting.test_shell_linked import cmpfunction
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
from statistics import mode

"""
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
"""
    
def newCatalog(typelist):
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

def printTecnics(inputArtist,artworks,constituentID):
    filtered_artworks = lt.newList()
    mediums_tecnics = []
    for artwork in lt.iterator(artworks):
        remplaced1 = artwork[2].replace("[","")
        remplaced2 = remplaced1.replace("]","")
        ids = remplaced2.split(sep=',')
        for id in ids:
            if(str(id) == str(constituentID)):
                lt.addLast(filtered_artworks,artwork)
                mediums_tecnics.append(artwork[4])
    moreComom = str(mode(mediums_tecnics))

    print(inputArtist + " con el MOMA ID "+ constituentID + " tiene " + str(lt.size(filtered_artworks))+ " obras en el museo a su nombre.")
    print("Hay " + str(count(mediums_tecnics)) + " tecnicas dierentes en su trabajo, la mas usual es: " + moreComom)
    top = 1
    for i in lt.iterator(filtered_artworks):
        if(i[4] == moreComom):
            print(str(top) + ") Titulo: " + str(i[1])+ ", Fecha de la obra :" + str(i[3]) + ", Medio de la obra: " + str(i[4]) + "Dimensiones:" + str(i[5]))
            top = top + 1

def printDepartamet(departament, artworks):
    filtered_artworks = lt.newList()
    top = 1
    for artwork in lt.iterator(artworks):
        if(departament == artwork[9] ):
            ini = artwork[5].find("(")
            fin = artwork[5].find(")")
            if(ini != -1 and fin != -1):
                fValue = artwork[5][ini+1:fin]
                if("cm" in fValue):
                    convertValue(fValue)
                else:
                    fValue2 = artwork[5][fin+1:]
                    fValue3 = fValue2[fValue2.find("(") + 1:fValue2.find(")")]
                    convertValue(fValue3) 
            else:
                print("no tiene")
            top = top + 1
            print("El total de obras a transporta es:" + str(top)) 
    print(top)
    
#Drawings & Prints
def convertValue(text):
    text1 = text.replace("x","/")
    text1 = text.replace("x","/")
    text2 = text1.replace("cm","")
    num1 = text2[:text2.find("/")]
    num2 = text2[text2.find("/") +1:]
    try:
        return float(num1) * float(num2)
    except:
        return convertValue(num1)

def count(catalog):
    result = []
    for item in catalog:
        if item not in result:
            result.append(item)
    return len(result)

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
