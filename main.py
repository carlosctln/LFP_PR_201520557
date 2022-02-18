import matplotlib.pyplot as plt

from codecs import EncodedFile
from encodings import utf_8
from fileinput import filename
from tkinter import filedialog, Tk

from numpy import tile

data = ''
instrucciones = ''
aux = ''
listaProductos = []
aux1 = ''
dicInstrucciones = {}

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
            file.close()
            print('Lectura exitosa\n')
            return data

def LeerArchivoInstrucciones():
    global instrucciones
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
            file.close()
            print('Lectura exitosa\n')
            return instrucciones
    
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
    aux1 = ''
    aux1 = mes
    mes = aux1.strip()
    aux1 = ''

    aux1 = year
    year = aux1.strip()
    aux1 = ''
    aux =''
    
    for i in listaProductos:
        print(i)

    # Recorremos el archivo .lfp
    for i in instrucciones:
        if i =='<':
            continue
        elif i == '¿':
            continue
        elif i == '>':
            continue
        elif i == '\n':
            continue
        elif i == '\t':
            continue
        aux += i

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

    name = dicInstrucciones['Nombre']
    title = dicInstrucciones['Titulo']
    titleX = dicInstrucciones['TituloX']
    titleY = dicInstrucciones['TituloY']
    
    title = title.replace('"', '', 2)
    titleX = titleX.replace('"', '', 2)
    titleY = titleY.replace('"', '', 2)
    num = [1, 2, 3, 4, 5]

    # Crear la figura y los ejes
    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Títulos de los ejes.
    plt.xlabel(titleX)
    plt.ylabel(titleY)

    #Título de la gráfica.
    plt.title(title)

    # Dibujar gráficas
    #ax.plot(listaValores, listaLlaves)
    #ax.bar(listaValores, listaLlaves)
    ax.pie(num, labels=listaLlaves)

    # Guardar el grafica en formato png
    plt.savefig(f'./grafica.png')

    # Mostrar el gráfico
    #plt.show()

if __name__ == '__main__':
    opcion = 0
    menu(opcion)
