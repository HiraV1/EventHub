from pydantic import BaseModel, ConfigDict, EmailStr, Field

from datetime import datetime

from app.models.status_inscricao import StatusInscricao

class InscricaoCreate(BaseModel):
    evento_id: int = Field(gt=0)
    participante_nome: str = Field(min_length=3, max_length=100)
    participante_email: EmailStr

class InscricaoResponse(BaseModel):
    id: int
    evento_id:int
    participante_nome:str
    participante_email: EmailStr
    data_inscricao: datetime
    status: StatusInscricao

    model_config = ConfigDict(from_attributes=True)

class InscricaoUpdate(BaseModel):
    participante_nome: str = Field(min_length=3, max_length=100)
    participante_email: EmailStr