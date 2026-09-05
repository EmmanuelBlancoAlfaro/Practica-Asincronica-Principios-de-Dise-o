# clinicasegura/dominio/reglas.py

def calcular_recargo(dias: int, tarifa_diaria: float, riesgo_alto: bool) -> float:
    """
    Función pura que calcula el recargo de una receta.
    No llama a bases de datos ni lee configuraciones globales.
    """
    if riesgo_alto:
        return tarifa_diaria * dias * 2
    return tarifa_diaria * dias