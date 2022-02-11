flag = True
opc = 0
class menu:
    def ImprimirMenu():
        try:
            while flag == True:
                print('╔══════════════════════════════════════════╗')
                print('║                   Menú                   ║')
                print('║══════════════════════════════════════════║')
                print('║ 1. Cargar Data.                          ║')
                print('║ 2. Cargar Instrucciones.                 ║')
                print('║ 3. Analizar.                             ║')
                print('║ 4. Reportes                              ║')
                print('║ 5. Salir                                 ║')
                print('╚══════════════════════════════════════════╝')
                print('Ingrese un número entre las opciones')
                opc = input()
                #OpcMenu(opc)
        except:
            print('Ingresa un número entero')

    
    