# Con esta función buscamos el nombre del municipio a partir de su código
def buscar_muni(value):
    import pandas as pd

    mungal = pd.read_csv('databases/mungal.csv', sep=';')
    munidict = mungal.set_index('MUNICIPIO').to_dict()['CODIGO_MUNICIPIO']
    return next((k for k, v in munidict.items() if v == value), None)


# Con esta función buscamos el nombre de la provincia a partir de su código
def buscar_prov(value):
    from databases.provincias import provincedict
    return next((k for k, v in provincedict.items() if v == value), None)

# Calcular el saldo de variación residencial para un municipio
def get_saldo(municipio, df):
    entradas = df.PROVMUNIALTA[df.PROVMUNIALTA == municipio].count()
    salidas = df.PROVMUNIBAJA[df.PROVMUNIBAJA == municipio].count()
    saldo = entradas - salidas
    return saldo

# Calcular el saldo de variación residencial de hombres para un municipio
def get_saldo_hombres(municipio, df):
    entradas_hombres = df.SEXO[(df.PROVMUNIALTA == municipio) & (df.SEXO == 1)].count()
    salidas_hombres = df.SEXO[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 1)].count()
    saldo_hombres = entradas_hombres - salidas_hombres
    return saldo_hombres

# Calcular el saldo de variación residencial de mujeres para un municipio
def get_saldo_mujeres(municipio, df):
    entradas_mujeres = df.SEXO[(df.PROVMUNIALTA == municipio) & (df.SEXO == 6)].count()
    salidas_mujeres = df.SEXO[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 6)].count()
    saldo_mujeres = entradas_mujeres - salidas_mujeres
    return saldo_mujeres