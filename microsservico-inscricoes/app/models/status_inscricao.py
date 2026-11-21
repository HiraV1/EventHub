from enum import Enum

class StatusInscricao(str, Enum):
    PENDENTE = "PENDENTE"
    CONFIRMADA = "CONFIRMADA"
    CANCELADA = "CANCELADA"