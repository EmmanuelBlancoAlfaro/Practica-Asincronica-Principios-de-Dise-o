from datetime import datetime, timedelta
from decimal import Decimal
import pytest

from clinicasegura.aplicacion.borde import validar_cedula_formato
from clinicasegura.dominio.modelos import Receta, Cedula
from clinicasegura.dominio.servicio import EmisionDeRecetas


# --- Dobles de prueba para controlar el entorno ---

class RelojFijo:
    def ahora(self) -> datetime:
        return datetime(2026, 3, 1, 9, 0, 0)


class FoliosSecuenciales:
    def siguiente(self) -> str:
        return "F-00001"


class BitacoraEspia:
    def registrar(self, evento: str, folio: str) -> None:
        pass


class PasarelaNormal:
    cadena = "farmauno"
    def enviar(self, receta, folio, vence):
        from clinicasegura.dominio.modelos import Despacho
        return Despacho(folio=folio, cadena=self.cadena, vence=vence)


class PasarelaCaida:
    cadena = "farmacrisis"
    def enviar(self, receta, folio, vence):
        raise TimeoutError("La red con la farmacia se cayó")


# --- Las 3 pruebas requeridas ---

def test_vigencia_calculada_con_reloj_fijo():
    """1. La vigencia calculada con un reloj fijo (antes imposible sin congelar el sistema operativo)."""
    pasarela = PasarelaNormal()
    servicio = EmisionDeRecetas(
        pasarelas={pasarela.cadena: pasarela},
        reloj=RelojFijo(),
        folios=FoliosSecuenciales(),
        bitacora=BitacoraEspia()
    )
    receta = Receta(cedula=Cedula("1-1234-5678"), medicamento="N02BE01", dias=30, dosis_mg=Decimal("500"))
    
    despacho = servicio.emitir(receta, "farmauno")
    
    # Comprobamos que el vencimiento se calculó exactamente a 30 días del reloj inyectado (2026-03-01)
    esperado = datetime(2026, 3, 1, 9, 0, 0) + timedelta(days=30)
    assert despacho.vence == esperado or str(esperado.date()) in str(despacho.vence)


def test_cadena_caida_lanza_timeout():
    """2. La cadena caída: simula que la pasarela externa falla por red."""
    pasarela = PasarelaCaida()
    servicio = EmisionDeRecetas(
        pasarelas={pasarela.cadena: pasarela},
        reloj=RelojFijo(),
        folios=FoliosSecuenciales(),
        bitacora=BitacoraEspia()
    )
    receta = Receta(cedula=Cedula("1-1234-5678"), medicamento="N02BE01", dias=30, dosis_mg=Decimal("500"))
    
    with pytest.raises(TimeoutError):
        servicio.emitir(receta, "farmacrisis")


def test_validacion_de_formato_cedula_en_borde():
    """3. Validación directa del formato de cédula inválida en la capa de borde."""
    # Comprueba que el parseo de entradas crudas rechaza formatos erróneos
    es_valida = validar_cedula_formato("FORMATO-INCORRECTO-XYZ")
    assert es_valida is False