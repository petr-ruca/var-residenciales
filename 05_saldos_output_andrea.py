import pandas as pd
from resources.funciones import buscar_muni
from resources.funciones import buscar_prov
from resources.funciones import get_saldo
from resources.funciones import get_saldo_hombres
from resources.funciones import get_saldo_mujeres
from tkinter.filedialog import askopenfilenames


munidatabase = pd.read_csv('databases/municipios.csv', sep=';')

filename = askopenfilenames(title= "Elige todos los microdatos en .CSV", filetypes=[('CSV file', '*.csv'), ('All files', '*.*')])

for filez in filename:
    microdatos = pd.read_csv(filez)
    year = filez[-8:-4]
    munidatabase['Saldo_' + year] = munidatabase['PROVMUNI'].apply(get_saldo, df=microdatos)
    munidatabase['Saldo_H_' + year] = munidatabase['PROVMUNI'].apply(get_saldo_hombres, df=microdatos)
    munidatabase['Saldo_M_' + year] = munidatabase['PROVMUNI'].apply(get_saldo_mujeres, df=microdatos)

munidatabase.to_csv('outputs/variacionesresidencialesAndrea.csv', index=False)