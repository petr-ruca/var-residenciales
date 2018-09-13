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

# VR total del municipio
def get_saldo_total(municipio, df):
    entradas = df.PROVMUNIALTA[df.PROVMUNIALTA == municipio].count()
    salidas = df.PROVMUNIBAJA[df.PROVMUNIBAJA == municipio].count()
    saldo = entradas - salidas
    return saldo

# VR total por género
def get_saldo_h(municipio, df):
    entradas_hombres = df.SEXO[(df.PROVMUNIALTA == municipio) & (df.SEXO == 1)].count()
    salidas_hombres = df.SEXO[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 1)].count()
    saldo_hombres = entradas_hombres - salidas_hombres
    return saldo_hombres
def get_saldo_m(municipio, df):
    entradas_mujeres = df.SEXO[(df.PROVMUNIALTA == municipio) & (df.SEXO == 6)].count()
    salidas_mujeres = df.SEXO[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 6)].count()
    saldo_mujeres = entradas_mujeres - salidas_mujeres
    return saldo_mujeres

# VR de extranjeros total
def get_saldo_ext(municipio, df):
    entradas_ext = df.PROVMUNIALTA[(df.PROVMUNIALTA == municipio) & (df.PROVBAJA == 66)].count()
    salidas_ext = df.PROVMUNIBAJA[(df.PROVMUNIBAJA == municipio) & (df.PROVALTA == 66)].count()
    saldo_ext = entradas_ext - salidas_ext
    return saldo_ext

# VR de entranjeros por género
def get_saldo_ext_h(municipio, df):
    entradas_ext_hombres = df.PROVMUNIALTA[(df.PROVMUNIALTA == municipio) & (df.PROVBAJA == 66) & (df.SEXO == 1)].count()
    salidas_ext_hombres = df.PROVMUNIBAJA[(df.PROVMUNIBAJA == municipio) & (df.PROVALTA == 66) & (df.SEXO == 1)].count()
    saldo_ext_hombres = entradas_ext_hombres - salidas_ext_hombres
    return saldo_ext_hombres
def get_saldo_ext_m(municipio, df):
    entradas_ext_mujeres = df.PROVMUNIALTA[(df.PROVMUNIALTA == municipio) & (df.PROVBAJA == 66) & (df.SEXO == 6)].count()
    salidas_ext_mujeres = df.PROVMUNIBAJA[(df.PROVMUNIBAJA == municipio) & (df.PROVALTA == 66) & (df.SEXO == 6)].count()
    saldo_ext_mujeres = entradas_ext_mujeres - salidas_ext_mujeres
    return saldo_ext_mujeres

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
def get_saldo_menores_h(municipio, df):
    age_menores_high = 15

    entradas_menores_h = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD <= age_menores_high) & (df.SEXO == 1)].count()
    salidas_menores_h = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD <= age_menores_high) & (df.SEXO == 1)].count()
    saldo_menores_h = entradas_menores_h - salidas_menores_h
    
    return saldo_menores_h
def get_saldo_estudiantes_h(municipio, df):
    age_estudiantes_low = 16
    age_estudiantes_high = 24
    
    entradas_estudiantes_h = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD >= age_estudiantes_low) & (df.EDAD <= age_estudiantes_high) & (df.SEXO == 1)].count()
    salidas_estudiantes_h = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD >= age_estudiantes_low) & (df.EDAD <= age_estudiantes_high) & (df.SEXO == 1)].count()
    saldo_estudiantes_h = entradas_estudiantes_h - salidas_estudiantes_h
    
    return saldo_estudiantes_h
def get_saldo_trabajadores_h(municipio, df):
    age_trabajadores_low = 25
    age_trabajadores_high = 35
    
    entradas_trabajadores_h = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD >= age_trabajadores_low) & (df.EDAD <= age_trabajadores_high) & (df.SEXO == 1)].count()
    salidas_trabajadores_h = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD >= age_trabajadores_low) & (df.EDAD <= age_trabajadores_high) & (df.SEXO == 1)].count()
    saldo_trabajadores_h = entradas_trabajadores_h - salidas_trabajadores_h
    
    return saldo_trabajadores_h
