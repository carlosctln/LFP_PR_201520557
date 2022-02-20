#from unicodedata import name
import matplotlib.pyplot as plt

from codecs import EncodedFile
from encodings import utf_8
from fileinput import filename
from tkinter import Image, filedialog, Tk
from PIL import Image
import webbrowser
import operator

from numpy import tile

aux = ''
aux1 = ''
data = ''
instrucciones = ''

listaProductos = []
listaProductos1 = []
listNomPro = []
listNomPro1 = []
listTotPro = []
listProG = []

dicProductos = {}
dicInstrucciones = {}
dicInstrucciones1 = {}
dicInstrucciones2 = {}
dicReportes = {}


def menu (opcion):
    try:    
        while opcion != 5:
            
            print('╔══════════════════════════════════════════╗')
            print('║                   Menú                   ║')
            print('║══════════════════════════════════════════║')
            print('║ 1. Cargar Data.                          ║')
            print('║ 2. Cargar Instrucciones.                 ║')
            print('║ 3. Analizar.                             ║')
            print('║ 4. Reportes.                             ║')
            print('║ 5. Salir.                                ║')
            print('╚══════════════════════════════════════════╝')
            opcion = int(input("Elige un número del menú de opciones: "))
            OpcionesDelMenu(opcion)
            print("") 
    except Exception as e:
        if opcion == 2:
            print()
            print('Debes cargar un archivo con extensión .lfp')
        elif opcion == 1:
            print()
            print('Debes cargar un archivo con extensión .data')
        elif opcion == 4:
            print()
            print('No se pueden generar reportes')
        else:
            print()
            print("¡Has cometido un error vuelve a intentarlo!")
            print(type(e).__name__)
        opcion = 0
        menu(opcion)


def OpcionesDelMenu(opcion): 
    if opcion == 1:
        LeerArchivoData()
    elif opcion == 2:
        LeerArchivoInstrucciones()
    elif opcion == 3:
        Analizar()
    elif opcion == 4:
        Reportes()
    elif opcion == 5:
        print("¡Programa finalizado!")
    else:
        print("\n¡La opción que has elegido no existe!")


def LeerArchivoData():
    global data
    data = ''
    Tk().withdraw()
    archivo = filedialog.askopenfilename(
        title= 'Seleccionar un archivo',
        filetypes=[('Archivo Data', '*.data'),
        ('All Files', '*')])
    with open(archivo, 'r', encoding='utf8') as file:
        if archivo is None:
            print('No se seleccionó ningun archivo\n')
            return None
        else:
            data = file.read()
            data = data.lower()
            file.close()
            print('Lectura exitosa\n')


def LeerArchivoInstrucciones():
    global instrucciones
    instrucciones = ''
    Tk().withdraw()
    archivo = filedialog.askopenfilename(
        title= 'Seleccionar un archivo',
        filetypes=[('Archivo LFP', '*.lfp'),
        ('All Files', '*')])
    with open(archivo, 'r', encoding='utf8') as file:
        if archivo is None:
            print('No se seleccionó ningun archivo\n')
            return None
        else:
            instrucciones = file.read()
            instrucciones = instrucciones.lower()
            file.close()
            print('Lectura exitosa\n')


def Analizar():
    if data != '' and instrucciones != '':
        print('Archivos cargados correctamente')
        RecorrerArchivos()
    else:
        print()
        print('Debes cargar dos archivos uno con extensión .data y el otro con extensión .lfp')

