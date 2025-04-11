import unittest
from suma import Suma

class MyTestCase(unittest.TestCase):
    def test_suma_dosNumeros_retornaSuma(self):
        # Arrange
        operando1 = 10
        operando2 = 15
        resultadoEsperado = 25

        objSuma = Suma(operando1, operando2)

        # Act
        resultadoActual = objSuma.calcularsuma()

        # Assert
        self.assertEqual(resultadoEsperado,resultadoActual,msg="Fallo la suma")

    def test_suma_operadorNoNumerico_lanzaExcepcion(self):
        objSuma = Suma(operando1=3, operando2="A")
        with self.assertRaises(TypeError):
            objSuma.calcularsuma()


if __name__ == '__main__':
    unittest.main()
