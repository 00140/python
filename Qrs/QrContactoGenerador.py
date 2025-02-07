
from segno import helpers
# Some params accept multiple values, like email, phone, url
def main():

    qrcodes = helpers.make_vcard(name='Dominguez Sanchez; Erick', displayname='Erick Dominguez Sanchez',
                                email=('kire.erickoz@gmail.com'),
                                #org='',
                                title='Ing. Sistemas Computacionales',
                                #phone='5547737395',
                                cellphone='5547737395',
                                #workphone='',
                                #country='',
                                url=['https://github.com/00140'])
    qrcodes.save('QRCONTACTO.png', scale=4)



if __name__ == "__main__":
    main()