def RecorrerArchivos():
    # Recorremos el archivo .data
    global aux
    global aux1
    aux = ''
    aux1 = ''
    parA = 0
    parC = 0
    corA = 0
    corC = 0
    menor = 0
    mayor = 0
    intA = 0
    intC = 0
    year = ''
    mes = ''
    dato = ''
    listaProductos = []
    listaProductos1 = []

    for dato in data:
        if dato == '\t':
            continue
        elif dato == '\n':
            continue
        aux += dato

    for c in aux:
        if c in aux:
            if c != ':':
                if c != '=':
                    if c != '(':
                        if c != ')':
                            if c != ';':
                                if c != '[':
                                    if c != ']':
                                        aux1 += c
            if c == ':':
                mes = aux1
                aux1 = ''
            if c == '=':
                year = aux1
                aux1 = ''
            if c == ';':
                aux1 = aux1.strip()
                listaProductos.append(aux1)
                aux1 = ''
            if c == '(':
                parA = parA + 1
            if c == ')':
                parC = parC + 1
            if c == '[':
                corA = corA + 1
            if c == ']':
                corC = corC + 1

    if parA == 1 and parC == 1:
        pass
    else:
        print('Error parentesis incorrectos!')
        opcion = 0
        menu(opcion)

    if corA == corC:
        pass
    else:
        print('Error corchetes incorrectos!')
        opcion = 0
        menu(opcion)
    
    aux1 = ''
    aux1 = mes
    mes = aux1.strip()
    aux1 = ''

    if mes == 'enero':
        pass
    elif mes == 'febrero':
        pass
    elif mes == 'marzo':
        pass
    elif mes == 'abril':
        pass
    elif mes == 'mayo':
        pass
    elif mes == 'junio':
        pass
    elif mes == 'julio':
        pass
    elif mes == 'agosto':
        pass
    elif mes == 'septiembre':
        pass
    elif mes == 'octubre':
        pass
    elif mes == 'noviembre':
        pass
    elif mes == 'diciembre':
        pass
    else:
        print('Has introducido un mes no valido!')
        opcion = 0
        menu(opcion)

    aux1 = year
    year = int(aux1.strip())
    aux1 = ''
    aux =''

    if year > 0:
        pass
    else:
        print('Has introducido un año no valido!')
        opcion = 0
        menu(opcion)

    # Recorremos el archivo .lfp
    for i in instrucciones:
        if i =='<':
            menor = menor + 1
            continue
        elif i == '¿':
            intA = intA + 1
            continue
        elif i == '>':
            mayor = mayor + 1
            continue
        elif i == '?':
            intC = intC + 1
        elif i == '\n':
            continue
        elif i == '\t':
            continue
        aux += i

    if menor == 1 and mayor == 1:
        if intA == 1 and intC == 1:
            pass
        else:
            print('Error en los signos de interrogación')
            opcion = 0
            menu(opcion)
    else:
        print('Error en los signos de signos de mayor y menor que')
        opcion = 0
        menu(opcion)

    listaValores = []
    listaLlaves = []
    listIns = []

    for i in aux:
        while i != ',':
            aux1 += i
            break
        if i == ',' or i == '?':
            listIns.append(aux1.replace('?','',1))
            aux1 = ''
    aux = ''
    aux1 = ''
    cont = 0
    for ele in listaProductos:
        listaProductos1.append(ele.split(','))
    
    for ele in listaProductos1:
        if len(ele) != 3:
            print('Error en la catidad de elementos del producto')
            opcion = 0
            menu(opcion)
        for e in ele:
            if e == '' or e == ' ':
                print('Error en la catidad de elementos del producto')
                opcion = 0
                menu(opcion)
    tot = 0
    for ele in listaProductos1:
        for i in range(len(ele)):
            try:
                ele[1] = float(ele[1])
                ele[2] = int(ele[2])
                #tot = ele[1] * ele[2]
                tot = "{0:.2f}".format(ele[1] * ele[2])
                ele.append(tot)
                listaProductos[i] = ele
                break
            except:
                print('El producto contiene caracteres y no números')
                opcion = 0
                menu(opcion)
    global listProG
    listProG = listaProductos1

    for ele in listaProductos1:
        for i in range(len(ele)):
            if ele[1] <= 0 or ele[2] <= 0:
                print('Error ingresa valores mayores o iguales a 1')
                opcion = 0
                menu(opcion)

    listNomPro = []

    for ele in listaProductos1:
        for i in range(len(ele)):
            listNomPro.append(ele[0])
            listTotPro.append(ele[1] * ele[2])
            break
    
    aux = ''
    for ele in listNomPro:
        aux = ele.replace('“', '', 1)
        ele = aux.replace('”', '', 1)
        ele = ele.replace('"', '', 2)
        listNomPro1.append(ele)

    global dicProductos
    for i in range(len(listNomPro1)):
        dicProductos[listNomPro1[i]] = listTotPro[i]

    aux = ''
    aux1 = ''
    cont = 0

    for c in listIns:
        cont = 0
        for c1 in c:
            cont = cont + 1
            if c1 == ":":
                break
            aux += c1
            aux1 = c
        listaLlaves.append(aux)
        listaValores.append(aux1[cont: len(aux1)])
        aux = ""

    aux = listaLlaves
    listaLlaves = []
    aux1 =listaValores
    listaValores = []
    listIns = []

    if len(aux) > len(aux1):
        print('Error posiblemente hay una coma de más en el archivo .lfp')
        opcion = 0
        menu(opcion)

    for i in aux:
        listaLlaves.append(i.strip())

    for i in aux1:
        listaValores.append(i.strip())

    aux =''
    aux1 = ''
    
    dicInstrucciones = {}
    dicInstrucciones1 = {}
    dicInstrucciones2 = {}
    for i in range(len(listaLlaves)):
        dicInstrucciones[listaLlaves[i]] = listaValores[i]
    dicInstrucciones1 = sorted(dicInstrucciones.items())
    dicInstrucciones2 = dict(dicInstrucciones1)

    if dicInstrucciones2.get('nombre'):
        pass
    else:
        print('No se encontro el nombre de la gráfica')
        opcion = 0
        menu(opcion)

    if dicInstrucciones2.get('grafica'):
        pass
    else:
        print('No se encontro el tipo de la gráfica')
        opcion = 0
        menu(opcion)

    if len(dicInstrucciones2) == 2:
        if dicInstrucciones2.get('grafica') == '"barras"':
            GraficaBarras2(dicInstrucciones2, mes, year, listNomPro1, listTotPro)
        elif dicInstrucciones2.get('grafica') == '"lineas"':
            GraficaLineas2(dicInstrucciones2, mes, year, listNomPro1, listTotPro)
        elif dicInstrucciones2.get('grafica') == '"pie"':
            GraficaPie2(dicInstrucciones2, mes, year, listNomPro1, listTotPro)
        else:
            print('Error el tipo de gráfica no es valido')
            opcion = 0
            menu(opcion)

    if len(dicInstrucciones2) == 3:
        if dicInstrucciones2.get('grafica') == '"barras"':
            GraficaBarras3(dicInstrucciones2, listNomPro1, listTotPro)
        elif dicInstrucciones2.get('grafica') == '"lineas"':
            GraficaLineas3(dicInstrucciones2, listNomPro1, listTotPro)
        elif dicInstrucciones2.get('grafica') == '"pie"':
            GraficaPie3(dicInstrucciones2, listNomPro1, listTotPro)
        else:
            print('Error el tipo de gráfica no es valido')
            opcion = 0
            menu(opcion)

    if len(dicInstrucciones2) == 4:
        if dicInstrucciones2.get('grafica') == '"barras"':
            GraficaBarras4(dicInstrucciones2, listNomPro1, listTotPro)
        elif dicInstrucciones2.get('grafica') == '"lineas"':
            GraficaLineas4(dicInstrucciones2, listNomPro1, listTotPro)
        elif dicInstrucciones2.get('grafica') == '"pie"':
            GraficaPie4(dicInstrucciones2, listNomPro1, listTotPro)
        else:
            print('Error el tipo de gráfica no es valido')
            opcion = 0
            menu(opcion)

    if len(dicInstrucciones2) == 5:
        if dicInstrucciones2.get('grafica') == '"barras"':
            GraficaBarras5(dicInstrucciones2, listNomPro1, listTotPro)
        elif dicInstrucciones2.get('grafica') == '"lineas"':
            GraficaLineas5(dicInstrucciones2, listNomPro1, listTotPro)
        elif dicInstrucciones2.get('grafica') == '"pie"':
            GraficaPie5(dicInstrucciones2, listNomPro1, listTotPro)
        else:
            print('Error el tipo de gráfica no es valido')
            opcion = 0
            menu(opcion)
    
    if len(dicInstrucciones2) < 2:
        print('Error faltan información')
        opcion = 0
        menu(opcion)

    if len(dicInstrucciones2) > 5:
        print('Hay información de más')
        opcion = 0
        menu(opcion)

    global dicReportes
    dicReportes = dicProductos


