from pylibdmtx.pylibdmtx import encode
from PIL import Image
import os
import csv
from pathlib import Path

def abs_path():
    return str( Path(__file__).parent.absolute())



def create_datamatrix(data, output_file="datamatrix.png"):
    """
    Crea una imagen Data Matrix a partir de datos dados

    Args:
        data (str): Los datos a codificar
        output_file (str): Nombre del archivo de salida
    """
    try:
        # Convertir el string a bytes usando UTF-8
        data_bytes = bytes(data, encoding='utf-8')

        # Codificar los datos en Data Matrix
        encoded = encode(data_bytes)

        # Crear una imagen PIL desde los datos codificados
        img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)

        # Hacer la imagen más grande para mejor visibilidad
        img_resized = img.resize((encoded.width * 10, encoded.height * 10), Image.NEAREST)

        # Agregar un margen blanco
        border = 50
        new_img = Image.new('RGB', (img_resized.width + 2 * border, img_resized.height + 2 * border), 'white')
        new_img.paste(img_resized, (border, border))

        # Guardar la imagen
        new_img.save(f"{output_file}")
        print(f"Data Matrix creado exitosamente y guardado como {output_file}")
        return True

    except Exception as e:
        print(f"Error al crear el Data Matrix: {str(e)}")
        return False
    
#Crear carpeta de datamatrix
def carpetadatamatrix():
    if not os.path.exists(f"{abs_path()}/generatedatamatrix"):
        os.mkdir(f"{abs_path()}/generatedatamatrix")
        print("La carpeta /generatedatamatrix no existe, vamos a crearla")
    ruta = f"{abs_path()}/generatedatamatrix"
    return ruta

# Crear CSV
def crearcsv(nombre_archivo,texto,ruta):
    with open(f"{ruta}/datos.csv", mode="a",newline="")as file:
        writer = csv.writer(file)
        writer.writerow([nombre_archivo,texto])

#Crear data matrix dividido en carpetas
def creardatamatrix(no_datamatrix,num_carpera,ruta):
    carpeta = 1
    noX_Carpeta = num_carpera
    ruta_carpeta = ""
    os.mkdir(f"{ruta}/{carpeta}")

    ruta_carpeta = (f"{ruta}/{carpeta}/")
    crearcsv("nombre_archivo","Contiene", ruta_carpeta)

    for i in range(1, no_datamatrix+1):
        texto = f"Linde {i:05}"
        create_datamatrix(texto, f"{ruta_carpeta}/{i}.png")
        residuo = i % noX_Carpeta
        crearcsv(i,texto, ruta_carpeta)

        if residuo == 0:
            carpeta = carpeta + 1
            os.mkdir(f"{ruta}/{carpeta}")
            ruta_carpeta = (f"{ruta}/{carpeta}/")
            crearcsv("nombre_archivo","Contiene", ruta_carpeta)
            #os.chdir(f"{i-5} {i}")


if __name__ == "__main__":

    try:
        ruta = carpetadatamatrix()

        numint_datamatrix = int(input("Ingresa el numero de data matrix a generar:"))

        numint_dataxcarpeta = int(input("Ingresa el numero DataMatrix en cada carpeta:"))

        creardatamatrix(numint_datamatrix,numint_dataxcarpeta,ruta)

    except Exception as e:
        print("******* ERROR: Coloca un numero entero de favor ******")
    
    