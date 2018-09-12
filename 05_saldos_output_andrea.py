import pandas as pd
from resources.funciones import buscar_muni
from resources.funciones import buscar_prov
from resources.funciones import get_saldo_total
from resources.funciones import get_saldo_hombres
from resources.funciones import get_saldo_mujeres
from tkinter.filedialog import askopenfilenames


munidatabase = pd.read_csv('databases/municipios.csv', sep=';')

filename = askopenfilenames(title= "Elige todos los microdatos en .CSV", filetypes=[('CSV file', '*.csv'), ('All files', '*.*')])

for filez in filename:
    microdatos = pd.read_csv(filez)
    year = filez[-8:-4]
    munidatabase[year + '_SALDO_TOTAL'] = munidatabase['PROVMUNI'].apply(get_saldo_total, df=microdatos)
    munidatabase[year + '_SALDOHOMBRES_TOTAL'] = munidatabase['PROVMUNI'].apply(get_saldo_hombres, df=microdatos)
    munidatabase[year + '_SALDOMUJERES_TOTAL'] = munidatabase['PROVMUNI'].apply(get_saldo_mujeres, df=microdatos)
    munidatabase[year + '_SALDOEXT_TOTAL'] = munidatabase['PROVMUNI'].apply(get_saldo_extranjeros, df=microdatos)

