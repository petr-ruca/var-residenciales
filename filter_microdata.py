#Numero de campo respecto al diseño del fichero de microdatos INE:
#PROVALTA y MUNIALTA: campos 8 y 9 (python empieza a contar desde 0,
# así que hay que restar 1 a cada campo)
#PROVBAJA y MUNIBAJA: campos 12 y 13
import csv
import provincias
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, askopenfilenames


filename = askopenfilenames(title="Elige los microdatos en .CSV para filtrarlos por provincia",filetypes=[('CSV file','*.csv'), ('All files','*.*')])

for filez in filename:
    data_content = open(filez).read()
    lines = open(filez).readlines()

    #Abre la base de datos de las provincias
    from provincias import chosenprov_codes

    #Con esto convierte cada linea en una lista, y engloba todas en una superlista
    #Así podemos acceder a cada dato con lineslist[numerolinea][posiciondato]
    #lineslist = [[int(x) for x in rec] for rec in csv.reader(lines, delimiter=',')]
    lineslist = [[int(x) for x in rec] for rec in csv.reader(lines, delimiter=',')]

    #Empieza el loop para filtrar los movimientos por provincia
    for provcode in chosenprov_codes:
        filteredoutput = []
        for line in lineslist:
            #print(line[0])
            if line[7] == provcode or line[11] == provcode:
                filteredoutput.append(line)
            else:
                pass

        savename = filez[:-4] + "_PROV" + str(provcode)
        with open("{0}.csv".format(savename), "w") as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(filteredoutput)


messagebox.showinfo("CARL SAGAN:", "Parece que todo ha ido fenómeno")
#print (filteredoutput)
