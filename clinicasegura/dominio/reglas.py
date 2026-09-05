# clinicasegura/dominio/reglas.py

def calcular_recargo(dias_restantes: int, tarifa_diaria: float, recargo_por_riesgo: bool) -> float:
    """
    Función pura que calcula el recargo de una receta.
    No llama a bases de datos ni lee configuraciones globales.
    """
    if recargo_por_riesgo:
        return tarifa_diaria * dias_restantes * 2
    return tarifa_diaria * dias_restantes