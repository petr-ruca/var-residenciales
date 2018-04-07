# Numero de campo respecto al diseño del fichero de microdatos INE:
# PROVALTA y MUNIALTA: campos 8 y 9 (python empieza a contar desde 0,
# así que hay que restar 1 a cada campo)
# PROVBAJA y MUNIBAJA: campos 12 y 13
import csv
#from databases import provincias
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, askopenfilenames
import pandas as pd

#filename = askopenfilenames(title="Elige los microdatos en .CSV para filtrarlos por provincia",filetypes=[('CSV file','*.csv'), ('All files','*.*')])
filename = '/Volumes/HD/Google Drive/2018 UCO - Variaciones Residenciales/var-residenciales/testfiles/2000.csv'

completo = pd.read_csv(filename)
filtro = completo.PROVALTA == 39
filtro.head()
completo[filtro]

completo.head()

chosenprov = 1
for filez in filename:

    # Loop para cada archivo CSV, debería haber uno por año
    # for filez in filename:
    #    with open(filez) as csv_file:
    #        csv_reader = csv.reader(csv_file)
    #
    #        for line in csv_reader:
    #            print(line[2])
