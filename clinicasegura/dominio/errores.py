class ErrorDominio(Exception):
    """Clase base para todos los errores del negocio."""
    pass

class CedulaInvalida(ErrorDominio):
    """Error de dominio: la cédula no cumple el formato esperado."""
    def __init__(self, cedula):
        self.cedula = cedula
        super().__init__(f"Cédula inválida: {cedula}")

class RecetaInvalida(ErrorDominio):
    """Error de dominio: la receta no cumple el formato esperado."""
    def __init__(self, receta):
        self.receta = receta
        super().__init__(f"Receta inválida: {receta}")

class CadenaNoSoportada(ErrorDominio):
    """Error de dominio: la cadena de farmacias no está registrada."""
    pass

class FarmaciaNoDisponible(ErrorDominio):
    """Error de dominio: la farmacia no responde."""
    pass