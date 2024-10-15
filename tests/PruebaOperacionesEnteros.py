import unittest
from src.logica.OperacionesEnteros import OperacionesEnteros
from src.logica.FaltanParametros import FaltanParametros


class PruebaOperacionesEnteros(unittest.TestCase):

    def test_MCD_dosNumerosPositivos_retornaMCD(self):
        # Arrange
        operacion = OperacionesEnteros([18, 24])
        resultadoEsperado = 6

        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_tresNumerosPositivos_retornaMCD(self):
        # Arrange
        operacion = OperacionesEnteros([18, 24, 30])
        resultadoEsperado = 6

        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_cuatroNumerosPositivos_retornaMCD(self):
        # Arrange
        operacion = OperacionesEnteros([18, 24, 30, 4])
        resultadoEsperado = 2

        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_unNumeroPositivo_lanzaExcepcion(self):
        # Arrange
        operacion = OperacionesEnteros([18])

        # Assert
        with self.assertRaises(FaltanParametros):
            operacion.calcularMCD()

    def test_MCD_unaCadena_lanzaExcepcion(self):
        # Arrange
        operacion = OperacionesEnteros(["18a", 13])

        # Assert
        with self.assertRaises(ValueError):
            operacion.calcularMCD()


if __name__ == "__main__":
    unittest.main()