#NO se hacen funciones grandes
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
 """

from DISClib.ADT.list import size
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
#inicio copia
def initCatalog(typelist):  #Va "typelist" como parametro
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(typelist) #Va "typelist" como parametro
    return catalog


# Funciones para la carga de datos


def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)
    #sortArtist(catalog, size)
    

def loadArtists(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    artistsfile = cf.data_dir + 'Artists-utf8-small.csv' #para cambiar el archivo
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

def loadArtworks(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    artworksfile = cf.data_dir + 'Artworks-utf8-small.csv' #para cambiar el archivo
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

def printTecnics(inputArtist,artworks,constituentID):
    model.printTecnics(inputArtist,artworks,constituentID)

def printDepartamet(departament, artworks):
    model.printDepartamet(departament, artworks)
#final copia
# Inicialización del Catálogo de libros

# Funciones para la carga de datos
        

# Funciones de ordenamiento

def sortArtist(catalog, size):
        """
            Ordena artistas crónologicamente por año de nacimiento
        """
        model.sortArtists(catalog, size)

def getReq1 (catalog, startyear , endyear):
#    """
#        Hace lo solicitado en req 1
#    """
   Req1 = model.getReq1(catalog, startyear, endyear)
   return Req1###Aquí

#REQ2
def getReq2 (catalog, startdate, enddate):
    req2 = model.getReq2(catalog, startdate, enddate)
    return req2

#REQ3

def artworksartist (catalog):
    artworksart = model.getReq3Artwart(catalog)
    return artworksart

def tecnicsartist (catalog):
    tecnics = model.getReq3Tecnicsart(catalog)
    return tecnics

def artworkstecnic (catalog):
    artworkstec = model.getReq3Artwtec(catalog)
    return artworkstec



# Funciones de consulta sobre el catálogo

#Para REQ1 de Reto1
#def getReq1 (catalog,startyear , endyear):
#    """
#        Hace lo solicitado en req 1
#    """
#    Req1 = model.getReq1(catalog, startyear, endyear)
#    return Req1###Aquí