# Gráficas con dos elementos.
def GraficaBarras2(dicInstrucciones2, mes, year, listNomPro1, listTotPro):
    name = dicInstrucciones2['nombre']
    title = mes, ':', year
    name = name.replace('"', '', 2)

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    ax.bar(listNomPro1, listTotPro)

    # Guardar el grafica en formato png
    name = './' + name + '.png'
    plt.savefig(name)

    #Abrir imágen
    img = Image.open(name)
    img.show()

    listNomPro1 = []
    listTotPro = []

def GraficaLineas2(dicInstrucciones2, mes, year, listNomPro1, listTotPro):
    name = dicInstrucciones2['nombre']
    title = mes, ':', year
    name = name.replace('"', '', 2)

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    ax.plot(listNomPro1, listTotPro)

    # Guardar el grafica en formato png
    name = './' + name + '.png'
    plt.savefig(name)

    #Abrir imágen
    img = Image.open(name)
    img.show()

    listNomPro1 = []
    listTotPro = []

def GraficaPie2(dicInstrucciones2, mes, year, listNomPro1, listTotPro):
    name = dicInstrucciones2['nombre']
    title = mes, ':', year
    name = name.replace('"', '', 2)

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    ax.pie(listTotPro, labels = listNomPro1)

    # Guardar el grafica en formato png
    name = './' + name + '.png'
    plt.savefig(name)

    #Abrir imágen
    img = Image.open(name)
    img.show()

    listNomPro1 = []
    listTotPro = []

