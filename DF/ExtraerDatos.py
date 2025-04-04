import pandas as pd



def metodo_DatosDia(no_fila, df):

    fila = df.iloc[no_fila]

    valores_extraidos = []
    contador = 0
    vacio15 = 0

    for valor in fila:

        if pd.notna(valor) and valor != "":
            valores_extraidos.append(valor)
        elif contador == 6:
            valores_extraidos.append("Vacio")
        elif contador == 8:
            valores_extraidos.append("Vacio")
        elif contador == 9:
            valores_extraidos.append("Vacio")
        elif contador == 12:
            valores_extraidos.append("Vacio")
        elif contador == 15:
            vacio15 = vacio15 + 1
        elif contador == 16 and vacio15 == 1:
            valores_extraidos.append("Vacio")
        contador = contador + 1

    #for valores in valores_extraidos:
     #   print("Valores ectraidos: ", valores)

    return valores_extraidos

def metodo_DatosFila(no_fila, df):

    fila = df.iloc[no_fila]

    valores_extraidos = []
    
    for valor in fila:
        if pd.notna(valor) and valor != "":
            valores_extraidos.append(valor)

    return valores_extraidos