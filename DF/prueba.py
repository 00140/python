import pandas as pd

# Leer el archivo en ISO-8859-1
df = pd.read_csv('/home/erick/Documentos/DatosCSV/Abril/2dasemana.csv', encoding='ISO-8859-1')

# Convertir las cadenas que pueden estar en ISO-8859-1 a UTF-8
def convertir_a_utf8(x):
    if isinstance(x, str):  # Verificar si es una cadena
        try:
            # Intentar decodificar de ISO-8859-1 y luego codificar a UTF-8
            return x.encode('ISO-8859-1').decode('utf-8')
        except UnicodeDecodeError:
            # Si falla, devolver el valor original (puede ser un error en los datos)
            return x
    else:
        return x

# Aplicar la conversión a todo el DataFrame
df = df.applymap(convertir_a_utf8)

# Guardar el archivo convertido
df.to_csv('archivo_convertido_utf8.csv', encoding='utf-8', index=False)

print("Archivo CSV convertido a UTF-8 exitosamente.")