def get_saldo_madurez1_h(municipio, df):
    age_madurez1_low = 36
    age_madurez1_high = 49

    entradas_madurez1_h = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD >= age_madurez1_low) & (df.EDAD <= age_madurez1_high) & (df.SEXO == 1)].count()
    salidas_madurez1_h = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD >= age_madurez1_low) & (df.EDAD <= age_madurez1_high) & (df.SEXO == 1)].count()
    saldo_madurez1_h = entradas_madurez1_h - salidas_madurez1_h
    
    return saldo_madurez1_h
def get_saldo_madurez2_h(municipio, df):
    age_madurez2_low = 50
    age_madurez2_high = 64

    entradas_madurez2_h = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD >= age_madurez2_low) & (df.EDAD <= age_madurez2_high) & (df.SEXO == 1)].count()
    salidas_madurez2_h = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD >= age_madurez2_low) & (df.EDAD <= age_madurez2_high) & (df.SEXO == 1)].count()
    saldo_madurez2_h = entradas_madurez2_h - salidas_madurez2_h

    return saldo_madurez2_h
def get_saldo_jubilados_h(municipio, df):
    age_jubilados_low = 65

    entradas_jubilados_h = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD >= age_jubilados_low) & (df.SEXO == 1)].count()
    salidas_jubilados_h = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD >= age_jubilados_low) & (df.SEXO == 1)].count()
    saldo_jubilados_h = entradas_jubilados_h - salidas_jubilados_h
    
    return saldo_jubilados_h

# VR de mujeres por tramos de edad
def get_saldo_menores_m(municipio, df):
    age_menores_high = 15

    entradas_menores_m = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD <= age_menores_high) & (df.SEXO == 6)].count()
    salidas_menores_m = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD <= age_menores_high) & (df.SEXO == 6)].count()
    saldo_menores_m = entradas_menores_m - salidas_menores_m
    
    return saldo_menores_m
def get_saldo_estudiantes_m(municipio, df):
    age_estudiantes_low = 16
    age_estudiantes_high = 24
    
    entradas_estudiantes_m = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD >= age_estudiantes_low) & (df.EDAD <= age_estudiantes_high) & (df.SEXO == 6)].count()
    salidas_estudiantes_m = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD >= age_estudiantes_low) & (df.EDAD <= age_estudiantes_high) & (df.SEXO == 6)].count()
    saldo_estudiantes_m = entradas_estudiantes_m - salidas_estudiantes_m
    
    return saldo_estudiantes_m
def get_saldo_trabajadores_m(municipio, df):
    age_trabajadores_low = 25
    age_trabajadores_high = 35
    
    entradas_trabajadores_m = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD >= age_trabajadores_low) & (df.EDAD <= age_trabajadores_high) & (df.SEXO == 6)].count()
    salidas_trabajadores_m = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD >= age_trabajadores_low) & (df.EDAD <= age_trabajadores_high) & (df.SEXO == 6)].count()
    saldo_trabajadores_m = entradas_trabajadores_m - salidas_trabajadores_m
    
    return saldo_trabajadores_m
def get_saldo_madurez1_m(municipio, df):
    age_madurez1_low = 36
    age_madurez1_high = 49

    entradas_madurez1_m = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD >= age_madurez1_low) & (df.EDAD <= age_madurez1_high) & (df.SEXO == 6)].count()
    salidas_madurez1_m = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD >= age_madurez1_low) & (df.EDAD <= age_madurez1_high) & (df.SEXO == 6)].count()
    saldo_madurez1_m = entradas_madurez1_m - salidas_madurez1_m
    
    return saldo_madurez1_m
