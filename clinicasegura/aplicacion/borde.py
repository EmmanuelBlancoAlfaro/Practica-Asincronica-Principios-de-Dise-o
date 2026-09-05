# clinicasegura/aplicacion/borde.py
import re
from decimal import Decimal
from pydantic import BaseModel, Field, field_validator
from clinicasegura.dominio.modelos import Receta, Cedula

class SolicitudReceta(BaseModel):
    cedula: str
    medicamento: str
    dias: int = Field(gt=0, le=90)
    dosis_mg: Decimal = Field(gt=0)

    model_config = {
        "extra": "forbid",
        "frozen": True,
    }

    @field_validator("cedula")
    @classmethod
    def validar_cedula(cls, v):
        if not re.match(r"^\d-\d{4}-\d{4}$", v):
            raise ValueError("la cédula tiene formato 0-0000-0000")
        return v

def a_receta(solicitud: SolicitudReceta) -> Receta:
    """Parsea el DTO validado a los tipos fuertes del dominio."""
    return Receta(
        cedula=Cedula(solicitud.cedula),
        medicamento=solicitud.medicamento,
        dias=solicitud.dias,
        dosis_mg=solicitud.dosis_mg
    )

def validar_cedula_formato(cedula: str) -> bool:
    """Función auxiliar para su prueba propia de la etapa 5."""
    return bool(re.match(r"^\d-\d{4}-\d{4}$", cedula))