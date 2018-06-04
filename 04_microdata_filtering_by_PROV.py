import pandas as pd
import os
from resources import easygui as eg
from resources.funciones import buscar_prov
from databases.provincias import provincelist
from databases.provincias import provincedict
from tkinter.filedialog import askopenfilenames


# Abre los archivos de microdatos brutos por año
filename = askopenfilenames(title="Elige los microdatos en .CSV para filtrarlos por provincia",
                            filetypes=[('CSV file', '*.csv'), ('All files', '*.*')])


# Crea una lista con los codigos de las provincias elegidas
chosenprov = eg.multchoicebox("¿De que provincias?", "Carl Sagan asks:", provincelist)
chosenprov_codes = []
for key in chosenprov:
    if key in provincedict:
        chosenprov_codes.append(provincedict[key])

# Bucle para cada año, filtra los microdatos por provincias
for filez in filename:
    year = filez[-8:-4]
    microdatos_raw = pd.read_csv(filez)

#   Bucle para filtrar todas las provincias seleccionadas
    for prov in chosenprov_codes:
        nombreprov = buscar_prov(prov)
        provpath = nombreprov + '/'
        microdatos_filtro = microdatos_raw[(microdatos_raw.PROVALTA == prov) |
                                           (microdatos_raw.PROVBAJA == prov)]

#       Define la ruta del archivo nuevo y el nombre
        savepath = str(filez[:-8]) + str(provpath) + '/'
        filename = str(nombreprov) + '_' + str(year) + '.csv'

#       Si el directorio no existe se crea
        if not os.path.exists(savepath):
            os.makedirs(savepath)

#       Guarda el archivo filtrado
        microdatos_filtro.to_csv(savepath + filename, index=False)