def get_saldo_madurez2_m(municipio, df):
    age_madurez2_low = 50
    age_madurez2_high = 64

    entradas_madurez2_m = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD >= age_madurez2_low) & (df.EDAD <= age_madurez2_high) & (df.SEXO == 6)].count()
    salidas_madurez2_m = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD >= age_madurez2_low) & (df.EDAD <= age_madurez2_high) & (df.SEXO == 6)].count()
    saldo_madurez2_m = entradas_madurez2_m - salidas_madurez2_m

    return saldo_madurez2_m
def get_saldo_jubilados_m(municipio, df):
    age_jubilados_low = 65

    entradas_jubilados_m = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.EDAD >= age_jubilados_low) & (df.SEXO == 6)].count()
    salidas_jubilados_m = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.EDAD >= age_jubilados_low) & (df.SEXO == 6)].count()
    saldo_jubilados_m = entradas_jubilados_m - salidas_jubilados_m
    
    return saldo_jubilados_m

# VR total de extranjeros por tramos de edad
def get_saldo_menores_ext(municipio, df):
    age_menores_high = 15

    entradas_menores_ext = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.PROVBAJA == 66) & (df.EDAD <= age_menores_high)].count()
    salidas_menores_ext = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.PROVALTA == 66) & (df.EDAD <= age_menores_high)].count()
    saldo_menores_ext = entradas_menores_ext - salidas_menores_ext
    
    return saldo_menores_ext
def get_saldo_estudiantes_ext(municipio, df):
    age_estudiantes_low = 16
    age_estudiantes_high = 24
    
    entradas_estudiantes_ext = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.PROVBAJA == 66) & (df.EDAD >= age_estudiantes_low) & (df.EDAD <= age_estudiantes_high)].count()
    salidas_estudiantes_ext = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.PROVALTA == 66) & (df.EDAD >= age_estudiantes_low) & (df.EDAD <= age_estudiantes_high)].count()
    saldo_estudiantes_ext = entradas_estudiantes_ext - salidas_estudiantes_ext
    
    return saldo_estudiantes_ext
def get_saldo_trabajadores_ext(municipio, df):
    age_trabajadores_low = 25
    age_trabajadores_high = 35
    
    entradas_trabajadores_ext = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.PROVBAJA == 66) & (df.EDAD >= age_trabajadores_low) & (df.EDAD <= age_trabajadores_high)].count()
    salidas_trabajadores_ext = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.PROVALTA == 66) & (df.EDAD >= age_trabajadores_low) & (df.EDAD <= age_trabajadores_high)].count()
    saldo_trabajadores_ext = entradas_trabajadores_ext - salidas_trabajadores_ext
    
    return saldo_trabajadores_ext
def get_saldo_madurez1_ext(municipio, df):
    age_madurez1_low = 36
    age_madurez1_high = 49

    entradas_madurez1_ext = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.PROVBAJA == 66) & (df.EDAD >= age_madurez1_low) & (df.EDAD <= age_madurez1_high)].count()
    salidas_madurez1_ext = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.PROVALTA == 66) & (df.EDAD >= age_madurez1_low) & (df.EDAD <= age_madurez1_high)].count()
    saldo_madurez1_ext = entradas_madurez1_ext - salidas_madurez1_ext
    
    return saldo_madurez1_ext
def get_saldo_madurez2_ext(municipio, df):
    age_madurez2_low = 50
    age_madurez2_high = 64

    entradas_madurez2_ext = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.PROVBAJA == 66) & (df.EDAD >= age_madurez2_low) & (df.EDAD <= age_madurez2_high)].count()
    salidas_madurez2_ext = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.PROVALTA == 66) & (df.EDAD >= age_madurez2_low) & (df.EDAD <= age_madurez2_high)].count()
    saldo_madurez2_ext = entradas_madurez2_ext - salidas_madurez2_ext

    return saldo_madurez2_ext
def get_saldo_jubilados_ext(municipio, df):
    age_jubilados_low = 65

    entradas_jubilados_ext = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.PROVBAJA == 66) & (df.EDAD >= age_jubilados_low)].count()
    salidas_jubilados_ext = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.PROVALTA == 66) & (df.EDAD >= age_jubilados_low)].count()
    saldo_jubilados_ext = entradas_jubilados_ext - salidas_jubilados_ext
    
    return saldo_jubilados_ext

