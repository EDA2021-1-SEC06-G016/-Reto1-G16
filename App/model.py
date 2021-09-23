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
def ordgetReq2 (catalog, cmpfunction): #Ordenar por DateAcquired
    req1cat = catalog["artist"]
    size = lt.size(req1cat)
    if size > 1:
        mid = (size // 2)
        """se divide la lista original, en dos partes, izquierda y derecha,
        desde el punto mid."""
        leftlist = lt.subList(req1cat, 1, mid)
        rightlist = lt.subList(req1cat, mid+1, size - mid)

        """se hace el llamado recursivo con la lista izquierda y derecha"""
        ordgetReq2(leftlist, cmpfunction)
        ordgetReq2(rightlist, cmpfunction)

        """i recorre la lista izquierda, j la derecha y k la lista original"""
        i = j = k = 1

        leftelements = lt.size(leftlist)
        rightelements = lt.size(rightlist)

        while (i <= leftelements) and (j <= rightelements):
            elemi = lt.getElement(leftlist["BeginDate"], i)
            elemj = lt.getElement(rightlist["BeginDate"], j)
            """compara y ordena los elementos"""
            if cmpfunction(elemj, elemi):   # caso estricto elemj < elemi
                lt.changeInfo(req1cat, k, elemj)
                j += 1
            else:                            # caso elemi <= elemj
                lt.changeInfo(req1cat, k, elemi)
                i += 1
            k += 1

        """Agrega los elementos que no se comprararon y estan ordenados"""
        while i <= leftelements:
            lt.changeInfo(req1cat, k, lt.getElement(leftlist, i))
            i += 1
            k += 1

        while j <= rightelements:
            lt.changeInfo(req1cat, k, lt.getElement(rightlist, j))
            j += 1
            k += 1
    return req1cat

def getReq1size (req1cat, startyear, endyear): #Cantidad de obras de range
    i = 0
    date1 = datetime.date(startyear)
    date2 = datetime.date(endyear)
    pos1 = lt.isPresent(req1cat, startdate)
    pos2 = lt.isPresent(req1cat, enddate)
    elem = pos2 - pos1
    if pos1 > 0:
        if pos2 > 0:
            rangecat = lt.subList(req2cat, req2cat[pos1], elem)
        else:
            print("No se ha seleccionado una fecha de final válida")
    else:
        print("No se ha seleccionado una fecha de inicio válida")
    rangesize = lt.size(rangecat)
    return rangesize

###Funciones REQ2 de Reto1

def ordgetReq2 (catalog, cmpfunction): #Ordenar por DateAcquired
    req2cat = catalog["artworks"]
    size = lt.size(req2cat)
    if size > 1:
        mid = (size // 2)
        """se divide la lista original, en dos partes, izquierda y derecha,
        desde el punto mid."""
        leftlist = lt.subList(req2cat, 1, mid)
        rightlist = lt.subList(req2cat, mid+1, size - mid)

        """se hace el llamado recursivo con la lista izquierda y derecha"""
        ordgetReq2(leftlist, cmpfunction)
        ordgetReq2(rightlist, cmpfunction)

        """i recorre la lista izquierda, j la derecha y k la lista original"""
        i = j = k = 1

        leftelements = lt.size(leftlist)
        rightelements = lt.size(rightlist)

        while (i <= leftelements) and (j <= rightelements):
            elemi = lt.getElement(leftlist["DateAcquired"], i)
            elemj = lt.getElement(rightlist["DateAcquired"], j)
            """compara y ordena los elementos"""
            if cmpfunction(elemj, elemi):   # caso estricto elemj < elemi
                lt.changeInfo(req2cat, k, elemj)
                j += 1
            else:                            # caso elemi <= elemj
                lt.changeInfo(req2cat, k, elemi)
                i += 1
            k += 1

        """Agrega los elementos que no se comprararon y estan ordenados"""
        while i <= leftelements:
            lt.changeInfo(req2cat, k, lt.getElement(leftlist, i))
            i += 1
            k += 1

        while j <= rightelements:
            lt.changeInfo(req2cat, k, lt.getElement(rightlist, j))
            j += 1
            k += 1
    return req2cat

def getReq2size (req2cat, startdate, enddate): #Cantidad de obras de range
    #En caso de tener que pasar las fechas del catalogo por datetime.date
    #x = startdate.split("-")
    #y = enddate.split("-")
    #startd = (int(x[0]),int(x[1]),int(x[2]))
    #endd = (int(y[0]),int(y[1]),int(y[2]))
    #date1 = datetime.date(startd)
    #date2 = datetime.date(endd)
    pos1 = lt.isPresent(req2cat, startdate)
    pos2 = lt.isPresent(req2cat, enddate)
    elem = pos2 - pos1
    if pos1 > 0:
        if pos2 > 0:
            rangecat = lt.subList(req2cat, req2cat[pos1], elem)
        else:
            print("No se ha seleccionado una fecha de final válida")
    else:
        print("No se ha seleccionado una fecha de inicio válida")
    rangesize = lt.size(rangecat)
    return rangesize

def getLastsartwork (rangecat): #Últimas 3
    lastsartworks = lt.newList()
    u = lt.size(rangecat["artwork"])
    for i in range(u-2, u+1): #revisar rango
        firstartwork = lt.getElement(rangecat["artwork"], i)
        secondartwork = lt.getElement(rangecat["artwork"], i)
        thirdartwork = lt.getElement(rangecat["artwork"], i)
        lt.addLast(lastsartworks, firstartwork)
        lt.addLast(lastsartworks, secondartwork)
        lt.addLast(lastsartworks, thirdartwork)
    return lastsartworks

def getFirstsartworks (rangecat): #Primeras 3 
    firstsartworks = lt.newList()
    for i in range(1,4):
        firstartwork = lt.getElement(rangecat["artwork"], i)
        secondartwork = lt.getElement(rangecat["artwork"], i)
        thirdartwork = lt.getElement(rangecat["artwork"], i)
        lt.addLast(firstsartworks, firstartwork)
        lt.addLast(firstsartworks, secondartwork)
        lt.addLast(firstsartworks, thirdartwork)
    return firstsartworks

def getReq2purchase (rangecat, rangesize): #Tamaño de obras por "Purchase"
    partworks = lt.newList()
    i = 0
    while i < rangesize:
        if rangecat[i]["CreditLine"] == "Purchase":
            lt.addLast(partworks, rangecat[i])
        i +=1
    psize = lt.size(partworks)
    return psize

    return None
# REQ 3
def getReq3Artwart (catalog, name):
    i = 0
    artists = catalog["artist"]
    size = lt.size(catalog["artist"])
    artwart = lt.newList()
    #if lt.isPresent(catalog["artist"], name) == True:
        while i < size:
            if (artists[i]["DisplayName"]) == name:
                if lt.isPresent( artwart,artists[i]["DisplayName"]) == True:
                    artwart[name]
            i+=1

    pass


def getReq3Artwtec (catalog, name):
    
    return None

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
