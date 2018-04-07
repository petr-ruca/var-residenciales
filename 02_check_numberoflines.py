# Comprueba que no se ha perdido ningún dato
from tkinter import messagebox
from tkinter.filedialog import askopenfilenames

filename = askopenfilenames(filetypes=[('CSV file', '*.csv'), ('All files', '*.*')])
for filez in filename:
    num_linescsv = sum(1 for line in open(filez))
    num_linestxt = sum(1 for line in open(filez[:-4] + ".txt"))

    if num_linestxt == num_linescsv:
        messagebox.showinfo("Python:", "El archivo y su respectivo .TXT " + str(filez) +
                            " tienen el mismo numero de filas! En concreto: " + str(num_linescsv))
    else:
        messagebox.showinfo("Python:", "Algo ha ido mal, los archivos " +
                            str(filez) + " no tienen el mismo numero de filas..")
