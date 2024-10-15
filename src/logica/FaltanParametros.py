class FaltanParametros(Exception):
    def __init__(self, mensaje="Faltan parámetros necesarios"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