#POR HACER
    munidatabase[year + '_SALDOEXT_HOMBRES'] = munidatabase['PROVMUNI'].apply(get_saldo_hombres, df=microdatos)
    munidatabase[year + '_SALDOEXT_MUJERES'] = munidatabase['PROVMUNI'].apply(get_saldo_mujeres, df=microdatos)


    munidatabase[year + '_SALDOTOTAL_MENORES'] = munidatabase['PROVMUNI'].apply(get_saldo, df=microdatos)
    munidatabase[year + '_SALDOTOTAL_ESTUDIANTES'] = munidatabase['PROVMUNI'].apply(get_saldo_hombres, df=microdatos)
    munidatabase[year + '_SALDOTOTAL_TRABAJADORES'] = munidatabase['PROVMUNI'].apply(get_saldo_mujeres, df=microdatos)
    munidatabase[year + '_SALDOTOTAL_MADUREZ1'] = munidatabase['PROVMUNI'].apply(get_saldo, df=microdatos)
    munidatabase[year + '_SALDOTOTAL_MADUREZ2'] = munidatabase['PROVMUNI'].apply(get_saldo_hombres, df=microdatos)
    munidatabase[year + '_SALDOTOTAL_JUBILADOS'] = munidatabase['PROVMUNI'].apply(get_saldo_mujeres, df=microdatos)

    munidatabase[year + '_SALDOHOMBRES_MENORES'] = munidatabase['PROVMUNI'].apply(get_saldo, df=microdatos)
    munidatabase[year + '_SALDOHOMBRES_ESTUDIANTES'] = munidatabase['PROVMUNI'].apply(get_saldo_hombres, df=microdatos)
    munidatabase[year + '_SALDOHOMBRES_TRABAJADORES'] = munidatabase['PROVMUNI'].apply(get_saldo_mujeres, df=microdatos)
    munidatabase[year + '_SALDOHOMBRES_MADUREZ1'] = munidatabase['PROVMUNI'].apply(get_saldo, df=microdatos)
    munidatabase[year + '_SALDOHOMBRES_MADUREZ2'] = munidatabase['PROVMUNI'].apply(get_saldo_hombres, df=microdatos)
    munidatabase[year + '_SALDOHOMBRES_JUBILADOS'] = munidatabase['PROVMUNI'].apply(get_saldo_mujeres, df=microdatos)

    munidatabase[year + '_SALDOMUJERES_MENORES'] = munidatabase['PROVMUNI'].apply(get_saldo, df=microdatos)
    munidatabase[year + '_SALDOMUJERES_ESTUDIANTES'] = munidatabase['PROVMUNI'].apply(get_saldo_hombres, df=microdatos)
    munidatabase[year + '_SALDOMUJERES_TRABAJADORAS'] = munidatabase['PROVMUNI'].apply(get_saldo_mujeres, df=microdatos)
    munidatabase[year + '_SALDOMUJERES_MADUREZ1'] = munidatabase['PROVMUNI'].apply(get_saldo, df=microdatos)
    munidatabase[year + '_SALDOMUJERES_MADUREZ2'] = munidatabase['PROVMUNI'].apply(get_saldo_hombres, df=microdatos)
    munidatabase[year + '_SALDOMUJERES_JUBILADAS'] = munidatabase['PROVMUNI'].apply(get_saldo_mujeres, df=microdatos)
    

    
    munidatabase[year + '_SALDOEXT_MENORES'] = munidatabase['PROVMUNI'].apply(get_saldo, df=microdatos)
    munidatabase[year + '_SALDOEXT_ESTUDIANTES'] = munidatabase['PROVMUNI'].apply(get_saldo_hombres, df=microdatos)
    munidatabase[year + '_SALDOEXT_TRABAJADORES'] = munidatabase['PROVMUNI'].apply(get_saldo_mujeres, df=microdatos)
    munidatabase[year + '_SALDOEXT_MADUREZ1'] = munidatabase['PROVMUNI'].apply(get_saldo, df=microdatos)
    munidatabase[year + '_SALDOEXT_MADUREZ2'] = munidatabase['PROVMUNI'].apply(get_saldo_hombres, df=microdatos)
    munidatabase[year + '_SALDOEXT_JUBILADOS'] = munidatabase['PROVMUNI'].apply(get_saldo_mujeres, df=microdatos)

    munidatabase[year + '_SALDOEXT_HOMBRES_MENORES'] = munidatabase['PROVMUNI'].apply(get_saldo, df=microdatos)
    munidatabase[year + '_SALDOEXT_HOMBRES_ESTUDIANTES'] = munidatabase['PROVMUNI'].apply(get_saldo_hombres, df=microdatos)
    munidatabase[year + '_SALDOEXT_HOMBRES_TRABAJADORES'] = munidatabase['PROVMUNI'].apply(get_saldo_mujeres, df=microdatos)
    munidatabase[year + '_SALDOEXT_HOMBRES_MADUREZ1'] = munidatabase['PROVMUNI'].apply(get_saldo, df=microdatos)
    munidatabase[year + '_SALDOEXT_HOMBRES_MADUREZ2'] = munidatabase['PROVMUNI'].apply(get_saldo_hombres, df=microdatos)
    munidatabase[year + '_SALDOEXT_HOMBRES_JUBILADOS'] = munidatabase['PROVMUNI'].apply(get_saldo_mujeres, df=microdatos)

    munidatabase[year + '_SALDOEXT_MUJERES_MENORES'] = munidatabase['PROVMUNI'].apply(get_saldo, df=microdatos)
    munidatabase[year + '_SALDOEXT_MUJERES_ESTUDIANTES'] = munidatabase['PROVMUNI'].apply(get_saldo_hombres, df=microdatos)
    munidatabase[year + '_SALDOEXT_MUJERES_TRABAJADORES'] = munidatabase['PROVMUNI'].apply(get_saldo_mujeres, df=microdatos)
    munidatabase[year + '_SALDOEXT_MUJERES_MADUREZ1'] = munidatabase['PROVMUNI'].apply(get_saldo, df=microdatos)
    munidatabase[year + '_SALDOEXT_MUJERES_MADUREZ2'] = munidatabase['PROVMUNI'].apply(get_saldo_hombres, df=microdatos)
    munidatabase[year + '_SALDOEXT_MUJERES_JUBILADOS'] = munidatabase['PROVMUNI'].apply(get_saldo_mujeres, df=microdatos)


munidatabase.to_csv('outputs/variacionesresidencialesAndrea.csv', index=False)