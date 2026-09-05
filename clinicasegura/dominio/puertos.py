# clinicasegura/dominio/puertos.py
from typing import Protocol
from clinicasegura.dominio.modelos import Despacho, Receta

class Pasarela(Protocol):
    def enviar(self, receta: Receta, cadena: str) -> Despacho: 
        pass

class Reloj(Protocol):
    def ahora(self) -> str:
        pass

class GeneradorFolio(Protocol):
    def siguiente(self) -> str: 
        pass

class Bitacora(Protocol):
    def registrar(self, mensaje: str) -> None: 
        pass