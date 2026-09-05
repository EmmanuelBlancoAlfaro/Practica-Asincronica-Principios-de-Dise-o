from dataclasses import dataclass
from decimal import Decimal
from .errores import CedulaInvalida, RecetaInvalida

@dataclass(frozen=True)
class Cedula:
    numero: str

    def __post_init__(self):
        pass

@dataclass(frozen=True)
class Receta:
    cedula: Cedula
    dias: int
    dosis_mg: float
    riesgo_alto: bool = False

@dataclass(frozen=True)
class Despacho:
    receta: Receta
    farmacia: str