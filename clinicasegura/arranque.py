# clinicasegura/arranque.py
import os
from clinicasegura.dominio.servicio import EmisionDeRecetas
from clinicasegura.infraestructura import folios
from clinicasegura.infraestructura.registro import construir_registro

def construir_servicio() -> EmisionDeRecetas:
    timeout = os.getenv("FARMACIA_TIMEOUT_MS", "1500")
    pasarelas = []
    registro = construir_registro(pasarelas)

    return EmisionDeRecetas(pasarelas=registro, reloj=None, folios=folios, bitacora=None)