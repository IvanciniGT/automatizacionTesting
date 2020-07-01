from unittest import TestCase
from selenium_login import hacer_login


class Test(TestCase):

    RUTA_IMAGENES = '/home/usuario/Imágenes'

    def test_hacer_login_correcto(self):
        resultado = hacer_login('admin', '12345', 'correcto', Test.RUTA_IMAGENES)
        self.assertEqual(resultado,"WELCOME :)")

    def test_hacer_login_incorrecto_password(self):
        resultado = hacer_login('admin', 'RUINA', 'password_incorrecto', Test.RUTA_IMAGENES)
        self.assertEqual(resultado,"ACCESS DENIED!")

    def test_hacer_login_incorrecto_usuario(self):
        resultado = hacer_login('RUINA', 'password','usuario_incorrecto', Test.RUTA_IMAGENES)
        self.assertEqual(resultado,"ACCESS DENIED!")

    def test_hacer_login_incorrecto(self):
        resultado = hacer_login('RUINA', 'RUINA','incorrecto', Test.RUTA_IMAGENES)
        self.assertEqual(resultado,"ACCESS DENIED!")

    def test_hacer_login_vacio(self):
        resultado = hacer_login('', '','vacio', Test.RUTA_IMAGENES)
        self.assertEqual(resultado,"ACCESS DENIED!")
