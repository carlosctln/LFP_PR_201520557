from tkinter import filedialog, Tk

num = 0
let = 0
simb = 0
def abrir():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = 'Seleccionar un archivo',
        initialdir = './',
        filetypes = (
            ('Archivos TXT', '*.txt'),
            ('Todos los archivos', '*.*')
        )
    )
    if archivo is None:
        print('No se selcciono ningún archivo')
        return None
    else:
        texto = archivo.read()
        archivo.close()
        return texto

if __name__ == '__main__':
    txt = abrir()

    if txt is not None:
        if(len(txt) > 0):
            for c in txt:
                if ord(c) >= 48 and ord(c) <= 57:
                    num += 1
                elif ord(c) >= 65 and ord(c) <= 90:
                    let += 1
                elif ord(c) >= 97 and ord(c) <= 122:
                    let += 1
                else:
                    simb += 1
        else:
            print('No hay texto')
    else:
        print('No se puede procesar\n')

    print('La cantidad de letras es: ' + str(let))
    print('La cantidad de dígitos es: ' + str(num))
    print('La cantidad de símbolos es: ' + str(simb))
