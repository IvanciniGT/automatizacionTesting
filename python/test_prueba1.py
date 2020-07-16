from unittest import TestCase
from prueba1 import es_impar, mayuscular, numero_palabras

class Test(TestCase):

    def test_es_impar(self):
        resultado = es_impar(5)
        resultado_esperado = True
        self.assertEqual(resultado,resultado_esperado)

    def test_es_impar2(self):
        resultado = es_impar(-1)
        self.assertTrue(resultado)

    def test_es_impar3(self):
        resultado = es_impar(9)
        self.assertTrue(resultado)

    def test_no_es_impar(self):
        resultado = es_impar(4)
        self.assertFalse(resultado)

    def test_mayuscular_1(self):
        resultado = mayuscular("Hola amigo")
        self.assertEqual(resultado,"HOLA AMIGO")

    def test_mayuscular_2(self):
        resultado = mayuscular("ESTO YA ESTA EN MAYUSCULAS")
        self.assertEqual(resultado,"ESTO YA ESTA EN MAYUSCULAS")

    def test_numero_palabras_1(self):
        resultado = numero_palabras("")
        self.assertEqual(resultado,0)

    def test_numero_palabras_2(self):
        resultado = numero_palabras("Aqui hay 4 palabras")
        self.assertEqual(resultado,4)

    def test_numero_palabras_3(self):
        resultado = numero_palabras("SoloUnaPalabra")
        self.assertEqual(resultado,1)
