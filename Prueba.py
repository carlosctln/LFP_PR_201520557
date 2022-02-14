from tkinter import filedialog, Tk

def abrir():
    
    Tk().withdraw()
    archivo = filedialog.askopenfilename(title= 'Seleccionar un archivo',
        filetypes=[('Archivo Data', '*.data'),
        ('All Files', '*')])
    with open(archivo, 'r', encoding='utf8') as file:
        if archivo is None:
            print('No se seleccionó ningun archivo\n')
            return None
        else:
            texto = file.read()
            file.close()
            print('Lectura exitosa\n')
            print(texto)
            return texto 
abrir()