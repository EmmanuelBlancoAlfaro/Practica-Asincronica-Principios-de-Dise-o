# clinicasegura/infraestructura/folios.py
import uuid

class GeneradorFolioReal:
    def siguiente(self) -> str:
        return str(uuid.uuid4())