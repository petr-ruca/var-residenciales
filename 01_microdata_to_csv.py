import csv
from tkinter import messagebox
from tkinter.filedialog import askopenfilenames


filename = askopenfilenames(title="Elige los microdatos en .TXT", filetypes=[
                            ('TXT file', '*.txt'), ('All files', '*.*')])

for filez in filename:
    lines = open(filez).readlines()

    # Longitud de cada campo de cada microdato
    # segun el diseño de fichero del INE:
    field_widths = [1, 2, 3, 3, 2, 4, 3, 2, 3, 2, 4, 2, 3, 1, 1, 1]

    # Crea una lista con los digitos separados:
    outputList = []

    # Añade la cabecera de los datos del INE
    outputList.append(['SEXO', 'PROVNAC', 'MUNINAC', 'EDAD', 'MESNAC',
                       'ANONAC', 'CNAC', 'PROVALTA', 'MUNIALTA', 'MESVAR',
                       'ANOVAR', 'PROVBAJA', 'MUNIBAJA', 'TAMUALTA',
                       'TAMUBAJA', 'TAMUNACI'])

    for line in lines:
        idx = 0
        lineList = []
        for i in field_widths:
            upper = idx + i
            # sustituye espacios en blanco por 0
            linechecked = line[idx:upper].replace(" ", str(0))
            lineList.append(linechecked)
            # lineList.append(line[idx:upper])
            idx = upper
        outputList.append(lineList)

    # Guarda el resultado en un archivo compatible con excel:
    # quitando el '.txt' del nombre
    savename = filez[:-4]

    with open("{0}.csv".format(savename), "w") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(outputList)

messagebox.showinfo("Python:", "Archivos guardados correctamente")
