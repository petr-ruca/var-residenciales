import pandas as pd

# Abrir archivos necesarios
filename = askopenfilenames(title="Elige los microdatos en .CSV para añadir los códigos GAL y PROVMUNI",
                            filetypes=[('CSV file', '*.csv'), ('All files', '*.*')])

mungal = pd.read_csv('databases/mungal.csv', sep=';')

for filez in filename:
    microdatos = pd.read_csv(filename)

    # Convierte los códigos PROV y MUNI a un único código de 5 dígitos
    microdatos['PROVMUNIALTA'] = microdatos.PROVALTA.astype(
        str).str.zfill(1) + microdatos.MUNIALTA.astype(str).str.zfill(3)

    microdatos['PROVMUNIBAJA'] = microdatos.PROVBAJA.astype(
        str).str.zfill(1) + microdatos.MUNIBAJA.astype(str).str.zfill(3)

    microdatos['PROVMUNIALTA'] = pd.to_numeric(microdatos['PROVMUNIALTA'])
    microdatos['PROVMUNIBAJA'] = pd.to_numeric(microdatos['PROVMUNIBAJA'])

    # Añade el código del GAL del municipio de alta
    microdatos = pd.merge(microdatos, mungal[['CODIGO_MUNICIPIO', 'CODIGO_GAL']], how='left',
                          left_on='PROVMUNIALTA', right_on='CODIGO_MUNICIPIO')

    microdatos.rename(columns={'CODIGO_GAL': 'GALALTA'}, inplace=True)

    del microdatos['CODIGO_MUNICIPIO']

    # Añade el código del GAL del municipio de baja
    microdatos = pd.merge(microdatos, mungal[['CODIGO_MUNICIPIO', 'CODIGO_GAL']], how='left',
                          left_on='PROVMUNIBAJA', right_on='CODIGO_MUNICIPIO')

    microdatos.rename(columns={'CODIGO_GAL': 'GALBAJA'}, inplace=True)

    del microdatos['CODIGO_MUNICIPIO']

    # Guarda los cambios
    microdatos.to_csv(filez, index=False)