# VR total de hombres extranjeros por tramos de edad
def get_saldo_menores_ext_h(municipio, df):
    age_menores_high = 15

    entradas_menores_ext_h = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.SEXO == 1) & (df.PROVBAJA == 66) & (df.EDAD <= age_menores_high)].count()
    salidas_menores_ext_h = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 1) & (df.PROVALTA == 66) & (df.EDAD <= age_menores_high)].count()
    saldo_menores_ext_h = entradas_menores_ext_h - salidas_menores_ext_h
    
    return saldo_menores_ext_h
def get_saldo_estudiantes_ext_h(municipio, df):
    age_estudiantes_low = 16
    age_estudiantes_high = 24
    
    entradas_estudiantes_ext_h = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.SEXO == 1) & (df.PROVBAJA == 66) & (df.EDAD >= age_estudiantes_low) & (df.EDAD <= age_estudiantes_high)].count()
    salidas_estudiantes_ext_h = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 1) & (df.PROVALTA == 66) & (df.EDAD >= age_estudiantes_low) & (df.EDAD <= age_estudiantes_high)].count()
    saldo_estudiantes_ext_h = entradas_estudiantes_ext_h - salidas_estudiantes_ext_h
    
    return saldo_estudiantes_ext_h
def get_saldo_trabajadores_ext_h(municipio, df):
    age_trabajadores_low = 25
    age_trabajadores_high = 35
    
    entradas_trabajadores_ext_h = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.SEXO == 1) & (df.PROVBAJA == 66) & (df.EDAD >= age_trabajadores_low) & (df.EDAD <= age_trabajadores_high)].count()
    salidas_trabajadores_ext_h = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 1) & (df.PROVALTA == 66) & (df.EDAD >= age_trabajadores_low) & (df.EDAD <= age_trabajadores_high)].count()
    saldo_trabajadores_ext_h = entradas_trabajadores_ext_h - salidas_trabajadores_ext_h
    
    return saldo_trabajadores_ext_h
def get_saldo_madurez1_ext_h(municipio, df):
    age_madurez1_low = 36
    age_madurez1_high = 49

    entradas_madurez1_ext_h = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.SEXO == 1) & (df.PROVBAJA == 66) & (df.EDAD >= age_madurez1_low) & (df.EDAD <= age_madurez1_high)].count()
    salidas_madurez1_ext_h = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 1) & (df.PROVALTA == 66) & (df.EDAD >= age_madurez1_low) & (df.EDAD <= age_madurez1_high)].count()
    saldo_madurez1_ext_h = entradas_madurez1_ext_h - salidas_madurez1_ext_h
    
    return saldo_madurez1_ext_h
def get_saldo_madurez2_ext_h(municipio, df):
    age_madurez2_low = 50
    age_madurez2_high = 64

    entradas_madurez2_ext_h = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.SEXO == 1) & (df.PROVBAJA == 66) & (df.EDAD >= age_madurez2_low) & (df.EDAD <= age_madurez2_high)].count()
    salidas_madurez2_ext_h = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 1) & (df.PROVALTA == 66) & (df.EDAD >= age_madurez2_low) & (df.EDAD <= age_madurez2_high)].count()
    saldo_madurez2_ext_h = entradas_madurez2_ext_h - salidas_madurez2_ext_h

    return saldo_madurez2_ext_h
def get_saldo_jubilados_ext_h(municipio, df):
    age_jubilados_low = 65

    entradas_jubilados_ext_h = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.SEXO == 1) & (df.PROVBAJA == 66) & (df.EDAD >= age_jubilados_low)].count()
    salidas_jubilados_ext_h = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 1) & (df.PROVALTA == 66) & (df.EDAD >= age_jubilados_low)].count()
    saldo_jubilados_ext_h = entradas_jubilados_ext_h - salidas_jubilados_ext_h
    
    return saldo_jubilados_ext_h

