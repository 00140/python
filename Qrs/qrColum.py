import segno
import pandas as pd

OUTPUT = 'qrcode.png'
URL = 'QR/TIJUANA/'

# Make QR code


def main():
    archivo_excel = f"{URL}CODIGOS QR TIJUANA.xlsx"
    df = pd.read_excel(archivo_excel, header=2)

    #header=2, Desde que fila empieza


    def qr_generador(Contenido: str,NomArchivo: str):
        qr = segno.make(Contenido,version=2)
        RUTA = f"{URL}/QRS/{NomArchivo}"
        qr.save(f"{RUTA}.png", scale=10,border=0)

        print(f"Generado: {Contenido} Con nombre: {NomArchivo}")
        print(f"Guardao en {RUTA}")
        
    conteo = 0

    for index, row in df.iterrows():
        
        #Las columnas que vamos a tomar del archivo

        #id_libroexcel = row['ID']
        titulo_libroexcel = row['CODIGOS QR']

        datosColum = f"{titulo_libroexcel}"
#        print(datosColum)
        conteo = conteo + 1
        qr_generador(datosColum, conteo)

if __name__ == "__main__":
    main()