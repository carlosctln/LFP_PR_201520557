#_*_ coding: utf8 _*_

from codecs import EncodedFile
from encodings import utf_8
from fileinput import filename
from tkinter import filedialog, Tk

data = ''
instrucciones = ''
aux = ''
listaProductos = []
aux1 = ''

def menu (opcion):
    try:    
        while opcion != 5:
            
            print('╔══════════════════════════════════════════╗')
            print('║                   Menú                   ║')
            print('║══════════════════════════════════════════║')
            print('║ 1. Cargar Data.                          ║')
            print('║ 2. Cargar Instrucciones.                 ║')
            print('║ 3. Analizar.                             ║')
            print('║ 4. Reportes                              ║')
            print('║ 5. Salir                                 ║')
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
            print(data)
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
            print(instrucciones)
            return instrucciones
    
def Analizar():
    if data != '' and instrucciones != '':
        print('Archivos cargados correctamente')
        RecorrerArchivos()
    else:
        print('Debes cargar dos archivos uno con extensión .data y el otro con instrucción .lfp')

def RecorrerArchivos():
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
    for i in mes:
        if i == ' ':
            continue
        aux1 += i
    mes = aux1
    aux1 = ''

    for i in year:
        if i == ' ':
            continue
        aux1 += i
    year = aux1
    aux1 = ''

    print(mes)
    print(year)
    
    for lista in listaProductos:
        print(lista)

if __name__ == '__main__':
    opcion = 0
    menu(opcion)