# VR total de mujeres extranjeras por tramos de edad
def get_saldo_menores_ext_m(municipio, df):
    age_menores_high = 15

    entradas_menores_ext_m = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.SEXO == 6) & (df.PROVBAJA == 66) & (df.EDAD <= age_menores_high)].count()
    salidas_menores_ext_m = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 6) & (df.PROVALTA == 66) & (df.EDAD <= age_menores_high)].count()
    saldo_menores_ext_m = entradas_menores_ext_m - salidas_menores_ext_m
    
    return saldo_menores_ext_m
def get_saldo_estudiantes_ext_m(municipio, df):
    age_estudiantes_low = 16
    age_estudiantes_high = 24
    
    entradas_estudiantes_ext_m = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.SEXO == 6) & (df.PROVBAJA == 66) & (df.EDAD >= age_estudiantes_low) & (df.EDAD <= age_estudiantes_high)].count()
    salidas_estudiantes_ext_m = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 6) & (df.PROVALTA == 66) & (df.EDAD >= age_estudiantes_low) & (df.EDAD <= age_estudiantes_high)].count()
    saldo_estudiantes_ext_m = entradas_estudiantes_ext_m - salidas_estudiantes_ext_m
    
    return saldo_estudiantes_ext_m
def get_saldo_trabajadores_ext_m(municipio, df):
    age_trabajadores_low = 25
    age_trabajadores_high = 35
    
    entradas_trabajadores_ext_m = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.SEXO == 6) & (df.PROVBAJA == 66) & (df.EDAD >= age_trabajadores_low) & (df.EDAD <= age_trabajadores_high)].count()
    salidas_trabajadores_ext_m = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 6) & (df.PROVALTA == 66) & (df.EDAD >= age_trabajadores_low) & (df.EDAD <= age_trabajadores_high)].count()
    saldo_trabajadores_ext_m = entradas_trabajadores_ext_m - salidas_trabajadores_ext_m
    
    return saldo_trabajadores_ext_m
def get_saldo_madurez1_ext_m(municipio, df):
    age_madurez1_low = 36
    age_madurez1_high = 49

    entradas_madurez1_ext_m = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.SEXO == 6) & (df.PROVBAJA == 66) & (df.EDAD >= age_madurez1_low) & (df.EDAD <= age_madurez1_high)].count()
    salidas_madurez1_ext_m = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 6) & (df.PROVALTA == 66) & (df.EDAD >= age_madurez1_low) & (df.EDAD <= age_madurez1_high)].count()
    saldo_madurez1_ext_m = entradas_madurez1_ext_m - salidas_madurez1_ext_m
    
    return saldo_madurez1_ext_m
def get_saldo_madurez2_ext_m(municipio, df):
    age_madurez2_low = 50
    age_madurez2_high = 64

    entradas_madurez2_ext_m = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.SEXO == 6) & (df.PROVBAJA == 66) & (df.EDAD >= age_madurez2_low) & (df.EDAD <= age_madurez2_high)].count()
    salidas_madurez2_ext_m = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 6) & (df.PROVALTA == 66) & (df.EDAD >= age_madurez2_low) & (df.EDAD <= age_madurez2_high)].count()
    saldo_madurez2_ext_m = entradas_madurez2_ext_m - salidas_madurez2_ext_m

    return saldo_madurez2_ext_m
def get_saldo_jubilados_ext_m(municipio, df):
    age_jubilados_low = 65

    entradas_jubilados_ext_m = df.EDAD[(df.PROVMUNIALTA == municipio) & (df.SEXO == 6) & (df.PROVBAJA == 66) & (df.EDAD >= age_jubilados_low)].count()
    salidas_jubilados_ext_m = df.EDAD[(df.PROVMUNIBAJA == municipio) & (df.SEXO == 6) & (df.PROVALTA == 66) & (df.EDAD >= age_jubilados_low)].count()
    saldo_jubilados_ext_m = entradas_jubilados_ext_m - salidas_jubilados_ext_m
    
    return saldo_jubilados_ext_m