# Gráficas con tres elementos.
def GraficaBarras3(dicInstrucciones2, listNomPro1, listTotPro):
    aux = dicInstrucciones2.keys()
    for i in aux:
        if i == 'titulo':
            name = dicInstrucciones2['nombre']
            title = dicInstrucciones2['titulo']

            name = name.replace('"', '', 2)
            title = title.replace('"', '', 2)

            # Crear la figura y los ejes
            plt.rcdefaults()
            fig, ax = plt.subplots()

            #Título de la gráfica.
            plt.title(title)

            # Dibujar gráficas
            ax.bar(listNomPro1, listTotPro)

            # Guardar el grafica en formato png
            name = './' + name + '.png'
            plt.savefig(name)

            #Abrir imágen
            img = Image.open(name)
            img.show()

        elif i == 'titulox':
            name = dicInstrucciones2['nombre']
            titleX = dicInstrucciones2['titulox']

            name = name.replace('"', '', 2)
            titleX = titleX.replace('"', '', 2)

            # Crear la figura y los ejes
            plt.rcdefaults()
            fig, ax = plt.subplots()

            # Títulos de los ejes.
            plt.xlabel(titleX)

            # Dibujar gráficas
            ax.bar(listNomPro1, listTotPro)

            # Guardar el grafica en formato png
            name = './' + name + '.png'
            plt.savefig(name)

            #Abrir imágen
            img = Image.open(name)
            img.show()

        elif i == 'tituloy':
            name = dicInstrucciones2['nombre']
            titleY = dicInstrucciones2['tituloy']

            name = name.replace('"', '', 2)
            titleY = titleY.replace('"', '', 2)

            # Crear la figura y los ejes
            plt.rcdefaults()
            fig, ax = plt.subplots()

            # Títulos de los ejes.
            plt.ylabel(titleY)

            # Dibujar gráficas
            ax.bar(listNomPro1, listTotPro)

            # Guardar el grafica en formato png
            name = './' + name + '.png'
            plt.savefig(name)

            #Abrir imágen
            img = Image.open(name)
            img.show()

    listNomPro1 = []
    listTotPro = []

def GraficaLineas3(dicInstrucciones2, listNomPro1, listTotPro):
    aux = dicInstrucciones2.keys()
    for i in aux:
        if i == 'titulo':
            name = dicInstrucciones2['nombre']
            title = dicInstrucciones2['titulo']

            name = name.replace('"', '', 2)
            title = title.replace('"', '', 2)

            # Crear la figura y los ejes
            plt.rcdefaults()
            fig, ax = plt.subplots()

            #Título de la gráfica.
            plt.title(title)

            # Dibujar gráficas
            ax.plot(listNomPro1, listTotPro)

            # Guardar el grafica en formato png
            name = './' + name + '.png'
            plt.savefig(name)

            #Abrir imágen
            img = Image.open(name)
            img.show()
        elif i == 'titulox':
            name = dicInstrucciones2['nombre']
            titleX = dicInstrucciones2['titulox']

            name = name.replace('"', '', 2)
            titleX = titleX.replace('"', '', 2)

            # Crear la figura y los ejes
            plt.rcdefaults()
            fig, ax = plt.subplots()

            # Títulos de los ejes.
            plt.xlabel(titleX)

            # Dibujar gráficas
            ax.plot(listNomPro1, listTotPro)

            # Guardar el grafica en formato png
            name = './' + name + '.png'
            plt.savefig(name)

            #Abrir imágen
            img = Image.open(name)
            img.show()
        elif i == 'tituloy':
            name = dicInstrucciones2['nombre']
            titleY = dicInstrucciones2['tituloy']

            name = name.replace('"', '', 2)
            titleY = titleY.replace('"', '', 2)

            # Crear la figura y los ejes
            plt.rcdefaults()
            fig, ax = plt.subplots()

            # Títulos de los ejes.
            plt.ylabel(titleY)

            # Dibujar gráficas
            ax.plot(listNomPro1, listTotPro)

            # Guardar el grafica en formato png
            name = './' + name + '.png'
            plt.savefig(name)

            #Abrir imágen
            img = Image.open(name)
            img.show()
    
    listNomPro1 = []
    listTotPro = []


