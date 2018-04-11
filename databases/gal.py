# Diccionario de provincias y sus códigos correspondientes
provincedict = {"Extranjero": 66, "Alava": 1, "Albacete": 2, "Alicante": 3, "Almeria": 4,
                "Avila": 5, "Badajoz": 6, "Baleares": 7, "Barcelona": 8, "Burgos": 9, "Caceres": 10, "Cadiz": 11,
                "Castellon": 12, "Ciudad Real": 13, "Cordoba": 14, "A Coruña": 15, "Cuenca": 16, "Girona": 17,
                "Granada": 18, "Guadalajara": 19, "Gipuzkoa": 20, "Huelva": 21, "Huesca": 22, "Jaen": 23, "Leon": 24,
                "Lleida": 25, "La Rioja": 26, "Lugo": 27, "Madrid": 28, "Malaga": 29, "Murcia": 30, "Navarra": 31,
                "Ourense": 32, "Asturias": 33, "Palencia": 34, "Las Palmas": 35, "Pontevedra": 36, "Salamanca": 37,
                "Santa Cruz de Tenerife": 38, "Cantabria": 39, "Segovia": 40, "Sevilla": 41, "Soria": 42,
                "Tarragona": 43, "Teruel": 44, "Toledo": 45, "Valencia": 46, "Valladolid": 47, "Bizkaia": 48,
                "Zamora": 49, "Zaragoza": 50, "Ceuta": 51, "Melilla": 52}

# Lista con todas las provincias
provincelist = ["Extranjero", "Alava", "Albacete", "Alicante", "Almeria",
                "Avila", "Badajoz", "Baleares", "Barcelona", "Burgos", "Caceres", "Cadiz",
                "Castellon", "Ciudad Real", "Cordoba", "A Coruña", "Cuenca", "Girona",
                "Granada", "Guadalajara", "Gipuzkoa", "Huelva", "Huesca", "Jaen", "Leon",
                "Lleida", "La Rioja", "Lugo", "Madrid", "Malaga", "Murcia", "Navarra",
                "Ourense", "Asturias", "Palencia", "Las Palmas", "Pontevedra", "Salamanca",
                "Santa Cruz de Tenerife", "Cantabria", "Segovia", "Sevilla", "Soria",
                "Tarragona", "Teruel", "Toledo", "Valencia", "Valladolid", "Bizkaia",
                "Zamora", "Zaragoza", "Ceuta", "Melilla"]


# Con esta función buscamos el nombre de la provincia a partir de su código


def buscar_prov(value):
    return next((k for k, v in provincedict.items() if v == value), None)
