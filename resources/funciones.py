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