def GraficaPie3(dicInstrucciones2, listNomPro1, listTotPro):
    aux = dicInstrucciones2.keys()
    for i in aux:
        if i == 'titulo':
            name = dicInstrucciones2['nombre']
            title = dicInstrucciones2['titulo']

            name = name.replace('"', '', 2)
            title = title.replace('"', '', 2)

            # Crear la figura y los ejes
            plt.rcdefaults()
            fig, ax = plt.subplots()

            #Título de la gráfica.
            plt.title(title)

            # Dibujar gráficas
            ax.pie(listTotPro, labels = listNomPro1)

            # Guardar el grafica en formato png
            name = './' + name + '.png'
            plt.savefig(name)

            #Abrir imágen
            img = Image.open(name)
            img.show()
        elif i == 'titulox':
            name = dicInstrucciones2['nombre']
            name = name.replace('"', '', 2)

            # Crear la figura y los ejes
            plt.rcdefaults()
            fig, ax = plt.subplots()

            # Dibujar gráficas
            ax.pie(listTotPro, labels = listNomPro1)

            # Guardar el grafica en formato png
            name = './' + name + '.png'
            plt.savefig(name)

            #Abrir imágen
            img = Image.open(name)
            img.show()
        elif i == 'tituloy':
            name = dicInstrucciones2['nombre']
            name = name.replace('"', '', 2)

            # Crear la figura y los ejes
            plt.rcdefaults()
            fig, ax = plt.subplots()

            # Dibujar gráficas
            ax.pie(listTotPro, labels = listNomPro1)

            # Guardar el grafica en formato png
            name = './' + name + '.png'
            plt.savefig(name)

            #Abrir imágen
            img = Image.open(name)
            img.show()
    
    listNomPro1 = []
    listTotPro = []

# Gráficas con cuatro elementos.
def GraficaBarras4(dicInstrucciones2, listNomPro1, listTotPro):
    aux = dicInstrucciones2.keys()
    aux1 = dicInstrucciones2.keys()
    for i in aux:
        if i == 'titulo':
            for j in aux1:
                if j == 'titulox':
                    name = dicInstrucciones2['nombre']
                    title = dicInstrucciones2['titulo']
                    titlex = dicInstrucciones2['titulox']

                    name = name.replace('"', '', 2)
                    title = title.replace('"', '', 2)
                    titlex = titlex.replace('"', '', 2)

                    # Crear la figura y los ejes
                    plt.rcdefaults()
                    fig, ax = plt.subplots()

                    # Títulos de los ejes.
                    plt.xlabel(titlex)

                    #Título de la gráfica.
                    plt.title(title)

                    # Dibujar gráficas
                    ax.bar(listNomPro1, listTotPro)

                    # Guardar el grafica en formato png
                    name = './' + name + '.png'
                    plt.savefig(name)

                    #Abrir imágen
                    img = Image.open(name)
                    img.show()
                elif j == 'tituloy':
                    name = dicInstrucciones2['nombre']
                    title = dicInstrucciones2['titulo']
                    titley = dicInstrucciones2['tituloy']

                    name = name.replace('"', '', 2)
                    title = title.replace('"', '', 2)
                    titley = titley.replace('"', '', 2)

                    # Crear la figura y los ejes
                    plt.rcdefaults()
                    fig, ax = plt.subplots()

                    # Títulos de los ejes.
                    plt.ylabel(titley)

                    #Título de la gráfica.
                    plt.title(title)

                    # Dibujar gráficas
                    ax.bar(listNomPro1, listTotPro)

                    # Guardar el grafica en formato png
                    name = './' + name + '.png'
                    plt.savefig(name)

                    #Abrir imágen
                    img = Image.open(name)
                    img.show()
    
    listNomPro1 = []
    listTotPro = []

