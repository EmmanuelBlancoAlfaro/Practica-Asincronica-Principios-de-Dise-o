# clinicasegura/dominio/servicio.py
from clinicasegura.dominio.modelos import Receta

class EmisionDeRecetas:
    def __init__(self, tarifa_diaria: float, vigencia_dias: int):
        # La configuración se recibe por el constructor y se guarda como estado de la instancia.
        self.tarifa_diaria = tarifa_diaria
        self.vigencia_dias = vigencia_dias

    def emitir(self, receta: Receta):
        # Recibe un objeto Receta puro del dominio, no un diccionario crudo.
        pass