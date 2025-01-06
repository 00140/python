import segno
import pandas as pd
from qrcode.image.styles.moduledrawers import CircleModuleDrawer
from segno import helpers
from PIL import Image
# Some params accept multiple values, like email, phone, url
def main():
    archivo_excel = 'libros/BDLIBROS.xlsx'
    df = pd.read_excel(archivo_excel)

    def qr_calco(id_libro: str):
        URL = id_libro
        logo = 'LOGOCT2.png'
        OUTPUT = 'qrlibros/'+id_libro+'qrcode.png'

        # Make QR code
        qr = segno.make(URL, error='H')
        qr.save(OUTPUT, finder_dark='#0096FF', scale=10,border=1)

        # Now open that png image to put the logo
        img = Image.open(OUTPUT).convert("RGBA")

        width, height = img.size

        # How big the logo we want to put in the qr code png
        logo_size = 60

        # Open the logo image
        logo = Image.open(logo).convert("RGBA")

        # Calculate xmin, ymin, xmax, ymax to put the logo
        xmin = ymin = int((width / 2) - (logo_size / 2))
        xmax = ymax = int((width / 2) + (logo_size / 2))

        # resize the logo as calculated
        logo = logo.resize((xmax - xmin, ymax - ymin))

        # put the logo in the qr code
        img.paste(logo, (xmin, ymin, xmax, ymax))

        # img.show()
        img.save(OUTPUT)

    for index, row in df.iterrows():
        id_libroexcel = row['ID']
        titulo_libroexcel = row['Titulo']

        qr_libro = f"{id_libroexcel} {titulo_libroexcel}"
        print(qr_libro)
        qr_calco(qr_libro)







if __name__ == "__main__":
    main()