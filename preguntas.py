"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
data = open("data.csv", "r").readlines()
data = [row.replace("\t",",") for row in data]
data = [row.replace("\n", "") for row in data]
data = [row.split(",") for row in data]


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    column=1
    
    return sum(int(row[column]) for row in data)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    def countX(lst, x):
      count = 0
      for ele in lst:
        if (ele == x):
          count = count + 1
      return count
    lista_punto = [x[0] for x in data]  
    list_set = set(lista_punto)
    unique_list = (list(list_set))
    letras = [x for x in unique_list]
    result = []
    for letra in letras:
       resultado = countX( lista_punto ,letra)
       result.append((letra,resultado ))
    return print(sorted(result))

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    lista_punto = [(x[0],x[1]) for x in data]   
    lista_punto1 = [x[0] for x in lista_punto]  
    list_set = set(lista_punto1)
    unique_list = (list(list_set))

    letras = [x for x in unique_list]


    resultado = []
    for letra in letras:
      result= []
      for element in lista_punto:
        if element[0]==letra:
          result.append(int(element[1]))
          result2 = sum(result)
          answer = (element[0],result2)
      resultado.append(answer)  
    return print(sorted(resultado))


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    dat = [row[2].split("-") for row in data]
    #dat
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    resultado=[]
    for month in months:
      result=[]
      for x in dat:
        if month == x[1]:
          result.append(int(x[1]))
          result2 = len(result)
          answer = (x[1],result2)
      resultado.append(answer)
    return resultado


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    lista_punto = [(x[0],x[1]) for x in data] 
    lista_punto1 = [x[0] for x in lista_punto]  
    list_set = set(lista_punto1)
    unique_list = (list(list_set))

    letras = [x for x in unique_list]

    resultado=[]
    for letra in letras:
      result=[]
      for x in lista_punto:
        if letra == x[0]:
          result.append(int(x[1]))
          result2 = min(result)
          result3 = max(result)
          answer = (x[0],result3,result2)
      resultado.append(answer) 
    return print(sorted(resultado))


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    parte_1 =[row[0:3] for row in data]
    parte_1[0:2]

    #Part_2- tiene las letras del medio
    lista_letras = [[value for value in row if len(value) == 1] for row in data]
    lista_letras = [row[2:] for row in lista_letras]
    largo_maximo_letras =max([len(row) for row in lista_letras])

    parte_2 = []
    lista_temporal = []
    for row in lista_letras:
      for i in range(len(row)):
        lista_temporal.append(row[i])
      while len(lista_temporal) < largo_maximo_letras:
        lista_temporal.append('')
      parte_2.append(lista_temporal)
      lista_temporal = []
    parte_2[0:2]

    #Part_3 - Contiene los diccionarios
    lista_diccionario = [[value for value in row if len(value) >=5] for row in data]
    lista_diccionario = [row[1:] for row in lista_diccionario]

    diccionario = {}
    parte_3 = []
    for row in lista_diccionario:
      for i in range(len(row)):
        a,b =row[i].split(":")
        diccionario[a] = int(b)
      parte_3.append(diccionario)
      diccionario = {}
    parte_3[0:2]

    list(zip(parte_1,parte_2,parte_3))[0]

    datad = []
    lista_intermedia = []
    lista_temporal = []

    for row in list(zip(parte_1,parte_2)):
      for element in row:
        for value in element:
          lista_intermedia.append(value)
      datad.append(lista_intermedia)
      lista_intermedia = []

    for i in range(len(datad)):
      datad[i].append(parte_3[i])

    datad[0:3]


    resultado = []
    llaves_unicas =set()
    for row in [list(row[7].keys()) for row in datad]:
      for element in row:
        llaves_unicas.add(element)
    llaves_unicas

    for value in llaves_unicas:
      resultado.append((value,min([row[7][value] for row in datad if value in list(row[7].keys())]),max([row[7][value] for row in datad if value in list(row[7].keys())])))
    resultado

    resultado = sorted(resultado, key=lambda valor : valor[0])
    return resultado


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    columna1_2=[[x[1], x[0]] for x in data]
    columna1=sorted(set([x[1] for x in data])) # Aqui se indica que se organice en orden descendente los numero y que solo imprima un numero, y no de forma repetida.
    resultfinal=[]# Se crea un diccionario para poder almacenar los datos. 

    #En el siguiente fragmento de código se itera en la columna1 y dos, en la cual se le indica que imprima por cada numero las letras que este contiene. 

    for k in columna1:
      n=[]
      for f in columna1_2:
        if k == f[0]:
          n=n+[f[1]]
   
      result1=(k,n)
      a = print(result1)
    return a


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    columnajuntas=[[x[1], x[0]] for x in data]
    columnauna=sorted(set([x[1] for x in data])) 
    for k in columnauna:
      n=[]
      for f in columnajuntas:
        if k == f[0]:
          n=n+[f[1]]
          result1=n
          resultanlist= []
          
          for element in result1:
            if element not in resultanlist:
              resultanlist.append(element)
      b= print((k,resultanlist))
    return b


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    colum5_1=[x[5:]  for x in data] 

    columnaA=[]
    for i in colum5_1:
      row = []
      for x in i:
        if len(x)>=5:
          row.append(x)

      columnaA.append(row)
  
    columnaB=[]
    for i in columnaA:
      for a in i:
        columnaB.append(a)
    columnaB=sorted(columnaB)

    columnaC=[]
    columnaD=[x.replace(":",",") for x in columnaB] 
    columnaD=[x.split(",") for x in columnaD]
    columnaE=set([x[0] for x in columnaD])
    resultfinal=[]

    for k in columnaE:
      n=[]
      for f in columnaD:
        if k == f[0]:
          n=n+[f[1]]
      result1=[k,len(n)]
  
      resultfinal=resultfinal+[result1]
  
    resultfinal = sorted(resultfinal)

    for valor in resultfinal:
      columf= valor[0]+","+str(valor[1])
      c=print(columf)
    return c


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    import csv

    colum0 = [line[0] for line in data]
    colum3 = [line[3:] for line in data]
    datosa= [[fila for fila in line if len(fila) == 1] for line in colum3]
    datosb = [[fila for fila in line if len(fila) >4] for line in colum3]
    datosc = [[colum0[i], len(datosa[i]), len(datosb[i])] for i in range(len(colum3))]
 
    with open( "y.csv", 'w', newline='') as y_file:
         writer = csv.writer(y_file, quoting=csv.QUOTE_NONE,delimiter=',')
         writer.writerows(datosc)
    d = print(open("y.csv", "r").read())
    return d


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    colum2 = [[fila for fila in line if len(fila) == 1] for line in data]
    colum2 = [line[1:] for line in colum2]
    culum3 = [line[2:] for line in colum2]
    lst = []
    for valores in culum3:
      for vaina in valores:
        lst = lst+[vaina]
    lst = set(list(lst))
    lst=sorted(lst)
    respuesta = []
    for numerico in lst:
      num = [numerico]
      contador = 0
      for fila in colum2:
        if numerico in fila:
          contador = contador + int(fila[0])
      num = num + [contador]
      respuesta = respuesta + [num]
    for line in respuesta:
      final = line[0]+","+str(line[1])
      e=print(final)
    return e


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import re

    rows = [(line[0], str(line[5:])) for line in data]
    arab = []
    result = []
    for i in rows:
      f = print(i[0]+','+str(sum([int(j) for j in re.findall(r'-?\d+\.?\d*', i[1])])))
    return f
 
