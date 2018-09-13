import pandas as pd
from resources import funciones
from tkinter.filedialog import askopenfilenames


munidatabase = pd.read_csv('databases/municipios.csv', sep=';')

filename = askopenfilenames(title= "Elige todos los microdatos en .CSV", filetypes=[('CSV file', '*.csv'), ('All files', '*.*')])

for filez in filename:
    microdatos = pd.read_csv(filez)
    year = filez[-8:-4]
    munidatabase[year + '_SALDO_TOTAL'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_total, df=microdatos)
    
    munidatabase[year + '_SALDOHOMBRES_TOTAL'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_h, df=microdatos)
    munidatabase[year + '_SALDOMUJERES_TOTAL'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_m, df=microdatos)
    
    munidatabase[year + '_SALDOEXT_TOTAL'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_ext, df=microdatos)

    munidatabase[year + '_SALDOEXT_HOMBRES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_ext_h, df=microdatos)
    munidatabase[year + '_SALDOEXT_MUJERES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_ext_m, df=microdatos)

    munidatabase[year + '_SALDOTOTAL_MENORES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_menores, df=microdatos)
    munidatabase[year + '_SALDOTOTAL_ESTUDIANTES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_estudiantes, df=microdatos)
    munidatabase[year + '_SALDOTOTAL_TRABAJADORES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_trabajadores, df=microdatos)
    munidatabase[year + '_SALDOTOTAL_MADUREZ1'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_madurez1, df=microdatos)
    munidatabase[year + '_SALDOTOTAL_MADUREZ2'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_madurez2, df=microdatos)
    munidatabase[year + '_SALDOTOTAL_JUBILADOS'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_jubilados, df=microdatos)

    munidatabase[year + '_SALDOHOMBRES_MENORES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_menores_h, df=microdatos)
    munidatabase[year + '_SALDOHOMBRES_ESTUDIANTES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_estudiantes_h, df=microdatos)
    munidatabase[year + '_SALDOHOMBRES_TRABAJADORES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_trabajadores_h, df=microdatos)
    munidatabase[year + '_SALDOHOMBRES_MADUREZ1'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_madurez1_h, df=microdatos)
    munidatabase[year + '_SALDOHOMBRES_MADUREZ2'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_madurez2_h, df=microdatos)
    munidatabase[year + '_SALDOHOMBRES_JUBILADOS'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_jubilados_h, df=microdatos)

    munidatabase[year + '_SALDOMUJERES_MENORES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_menores_m, df=microdatos)
    munidatabase[year + '_SALDOMUJERES_ESTUDIANTES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_estudiantes_m, df=microdatos)
    munidatabase[year + '_SALDOMUJERES_TRABAJADORAS'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_trabajadores_m, df=microdatos)
    munidatabase[year + '_SALDOMUJERES_MADUREZ1'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_madurez1_m, df=microdatos)
    munidatabase[year + '_SALDOMUJERES_MADUREZ2'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_madurez2_m, df=microdatos)
    munidatabase[year + '_SALDOMUJERES_JUBILADAS'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_jubilados_m, df=microdatos)

    munidatabase[year + '_SALDOEXT_MENORES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_menores_ext, df=microdatos)
    munidatabase[year + '_SALDOEXT_ESTUDIANTES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_estudiantes_ext, df=microdatos)
    munidatabase[year + '_SALDOEXT_TRABAJADORES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_trabajadores_ext, df=microdatos)
    munidatabase[year + '_SALDOEXT_MADUREZ1'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_madurez1_ext, df=microdatos)
    munidatabase[year + '_SALDOEXT_MADUREZ2'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_madurez2_ext, df=microdatos)
    munidatabase[year + '_SALDOEXT_JUBILADOS'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_jubilados_ext, df=microdatos)

    munidatabase[year + '_SALDOEXT_HOMBRES_MENORES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_menores_ext_h, df=microdatos)
    munidatabase[year + '_SALDOEXT_HOMBRES_ESTUDIANTES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_estudiantes_ext_h, df=microdatos)
    munidatabase[year + '_SALDOEXT_HOMBRES_TRABAJADORES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_trabajadores_ext_h, df=microdatos)
    munidatabase[year + '_SALDOEXT_HOMBRES_MADUREZ1'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_madurez1_ext_h, df=microdatos)
    munidatabase[year + '_SALDOEXT_HOMBRES_MADUREZ2'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_madurez2_ext_h, df=microdatos)
    munidatabase[year + '_SALDOEXT_HOMBRES_JUBILADOS'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_jubilados_ext_h, df=microdatos)

    munidatabase[year + '_SALDOEXT_MUJERES_MENORES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_menores_ext_m, df=microdatos)
    munidatabase[year + '_SALDOEXT_MUJERES_ESTUDIANTES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_estudiantes_ext_m, df=microdatos)
    munidatabase[year + '_SALDOEXT_MUJERES_TRABAJADORES'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_trabajadores_ext_m, df=microdatos)
    munidatabase[year + '_SALDOEXT_MUJERES_MADUREZ1'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_madurez1_ext_m, df=microdatos)
    munidatabase[year + '_SALDOEXT_MUJERES_MADUREZ2'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_madurez2_ext_m, df=microdatos)
    munidatabase[year + '_SALDOEXT_MUJERES_JUBILADOS'] = munidatabase['COD_PROVMUNI'].apply(get_saldo_jubilados_ext_m, df=microdatos)

munidatabase.to_csv('outputs/variacionesresidencialesAndrea.csv', index=False)