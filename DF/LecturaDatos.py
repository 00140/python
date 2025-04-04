import pandas as pd

from ExtraerDatos import *

from Empleado import Empleado

from GuardarDatos import *

def LeerCSVDF():
    archivo_csv = 'archivo_convertido_utf8.csv'

    # Leer el archivo CSV completo
    df = pd.read_csv(archivo_csv, encoding='utf-8')
    df = df.fillna("")

    # Mostrar el contenido
    df = df.dropna()
    print(df)

    numero_filas = len(df)

    df.to_csv('archivo_resultante2.txt', sep=',', index=False)

    df = pd.read_csv('archivo_resultante2.txt', sep=',', header=None)

    fechas = []

    for i in range(0, numero_filas):
        datosi = metodo_DatosFila(i, df)
        if datosi[0] == "CALCOMANIAS TRADICIONALES S.A. DE C.V.":
            y = i + 2
            datosNombre = metodo_DatosFila(y, df)
            print(datosNombre[1])
        else:
            dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
            for dia in dias:
                if datosi[0] == dia:
                    diaLV = metodo_DatosDia(i,df)
                    print(diaLV)
