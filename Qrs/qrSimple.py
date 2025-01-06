import segno
import pandas as pd

Contenido = 'id_libro'
OUTPUT = 'qrcode002F6D.png'

# Make QR code
qr = segno.make(Contenido,version=2)
qr.save(OUTPUT, dark='#002F6D', scale=10,border=2)


#Valores QR
#qr = segno.make(Contenido, error='H')
# version=5, le colocamos la version al codigo qr
# error='H', le colocamos un error en caso de daño


# valores en el guardado
# qrcode.save(qr,dark='#171714', scale=28, border=4, dpi=300)
# qr.save(OUTPUT, finder_dark='#0096FF', scale=10,border=1)
# dark='#002f6c', Color al qr 

