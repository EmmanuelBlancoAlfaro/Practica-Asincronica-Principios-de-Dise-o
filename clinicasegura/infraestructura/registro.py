# clinicasegura/infraestructura/registro.py

def construir_registro(pasarelas: list) -> dict:
    return {p.cadena: p for p in pasarelas}