def GraficaLineas4(dicInstrucciones2, mes, year, listNomPro1, listTotPro):
    aux = dicInstrucciones2.keys()
    aux1 = dicInstrucciones2.keys()
    for i in aux:
        if i == 'titulo':
            for j in aux1:
                if j == 'titulox':
                    name = dicInstrucciones2['nombre']
                    title = dicInstrucciones2['titulo']
                    titlex = dicInstrucciones2['titulox']

                    name = name.replace('"', '', 2)
                    title = title.replace('"', '', 2)
                    titlex = titlex.replace('"', '', 2)

                    # Crear la figura y los ejes
                    plt.rcdefaults()
                    fig, ax = plt.subplots()

                    # Títulos de los ejes.
                    plt.xlabel(titlex)

                    #Título de la gráfica.
                    plt.title(title)

                    # Dibujar gráficas
                    ax.plot(listNomPro1, listTotPro)

                    # Guardar el grafica en formato png
                    name = './' + name + '.png'
                    plt.savefig(name)

                    #Abrir imágen
                    img = Image.open(name)
                    img.show()
                elif j == 'tituloy':
                    name = dicInstrucciones2['nombre']
                    title = dicInstrucciones2['titulo']
                    titley = dicInstrucciones2['tituloy']

                    name = name.replace('"', '', 2)
                    title = title.replace('"', '', 2)
                    titley = titley.replace('"', '', 2)

                    # Crear la figura y los ejes
                    plt.rcdefaults()
                    fig, ax = plt.subplots()

                    # Títulos de los ejes.
                    plt.ylabel(titley)

                    #Título de la gráfica.
                    plt.title(title)

                    # Dibujar gráficas
                    ax.plot(listNomPro1, listTotPro)

                    # Guardar el grafica en formato png
                    name = './' + name + '.png'
                    plt.savefig(name)

                    #Abrir imágen
                    img = Image.open(name)
                    img.show()
    
    listNomPro1 = []
    listTotPro = []

def GraficaPie4(dicInstrucciones2, listNomPro1, listTotPro):
    aux = dicInstrucciones2.keys()
    aux1 = dicInstrucciones2.keys()
    for i in aux:
        if i == 'titulo':
            for j in aux1:
                if j == 'titulox':
                    name = dicInstrucciones2['nombre']
                    title = dicInstrucciones2['titulo']

                    name = name.replace('"', '', 2)
                    title = title.replace('"', '', 2)

                    # Crear la figura y los ejes
                    plt.rcdefaults()
                    fig, ax = plt.subplots()

                    #Título de la gráfica.
                    plt.title(title)

                    # Dibujar gráficas
                    ax.pie(listTotPro, labels = listNomPro1)

                    # Guardar el grafica en formato png
                    name = './' + name + '.png'
                    plt.savefig(name)

                    #Abrir imágen
                    img = Image.open(name)
                    img.show()
                elif j == 'tituloy':
                    name = dicInstrucciones2['nombre']
                    title = dicInstrucciones2['titulo']

                    name = name.replace('"', '', 2)
                    title = title.replace('"', '', 2)

                    # Crear la figura y los ejes
                    plt.rcdefaults()
                    fig, ax = plt.subplots()

                    #Título de la gráfica.
                    plt.title(title)

                    # Dibujar gráficas
                    ax.pie(listTotPro, labels = listNomPro1)

                    # Guardar el grafica en formato png
                    name = './' + name + '.png'
                    plt.savefig(name)

                    #Abrir imágen
                    img = Image.open(name)
                    img.show()

    listNomPro1 = []
    listTotPro = []


# Gráficas con cinco elementos.
def GraficaBarras5(dicInstrucciones2, listNomPro1, listTotPro):
    name = dicInstrucciones2['nombre']
    title = dicInstrucciones2['titulo']
    titleX = dicInstrucciones2['titulox']
    titleY = dicInstrucciones2['tituloy']
    
    name = name.replace('"', '', 2)
    title = title.replace('"', '', 2)
    titleX = titleX.replace('"', '', 2)
    titleY = titleY.replace('"', '', 2)

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Títulos de los ejes.
    plt.xlabel(titleX)
    plt.ylabel(titleY)

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    ax.bar(listNomPro1, listTotPro)

    # Guardar el grafica en formato png
    name = './' + name + '.png'
    plt.savefig(name)

    #Abrir imágen
    img = Image.open(name)
    img.show()

    listNomPro1 = []
    listTotPro = []


