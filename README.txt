
ESTRUCTURA DE CARPETAS
-----------------------

/databases: bases de datos no editables que se usan para extraer información.
	/databases/mungal.csv: relación de nombres y códigos de municipios y grupos de acción local a los que pertenecen.
	/databases/provincias.py: diccionarios con las provincias y sus respectivos códigos.
/resources: recursos necesarios para que los programas funcionen, como por ejemplo librerías y funciones creadas por nosotros.
	/resources/easygui.py: librería necesaria para generar ventanas de interacción con el usuario.
	/resources/funciones.py: funciones creadas para usarlas en los programas.
/testfiles: archivos de prueba para confirmar que los programas funcionan y archivos creados por los propios programas.
	/testfiles/2000.txt: muestra muy pequeña de los microdatos que nos manda el INE. 
		Cada línea representa una persona y cada conjunto de dígitos una determinada información de esa persona (Sexo, año de nacimiento, etc)
	/testfiles/2000.csv: resultado del programa 01_microdata_to_csv

/*: los archivos en la carpeta raíz son los programas que creamos (.py). Además hay un cuaderno Jupyter para testear y enseñar ideas. 


NOMENCLATURA DE LOS PROGRAMAS
------------------------------

XX_nombre.py:
			XX: número en base a la jerarquía de uso.
			nombre: breve descripción acerca de la función de ese programa. Los espacios se sustituyen por '_' para facilitar el llamamiento de programas dentro de otros programas.


PROGRAMAS
----------

01_microdata_to_csv: convierte los microdatos que nos manda el INE (.TXT), a un formato que facilita su gestión en python (.CSV).

02_check_number_of_lines: comprueba que los archivos originales (TXT) y los generados en el paso 01 (CSV) tienen la misma cantidad de líneas y por tanto que no se ha perdido ningún dato.

03_add_GAL_y_PROVMUNI: añade al archivo de microdatos las columnas de código GAL de entrada y salida en base a los municipios de entrada y salida. Además añade otras columnas con los códigos PROVMUNI (PPMMM: los dos primeros dígitos (PP) son la provincia y los siguientes tres (MMM) el municipio, para evitar que 2 municipios de provincias diferentes tengan el mismo código).

04_microdata_filtering_by_PROV: filtra los microdatos (CSV) y genera nuevos archivos exclusivamente con las provincias que se quieran.

**05_results: archivo en desarrollo para obtención de resultados y operaciones.

test-jupyternotebook: cuaderno jupyter para testear operaciones o para exponer ideas de forma más visual.
