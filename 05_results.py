import pandas as pd
from tkinter.filedialog import askopenfilenames

munidatabase = pd.read_csv('databases/municipios.csv', sep=';')
result = munidatabase
filename = askopenfilenames(title= "Elige todos los microdatos en .CSV", filetypes=[('CSV file', '*.csv'), ('All files', '*.*')])

for filez in filename:
    microdatos = pd.read_csv(filez)
    year = filez[-8:-4]
    
    # Saldo VR TOTAL
    ent = microdatos.groupby('PROVMUNIALTA').size()
    sal = microdatos.groupby('PROVMUNIBAJA').size()
    saldo = ent.sub(sal, fill_value=0).reset_index().astype(int).rename(columns={'index': 'COD_PROVMUNI',0: str(year) + '_SALDOTOTAL'})

    result = pd.merge(result, saldo, on='COD_PROVMUNI')
    
    # Saldo VR TOTAL por GENERO
    ent = microdatos.groupby(['PROVMUNIALTA', 'SEXO']).size().unstack(fill_value=0)
    sal = microdatos.groupby(['PROVMUNIBAJA', 'SEXO']).size().unstack(fill_value=0)
    saldo = ent.sub(sal, fill_value=0).reset_index().astype(int).rename(columns={'index': 'COD_PROVMUNI',1: str(year) + '_SALDOTOTAL_HOMBRES', 6: str(year) + '_SALDOTOTAL_MUJERES'})

    result = pd.merge(result, saldo, on='COD_PROVMUNI')

    # Saldo VR TOTAL de EXTRANJEROS
    ent = microdatos[microdatos.PROVBAJA == 66].groupby('PROVMUNIALTA').size()
    sal = microdatos[microdatos.PROVALTA == 66].groupby('PROVMUNIBAJA').size()
    saldo = ent.sub(sal, fill_value=0).reset_index().astype(int).rename(columns={'index': 'COD_PROVMUNI', 'PROVMUNIALTA': 'COD_PROVMUNI',0: str(year) + '_SALDOEXT_TOTAL'})

    result = pd.merge(result, saldo, on='COD_PROVMUNI')

    # Saldo VR TOTAL por GENERO de EXTRANJEROS
    ent = microdatos[microdatos.PROVBAJA == 66].groupby(['PROVMUNIALTA', 'SEXO']).size().unstack(fill_value=0)
    sal = microdatos[microdatos.PROVALTA == 66].groupby(['PROVMUNIBAJA', 'SEXO']).size().unstack(fill_value=0)
    saldo = ent.sub(sal, fill_value=0).reset_index().astype(int).rename(columns={'index': 'COD_PROVMUNI', 'PROVMUNIALTA': 'COD_PROVMUNI',1: str(year) + '_SALDOEXT_HOMBRES', 6: str(year) + '_SALDOEXT_MUJERES'})

    result = pd.merge(result, saldo, on='COD_PROVMUNI')

    # Saldo VR TOTAL por TRAMOS DE EDAD
    ent = microdatos.groupby(['PROVMUNIALTA',pd.cut(microdatos['EDAD'], (0, 16, 25, 36, 50, 65, 200 ))]).size().unstack(fill_value=0)
    sal = microdatos.groupby(['PROVMUNIBAJA',pd.cut(microdatos['EDAD'], (0, 16, 25, 36, 50, 65, 200 ))]).size().unstack(fill_value=0)
    saldo = ent.sub(sal, fill_value=0).astype(int)
    saldo.columns = [year + '_SALDOTOTAL_MENORES', year + '_SALDOTOTAL_ESTUDIANTES', year + '_SALDOTOTAL_TRABAJADORES', year + '_SALDOTOTAL_MADUREZ1', year + '_SALDOTOTAL_MADUREZ2', year + '_SALDOTOTAL_JUBILADOS']
    saldo = saldo.reset_index().rename(columns={'index': 'COD_PROVMUNI'})

    result = pd.merge(result, saldo, on='COD_PROVMUNI')

    # Saldo VR TOTAL por GENERO y TRAMOS DE EDAD
    microdatos_h = microdatos[microdatos.SEXO == 1].reset_index(drop=True)

    ent = microdatos_h.groupby(['PROVMUNIALTA', pd.cut(microdatos_h['EDAD'], (0, 16, 25, 36, 50, 65, 200 ))]).size().unstack(fill_value=0).astype(int)
    sal = microdatos_h.groupby(['PROVMUNIBAJA', pd.cut(microdatos_h['EDAD'], (0, 16, 25, 36, 50, 65, 200 ))]).size().unstack(fill_value=0).astype(int)

    saldo = ent.sub(sal, fill_value=0).astype(int)
    saldo.columns = [year + '_SALDOHOMBRES_MENORES', year + '_SALDOHOMBRES_ESTUDIANTES', year + '_SALDOHOMBRES_TRABAJADORES', year + '_SALDOHOMBRES_MADUREZ1', year + '_SALDOHOMBRES_MADUREZ2', year + '_SALDOHOMBRES_JUBILADOS']
    saldo = saldo.reset_index().rename(columns={'index': 'COD_PROVMUNI'})

    result = pd.merge(result, saldo, on='COD_PROVMUNI')


    microdatos_m = microdatos[microdatos.SEXO == 6].reset_index(drop=True)

    ent = microdatos_m.groupby(['PROVMUNIALTA', pd.cut(microdatos_m['EDAD'], (0, 16, 25, 36, 50, 65, 200 ))]).size().unstack(fill_value=0).astype(int)
    sal = microdatos_m.groupby(['PROVMUNIBAJA', pd.cut(microdatos_m['EDAD'], (0, 16, 25, 36, 50, 65, 200 ))]).size().unstack(fill_value=0).astype(int)

    saldo = ent.sub(sal, fill_value=0).astype(int)
    saldo.columns = [year + '_SALDOMUJERES_MENORES', year + '_SALDOMUJERES_ESTUDIANTES', year + '_SALDOMUJERES_TRABAJADORES', year + '_SALDOMUJERES_MADUREZ1', year + '_SALDOMUJERES_MADUREZ2', year + '_SALDOMUJERES_JUBILADOS']
    saldo = saldo.reset_index().rename(columns={'index': 'COD_PROVMUNI'})

    result = pd.merge(result, saldo, on='COD_PROVMUNI')


    # Saldo VR para EXTRANJEROS por TRAMOS DE EDAD
    microdatos_ext_baja = microdatos[microdatos.PROVBAJA == 66].reset_index(drop=True)
    microdatos_ext_alta = microdatos[microdatos.PROVALTA == 66].reset_index(drop=True)

    ent = microdatos_ext_baja.groupby(['PROVMUNIALTA',pd.cut(microdatos_ext_baja['EDAD'], (0, 16, 25, 36, 50, 65, 200 ))]).size().unstack(fill_value=0)
    sal = microdatos_ext_alta.groupby(['PROVMUNIBAJA',pd.cut(microdatos_ext_alta['EDAD'], (0, 16, 25, 36, 50, 65, 200 ))]).size().unstack(fill_value=0)

    saldo = ent.sub(sal, fill_value=0).astype(int)
    saldo.columns = [year + '_SALDOEXT_MENORES', year + '_SALDOEXT_ESTUDIANTES', year + '_SALDOEXT_TRABAJADORES', year + '_SALDOEXT_MADUREZ1', year + '_SALDOEXT_MADUREZ2', year + '_SALDOEXT_JUBILADOS']
    saldo = saldo.reset_index().rename(columns={'index': 'COD_PROVMUNI', 'PROVMUNIALTA': 'COD_PROVMUNI'})

    result = pd.merge(result, saldo, on='COD_PROVMUNI')


    # Saldo VR para EXTRANJEROS por TRAMOS DE EDAD y GENERO
    microdatos_h_ext_baja = microdatos[(microdatos.PROVBAJA == 66) & (microdatos.SEXO == 1)].reset_index(drop=True)
    microdatos_h_ext_alta = microdatos[(microdatos.PROVALTA == 66) & (microdatos.SEXO == 1)].reset_index(drop=True)

    ent = microdatos_h_ext_baja.groupby(['PROVMUNIALTA',pd.cut(microdatos_h_ext_baja['EDAD'], (0, 16, 25, 36, 50, 65, 200 ))]).size().unstack(fill_value=0)
    sal = microdatos_h_ext_alta.groupby(['PROVMUNIBAJA',pd.cut(microdatos_h_ext_alta['EDAD'], (0, 16, 25, 36, 50, 65, 200 ))]).size().unstack(fill_value=0)

    saldo = ent.sub(sal, fill_value=0).astype(int)
    saldo.columns = [year + '_SALDOEXT_HOMBRES_MENORES', year + '_SALDOEXT_HOMBRES_ESTUDIANTES', year + '_SALDOEXT_HOMBRES_TRABAJADORES', year + '_SALDOEXT_HOMBRES_MADUREZ1', year + '_SALDOEXT_HOMBRES_MADUREZ2', year + '_SALDOEXT_HOMBRES_JUBILADOS']
    saldo = saldo.reset_index().rename(columns={'index': 'COD_PROVMUNI', 'PROVMUNIALTA': 'COD_PROVMUNI'})

    result = pd.merge(result, saldo, on='COD_PROVMUNI')


    microdatos_m_ext_baja = microdatos[(microdatos.PROVBAJA == 66) & (microdatos.SEXO == 6)].reset_index(drop=True)
    microdatos_m_ext_alta = microdatos[(microdatos.PROVALTA == 66) & (microdatos.SEXO == 6)].reset_index(drop=True)

    ent = microdatos_m_ext_baja.groupby(['PROVMUNIALTA',pd.cut(microdatos_m_ext_baja['EDAD'], (0, 16, 25, 36, 50, 65, 200 ))]).size().unstack(fill_value=0)
    sal = microdatos_m_ext_alta.groupby(['PROVMUNIBAJA',pd.cut(microdatos_m_ext_alta['EDAD'], (0, 16, 25, 36, 50, 65, 200 ))]).size().unstack(fill_value=0)

    saldo = ent.sub(sal, fill_value=0).astype(int)
    saldo.columns = [year + '_SALDOEXT_MUJERES_MENORES', year + '_SALDOEXT_MUJERES_ESTUDIANTES', year + '_SALDOEXT_MUJERES_TRABAJADORES', year + '_SALDOEXT_MUJERES_MADUREZ1', year + '_SALDOEXT_MUJERES_MADUREZ2', year + '_SALDOEXT_MUJERES_JUBILADOS']
    saldo = saldo.reset_index().rename(columns={'index': 'COD_PROVMUNI', 'PROVMUNIALTA': 'COD_PROVMUNI'})

    result = pd.merge(result, saldo, on='COD_PROVMUNI')

    print('Guardada la base de datos del año ' + año + '!!')

result.COD_PROVMUNI = result.COD_PROVMUNI.astype(str).str.zfill(5)

result.to_csv('outputs/' + year + '_VR_database.csv', index=False)
f'Guardada la base de datos del {year}!!'
print('FINALIZADO')