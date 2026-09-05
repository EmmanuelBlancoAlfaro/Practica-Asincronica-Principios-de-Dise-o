# clinicasegura/aplicacion/borde.py
import re
import uuid

def validar_cedula_formato(cedula: str) -> bool:
    patron = re.compile(r"^\d{1}-\d{4}-\d{4}$")
    return bool(patron.match(cedula))

def generar_folio_seguro() -> str:
    return str(uuid.uuid4())