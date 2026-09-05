# clinicasegura/dominio/servicio.py
from clinicasegura.dominio.modelos import Receta, Despacho
from clinicasegura.dominio.errores import CadenaNoSoportada
from datetime import timedelta

class EmisionDeRecetas:
    def __init__(self, pasarelas: dict, reloj, folios, bitacora):
        # La configuración se recibe por el constructor y se guarda como estado de la instancia.
        self.pasarelas = pasarelas
        self.reloj = reloj
        self.folios = folios
        self.bitacora = bitacora

    def emitir(self, receta: Receta, cadena: str) -> Despacho:
        cadena_lower = cadena.lower()
        if cadena_lower not in self.pasarelas:
            raise CadenaNoSoportada(cadena)
        
        pasarela = self.pasarelas[cadena_lower]
        folio = self.folios.siguiente()
        fecha_base = self.reloj.ahora()
        vence = fecha_base + timedelta(days=receta.dias)
        
        try:
            despacho = pasarela.enviar(receta, folio, vence)
        except Exception as e:
            # Fallar rápido no significa fallar en silencio: deje rastro.
            self.bitacora.registrar("FALLA_FARMACIA", folio)
            from clinicasegura.dominio.errores import FarmaciaNoDisponible
            raise FarmaciaNoDisponible(f"Falla en cadena: {cadena_lower} para folio: {folio}") from e
        self.bitacora.registrar("EMISION", folio)
        return despacho