def GraficaLineas5(dicInstrucciones2, listNomPro1, listTotPro):
    name = dicInstrucciones2['nombre']
    title = dicInstrucciones2['titulo']
    titleX = dicInstrucciones2['titulox']
    titleY = dicInstrucciones2['tituloy']
    
    name = name.replace('"', '', 2)
    title = title.replace('"', '', 2)
    titleX = titleX.replace('"', '', 2)
    titleY = titleY.replace('"', '', 2)

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Títulos de los ejes.
    plt.xlabel(titleX)
    plt.ylabel(titleY)

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    ax.plot(listNomPro1, listTotPro)
    #ax.pie(listTotPro, labels = listNomPro1)

    # Guardar el grafica en formato png
    name = './' + name + '.png'
    plt.savefig(name)

    #Abrir imágen
    img = Image.open(name)
    img.show()

    listNomPro1 = []
    listTotPro = []


def GraficaPie5(dicInstrucciones2, listNomPro1, listTotPro):
    name = dicInstrucciones2['nombre']
    title = dicInstrucciones2['titulo']
    
    name = name.replace('"', '', 2)
    title = title.replace('"', '', 2)

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    ax.pie(listTotPro, labels = listNomPro1)

    # Guardar el grafica en formato png
    name = './' + name + '.png'
    plt.savefig(name)

    #Abrir imágen
    img = Image.open(name)
    img.show()

    listNomPro1 = []
    listTotPro = []


