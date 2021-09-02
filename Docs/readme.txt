Responder preguntas y marcar con el nombre de los integrantes
Nombres y códigos:
Req. 2 - Juan Sebastián Castro Garay, 201813107, js.castrog@uniandes.edu.co
Req. 3 - Daniel Felipe Piñeros Montenegro, 202013147, d.pinerosm@uniandes.edu.co
Preguntas:
1)	¿Cuáles son los mecanismos de interacción (I/O: Input/Output) que tiene el view.py con el usuario?
 
 ***Mecanismos de interacción de salidas y entradas
 def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar los Top x libros por promedio")
    print("3- Consultar los libros de un autor")
    print("4- Libros por género")
    print("0- Salir")

    inputs=input("Seleccione una opción para continuar\n")

Los output son mecanismos que se usan en el view.py para mostrar elementos al usuario, en este caso en la función printMenu(), por otro lado los inputs son los mecanismos que se usan para que el usuario ingrese datos, cadenas de textos y valores entre otros, en el view.py se utilizan para seleccionar una opción.

2)	¿Cómo se almacenan los datos de GoodReads en el model.py?

La herramienta de almacenamiento depende de lo que se le asigne a newList, en este caso este es: “SINGLE_LINKED” lo que significa que es una lista encadenada.

 ***Fragmento de código
 catalog["autolog"] = lt.newlist("SINGLE_LINKED",
                                cmpfunction=compareauthors)

3)	¿Cuáles son las funciones que comunican el  view.py y el model.py?
view.py: Esta encargado de interactuar con el usuario, ya sea pedirle o mostrarle datos a este.
model.py: Esta encargado de ejecutar las acciones solicitadas por el usuario.
4)	¿Cómo se crea una lista?
 
 ***Ejemplo del lab de cómo crear una lista
    catalog = {"books" : None,
                "authors": None,
                "tags": None,
                "book_tags": None}
    catalog["books"] = lt.newList()
    catalog["authors"] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=compareauthors)

Primero se asignan el nombre que tendrá esta, luego se llama a la funcion newList que es la cargada de inicializar la lista vacia. 
5)	¿Qué hace el parámetro cmpfunction=None en la función newList()?


6)	¿Qué hace la funció addLast()?
Agrega a una lista ya existente un elemento en la última posición. 

7)	¿Qué hace la función getElement()?

Retorna el elemento de una posición especifica, siendo la posición del elemento en la lista a preguntar el parámetro de esta función.

8)	¿Qué hace la función subList()?
Permite extraer un subconjunto de elementos en ubicaciones especificas (parámetro), creando a partir de los elementos seleccionados una lista aparte, aunque no desconectada de la original, debido a que en caso de eliminar o modificar algo en la lista del subconjunto este cambio también se verá reflejado en la lista original. Es un método para usar con precaución en pro de no ocasionar daños en el código.

9)	¿Observó algún cambio en el comportamiento del programa al cambiar la implementación del parámetro “ARRAY_LIST” a “SINGLE_LINKED”?

No vimos una diferencia notable al cambiar “ARRAY_LIST” a “SINGLE_LINKED” tal vez se deba al procesador del computador o a que el numero de datos no es demasiado grande.
Pero sabemos que “ARRAY_LIST” es una contenedora y “SINGLE_LINKED” una lista, lo que debe intervenir en el tiempo de procesamiento.

