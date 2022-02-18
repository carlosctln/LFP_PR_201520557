from unicodedata import name
import matplotlib.pyplot as plt

from codecs import EncodedFile
from encodings import utf_8
from fileinput import filename
from tkinter import filedialog, Tk

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

dicProductos = {}
dicInstrucciones = {}
dicInstrucciones1 = {}
dicInstrucciones2 = {}

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
        print("Esta es la opción 4")
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
            #return data

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
            #return instrucciones
    
def Analizar():
    if data != '' and instrucciones != '':
        print('Archivos cargados correctamente')
        RecorrerArchivos()
    else:
        print('Debes cargar dos archivos uno con extensión .data y el otro con instrucción .lfp')

def RecorrerArchivos():
    # Recorremos el archivo .data
    global aux
    global aux1
    parA = 0
    parC = 0
    corA = 0
    corC = 0
    menor = 0
    mayor = 0
    intA = 0
    intC = 0

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

    for ele in listaProductos1:
        for i in range(len(ele)):
            try:
                ele[1] = float(ele[1])
                ele[2] = int(ele[2])
                listaProductos[i] = ele
                break
            except:
                print('El producto contiene caracteres y no números')
                opcion = 0
                menu(opcion)

    for ele in listaProductos1:
        for i in range(len(ele)):
            if ele[1] <= 0 or ele[2] <= 0:
                print('Error ingresa valores mayores o iguales a 1')
                opcion = 0
                menu(opcion)

    for ele in listaProductos1:
        for i in range(len(ele)):
            listNomPro.append(ele[0])
            listTotPro.append(ele[1] * ele[2])
            break
    
    aux = ''
    listNomPro1 = []
    for ele in listNomPro:
        aux = ele.replace('“', '', 1)
        ele = aux.replace('”', '', 1)
        ele = ele.replace('"', '', 2)
        listNomPro1.append(ele)

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

    for i in aux:
        listaLlaves.append(i.strip())

    for i in aux1:
        listaValores.append(i.strip())
        
    for i in range(len(listaLlaves)):
        dicInstrucciones[listaLlaves[i]] = listaValores[i]
    dicInstrucciones1 = sorted(dicInstrucciones.items())
    dicInstrucciones2 = dict(dicInstrucciones1)

    print(len(dicInstrucciones2))

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

# Gráficas con dos elementos.
def GraficaBarras2(dicInstrucciones2, mes, year, listNomPro1, listTotPro):
    name = dicInstrucciones2['nombre']
    title = mes, ':', year

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    ax.bar(listNomPro1, listTotPro)

    # Guardar el grafica en formato png
    plt.savefig(f'./grafica.png')

def GraficaLineas2(dicInstrucciones2, mes, year, listNomPro1, listTotPro):
    name = dicInstrucciones2['nombre']
    title = mes, ':', year

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    ax.plot(listNomPro1, listTotPro)

    # Guardar el grafica en formato png
    plt.savefig(f'./grafica.png')

def GraficaPie2(dicInstrucciones2, mes, year, listNomPro1, listTotPro):
    name = dicInstrucciones2['nombre']
    title = mes, ':', year

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    ax.pie(listTotPro, labels = listNomPro1)

    # Guardar el grafica en formato png
    plt.savefig(f'./grafica.png')