def Reportes():
    menosVendidos = []
    masVendidos = []
    primero = []
    ultimo = []

    for ele in listProG:
        for i in range(len(ele)):
            ele[3] = float(ele[3])
            #listaProductos[i] = ele
    
    for i in listProG:
        i = i.reverse()

    for i in range(1,len(listProG)):
        for j in range(0,len(listProG) - i):
            if(listProG[j + 1] < listProG[j]):
                aux = listProG[j];
                listProG[j] = listProG[j + 1];
                listProG[j + 1] = aux;
    
    for i in listProG:
        i = i.reverse()
    
    primero = listProG[0]
    ultimo = listProG[-1]

    aux = ''
    for i in range(len(listProG)):
        aux = listProG[i]

        if aux[3] == primero[3]:
            menosVendidos.append(listProG[i])
        
        if aux[3] == ultimo[3]:
            masVendidos.append(listProG[i])

    if len(listProG) > 0:
        docHTML = open('Reporte.html', 'w')
        docHTML.write('\n<!DOCTYPE html>')
        docHTML.write('\n<html lang="es">')
        docHTML.write('\n <h6>Carlos Daniel Catalan Catalan</h6>')
        docHTML.write('\n <h6>201520557</h6>')
        docHTML.write('\n<head>')
        docHTML.write('\n<meta charset="utf-8">')
        docHTML.write('\n<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">')
        docHTML.write('\n<title>Reporte de Ventas</title>')
        docHTML.write('\n</head>')
        docHTML.write('\n<body>')
        docHTML.write('\n<div class="container">')
        docHTML.write('\n <h4 class= "text-center">Lista De Productos</h4>')
        docHTML.write('\n<div>')
        docHTML.write('\n<div class="container">')
        docHTML.write('\n<table class="table" border="1">')
        docHTML.write('\n\t <thead class="thead-dark">')
        docHTML.write('\n\t\t <tr>')
        docHTML.write('\n\t\t\t<th scope = "col">Productos</th>')
        docHTML.write('\n\t\t\t<th scope = "col">Precio</th>')
        docHTML.write('\n\t\t\t<th scope = "col">Cantida de Unidades</th>')
        docHTML.write('\n\t\t\t<th scope = "col">Total</th>')
        docHTML.write('\n\t\t </tr>')
        docHTML.write('\n\t </thead>')
        docHTML.write('\n\t <tbody>')

        for i in listProG:
            for j in range(len(i)):
                docHTML.write('\n\t\t <tr class="table-success">')
                i[j] = i[j].replace('"', '', 2)
                docHTML.write('\n\t\t\t<th scope = "row">' + str(i[j]))
                docHTML.write('</th>')
                docHTML.write('\n\t\t\t<td>'+str(i[j+1]))
                docHTML.write('</td>')
                docHTML.write('\n\t\t\t<td>' + str(i[j+2]))
                docHTML.write('</td>')
                docHTML.write('\n\t\t\t<td>' + str(i[j+3]))
                docHTML.write('</td>')
                docHTML.write('\n\t\t </tr>')
                break

        docHTML.write('\n\t </tbody>')
        docHTML.write('\n</table>')
        docHTML.write('\n</div>')

        docHTML.write('\n<div class="container">')
        docHTML.write('\n <h4 class= "text-center">Lista De Productos Menos Vendidos</h4>')
        docHTML.write('\n<div>')
        docHTML.write('\n<div class="container">')
        docHTML.write('\n<table class="table" border="1">')
        docHTML.write('\n\t <thead class="thead-dark">')
        docHTML.write('\n\t\t <tr>')
        docHTML.write('\n\t\t\t<th scope = "col">Productos</th>')
        docHTML.write('\n\t\t\t<th scope = "col">Precio</th>')
        docHTML.write('\n\t\t\t<th scope = "col">Cantida de Unidades</th>')
        docHTML.write('\n\t\t\t<th scope = "col">Total</th>')
        docHTML.write('\n\t\t </tr>')
        docHTML.write('\n\t </thead>')
        docHTML.write('\n\t <tbody>')

        if len(menosVendidos) > 0:
            for i in menosVendidos:
                for j in range(len(i)):
                    docHTML.write('\n\t\t <tr class="table-success">')
                    i[j] = i[j].replace('"', '', 2)
                    docHTML.write('\n\t\t\t<th scope = "row">' + str(i[j]))
                    docHTML.write('</th>')
                    docHTML.write('\n\t\t\t<td>'+str(i[j+1]))
                    docHTML.write('</td>')
                    docHTML.write('\n\t\t\t<td>' + str(i[j+2]))
                    docHTML.write('</td>')
                    docHTML.write('\n\t\t\t<td>' + str(i[j+3]))
                    docHTML.write('</td>')
                    docHTML.write('\n\t\t </tr>')
                    break
            
        docHTML.write('\n\t </tbody>')
        docHTML.write('\n</table>')
        docHTML.write('\n</div>')
        docHTML.write('\n</body>')
        docHTML.write('\n</html>')

        docHTML.write('\n<div class="container">')
        docHTML.write('\n <h4 class= "text-center">Lista De Productos Mas Vendidos</h4>')
        docHTML.write('\n<div>')
        docHTML.write('\n<div class="container">')
        docHTML.write('\n<table class="table" border="1">')
        docHTML.write('\n\t <thead class="thead-dark">')
        docHTML.write('\n\t\t <tr>')
        docHTML.write('\n\t\t\t<th scope = "col">Productos</th>')
        docHTML.write('\n\t\t\t<th scope = "col">Precio</th>')
        docHTML.write('\n\t\t\t<th scope = "col">Cantida de Unidades</th>')
        docHTML.write('\n\t\t\t<th scope = "col">Total</th>')
        docHTML.write('\n\t\t </tr>')
        docHTML.write('\n\t </thead>')
        docHTML.write('\n\t <tbody>')

        if len(masVendidos) > 0:
            for i in masVendidos:
                for j in range(len(i)):
                    docHTML.write('\n\t\t <tr class="table-success">')
                    i[j] = i[j].replace('"', '', 2)
                    docHTML.write('\n\t\t\t<th scope = "row">' + str(i[j]))
                    docHTML.write('</th>')
                    docHTML.write('\n\t\t\t<td>'+str(i[j+1]))
                    docHTML.write('</td>')
                    docHTML.write('\n\t\t\t<td>' + str(i[j+2]))
                    docHTML.write('</td>')
                    docHTML.write('\n\t\t\t<td>' + str(i[j+3]))
                    docHTML.write('</td>')
                    docHTML.write('\n\t\t </tr>')
                    break
            
        docHTML.write('\n\t </tbody>')
        docHTML.write('\n</table>')
        docHTML.write('\n</div>')
        docHTML.write('\n</body>')
        docHTML.write('\n</html>')
        

        docHTML.write('\n</body>')
        docHTML.write('\n</html>')
        docHTML.close()

        webbrowser.open_new_tab('Reporte.html')
    else:
        docHTML = open('Reporte.html', 'w')
        docHTML.write('\n<!DOCTYPE html>')
        docHTML.write('\n<html lang="es">')
        docHTML.write('\n<head>')
        docHTML.write('\n<meta charset="utf-8">')
        docHTML.write('\n<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">')
        docHTML.write('\n<title>Reporte de Ventas</title>')
        docHTML.write('\n</head>')
        docHTML.write('\n<body>')
        docHTML.write('\n <h6>Carlos Daniel Catalan Catalan</h6>')
        docHTML.write('\n <h6>201520557</h6>')
        docHTML.write('\n <h4>No hay datos que mostar</h4>')
        docHTML.write('\n</body>')
        docHTML.write('\n</html>')
        docHTML.close()
        webbrowser.open_new_tab('Reporte.html')

if __name__ == '__main__':
    opcion = 0
    menu(opcion)
