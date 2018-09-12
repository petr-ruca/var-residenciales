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

#---------------------------

# VR total del municipio
def get_saldo_total(municipio, df):
    entradas = df.PROVMUNIALTA[df.PROVMUNIALTA == municipio].count()
    salidas = df.PROVMUNIBAJA[df.PROVMUNIBAJA == municipio].count()
    saldo = entradas - salidas
    return saldo

# VR total por género
def get_saldo_hombres(municipio, df):
    entradas_hombres = df.SEXO[(df.PROVMUNIALTA == municipio) & (df.SEXO == 1)].count()
    salidas_hombres = df.SEXO[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 1)].count()
    saldo_hombres = entradas_hombres - salidas_hombres
    return saldo_hombres
def get_saldo_mujeres(municipio, df):
    entradas_mujeres = df.SEXO[(df.PROVMUNIALTA == municipio) & (df.SEXO == 6)].count()
    salidas_mujeres = df.SEXO[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 6)].count()
    saldo_mujeres = entradas_mujeres - salidas_mujeres
    return saldo_mujeres

# VR de extranjeros total
def get_saldo_extranjeros(municipio, df):
    entradas_ext = df.PROVMUNIALTA[(df.PROVMUNIALTA == municipio) & (df.PROVMUNIBAJA == 66)].count()
    salidas_ext = df.PROVMUNIBAJA[(df.PROVMUNIBAJA == municipio) & (df.PROVMUNIALTA == 66)].count()
    saldo_ext = entradas_ext - salidas_ext
    return saldo_ext

# VR de entranjeros por género


# VR total por tramos de edad
def get_saldo_menores(municipio, df):
    age_menores_high = 15

    entradas_menores = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD <= age_menores_high)].count()
    salidas_menores = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD <= age_menores_high)].count()
    saldo_menores = entradas_menores - salidas_menores
    
    return saldo_menores
def get_saldo_estudiantes(municipio, df):
    age_estudiantes_low = 16
    age_estudiantes_high = 24
    
    entradas_estudiantes = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD >= age_estudiantes_low) & (df.EDAD <= age_estudiantes_high)].count()
    salidas_estudiantes = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD >= age_estudiantes_low) & (df.EDAD <= age_estudiantes_high)].count()
    saldo_estudiantes = entradas_estudiantes - salidas_estudiantes
    
    return saldo_estudiantes
def get_saldo_trabajadores(municipio, df):
    age_trabajadores_low = 25
    age_trabajadores_high = 35
    
    entradas_trabajadores = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD >= age_trabajadores_low) & (df.EDAD <= age_trabajadores_high)].count()
    salidas_trabajadores = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD >= age_trabajadores_low) & (df.EDAD <= age_trabajadores_high)].count()
    saldo_trabajadores = entradas_trabajadores - salidas_trabajadores
    
    return saldo_trabajadores
def get_saldo_madurez1(municipio, df):
    age_madurez1_low = 36
    age_madurez1_high = 49

    entradas_madurez1 = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD >= age_madurez1_low) & (df.EDAD <= age_madurez1_high)].count()
    salidas_madurez1 = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD >= age_madurez1_low) & (df.EDAD <= age_madurez1_high)].count()
    saldo_madurez1 = entradas_madurez1 - salidas_madurez1
    
    return saldo_madurez1
def get_saldo_madurez2(municipio, df):
    age_madurez2_low = 50
    age_madurez2_high = 64

    entradas_madurez2 = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD >= age_madurez2_low) & (df.EDAD <= age_madurez2_high)].count()
    salidas_madurez2 = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD >= age_madurez2_low) & (df.EDAD <= age_madurez2_high)].count()
    saldo_madurez2 = entradas_madurez2 - salidas_madurez2

    return saldo_madurez2
def get_saldo_jubilados(municipio, df):
    age_jubilados_low = 65

    entradas_jubilados = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD >= age_jubilados_low)].count()
    salidas_jubilados = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD >= age_jubilados_low)].count()
    saldo_jubilados = entradas_jubilados - salidas_jubilados
    
    return saldo_jubilados

# VR de hombres por tramos de edad

# VR de mujeres por tramos de edad

# VR total de extranjeros por tramos de edad

# VR de hombres extranjeros por tramos de edad

# VR de mujeres extranjeras por tramos de edad


#-----------


# Calcular el saldo de variación residencial de hombres extranjeros para un municipio
def get_saldo_extranjeros_hombres(municipio, df):
    entradas = df.SEXO[(df.PROVMUNIALTA == 66) & (df.SEXO == 1)].count()
    salidas_hombres = df.SEXO[(df.PROVMUNIBAJA == 66) & (df.SEXO == 1)].count()
    saldo = entradas - salidas
    return saldo

# Calcular el saldo de variación residencial de mujeres extranjeras para un municipio
def get_saldo_extranjeros_mujeres(municipio, df):
    entradas = df.SEXO[(df.PROVMUNIALTA == 66) & (df.SEXO == 1)].count()
    salidas_hombres = df.SEXO[(df.PROVMUNIBAJA == 66) & (df.SEXO == 1)].count()
    saldo = entradas - salidas
    return saldo