# Gráficas con tres elementos.
def GraficaBarras3(dicInstrucciones2, listNomPro1, listTotPro):
    aux = dicInstrucciones2.keys()
    print(aux)
    for i in aux:
        if i == 'titulo':
            name = dicInstrucciones2['nombre']
            title = dicInstrucciones2['titulo']
            title = title.replace('"', '', 2)

            # Crear la figura y los ejes
            plt.rcdefaults()
            fig, ax = plt.subplots()

            #Título de la gráfica.
            plt.title(title)

            # Dibujar gráficas
            ax.bar(listNomPro1, listTotPro)

            # Guardar el grafica en formato png
            plt.savefig(f'./grafica.png')
        elif i == 'titulox':
            name = dicInstrucciones2['nombre']
            titleX = dicInstrucciones2['titulox']
            titleX = titleX.replace('"', '', 2)

            # Crear la figura y los ejes
            plt.rcdefaults()
            fig, ax = plt.subplots()

            # Títulos de los ejes.
            plt.xlabel(titleX)

            # Dibujar gráficas
            ax.bar(listNomPro1, listTotPro)

            # Guardar el grafica en formato png
            plt.savefig(f'./grafica.png')
        elif i == 'tituloy':
            name = dicInstrucciones2['nombre']
            titleY = dicInstrucciones2['tituloy']
            titleY = titleY.replace('"', '', 2)

            # Crear la figura y los ejes
            plt.rcdefaults()
            fig, ax = plt.subplots()

            # Títulos de los ejes.
            plt.ylabel(titleY)

            # Dibujar gráficas
            ax.bar(listNomPro1, listTotPro)

            # Guardar el grafica en formato png
            plt.savefig(f'./grafica.png')

def GraficaLineas3(dicInstrucciones2, listNomPro1, listTotPro):

    name = dicInstrucciones2['nombre']
    title = ''

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    ax.plot(listNomPro1, listTotPro)

    # Guardar el grafica en formato png
    plt.savefig(f'./grafica.png')

def GraficaPie3(dicInstrucciones2, listNomPro1, listTotPro):
    name = dicInstrucciones2['nombre']
    title = ''

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    ax.pie(listTotPro, labels = listNomPro1)

    # Guardar el grafica en formato png
    plt.savefig(f'./grafica.png')

# Gráficas con cuatro elementos.
def GraficaBarras4(dicInstrucciones2, mes, year, listNomPro1, listTotPro):
    name = dicInstrucciones2['nombre']
    title = mes, ':', year

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    ax.bar(listNomPro1, listTotPro)

def GraficaLineas4(dicInstrucciones2, mes, year, listNomPro1, listTotPro):
    name = dicInstrucciones2['nombre']
    title = mes, ':', year

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    ax.plot(listNomPro1, listTotPro)

    # Guardar el grafica en formato png
    plt.savefig(f'./grafica.png')

def GraficaPie4(dicInstrucciones2, mes, year, listNomPro1, listTotPro):
    name = dicInstrucciones2['nombre']
    title = mes, ':', year

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    ax.pie(listTotPro, labels = listNomPro1)

    # Guardar el grafica en formato png
    plt.savefig(f'./grafica.png')

# Gráficas con cinco elementos.
def GraficaBarras5(dicInstrucciones2, mes, year, listNomPro1, listTotPro):
    name = dicInstrucciones2['nombre']
    title = mes, ':', year

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    ax.bar(listNomPro1, listTotPro)

def GraficaLineas5(dicInstrucciones2, mes, year, listNomPro1, listTotPro):
    name = dicInstrucciones2['nombre']
    title = mes, ':', year

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    ax.plot(listNomPro1, listTotPro)

    # Guardar el grafica en formato png
    plt.savefig(f'./grafica.png')

def GraficaPie5(dicInstrucciones2, mes, year, listNomPro1, listTotPro):
    name = dicInstrucciones2['nombre']
    title = mes, ':', year

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    ax.pie(listTotPro, labels = listNomPro1)

    # Guardar el grafica en formato png
    plt.savefig(f'./grafica.png')


    '''name = dicInstrucciones2['nombre']
    title = dicInstrucciones2['titulo']
    titleX = dicInstrucciones2['titulox']
    titleY = dicInstrucciones2['tituloy']
    
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
    #ax.plot(listNomPro1, listTotPro)
    #ax.bar(listNomPro1, listTotPro)
    ax.pie(listTotPro, labels = listNomPro1)

    # Guardar el grafica en formato png
    plt.savefig(f'./grafica.png')

    # Mostrar el gráfico
    #plt.show()
    '''

if __name__ == '__main__':
    opcion = 0
    menu(opcion)
