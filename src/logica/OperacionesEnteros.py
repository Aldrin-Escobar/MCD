from src.logica.FaltanParametros import FaltanParametros

class OperacionesEnteros:
    def __init__(self, numeros):
        self.__numeros = numeros

    def calcularMCD(self):
        # Verifica si hay al menos dos números
        if len(self.__numeros) < 2:
            raise FaltanParametros("Se requieren al menos dos números para calcular el MCD.")
        return self.MCDMasDosNumeros()

    def MCD(self, numero1, numero2):
        # Algoritmo de Euclides para calcular el MCD
        while numero2 != 0:
            numero1, numero2 = numero2, numero1 % numero2
        return numero1

    def MCDMasDosNumeros(self):
        # Verifica que todos los elementos sean enteros
        for n in self.__numeros:
            if not isinstance(n, int):
                raise ValueError("Todos los elementos deben ser enteros.")

        # Calcula el MCD de más de dos números
        mcd = self.__numeros[0]
        for n in self.__numeros[1:]:
            mcd = self.MCD(mcd, n)
        return mcd