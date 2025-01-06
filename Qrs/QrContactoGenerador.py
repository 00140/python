
from segno import helpers
# Some params accept multiple values, like email, phone, url
def main():

    qrcodes = helpers.make_vcard(name='APELLIDOS; NOMBRE', displayname='NOMBRE APELLIDO',
                                email=(''),
                                org='',
                                title='',
                                phone='',
                                cellphone='',
                                workphone='',
                                country='',
                                url=[''])
    qrcodes.save('QRCONTACTO.png', scale=4)



if __name__ == "__main__":
    main()