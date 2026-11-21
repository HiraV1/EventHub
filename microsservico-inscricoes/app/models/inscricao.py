
from datetime import datetime, timezone

from sqlalchemy import DateTime, Enum, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.conexao import Base
from app.models.status_inscricao import StatusInscricao


class Inscricao(Base):

    __tablename__ = "inscricoes"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    evento_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        index=True
    )

    participante_nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    participante_email: Mapped[str] = mapped_column(
        String(254),
        nullable=False
    )

    data_inscricao: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    status: Mapped[StatusInscricao] = mapped_column(
        Enum(StatusInscricao, name="status_inscricao"),
        default=StatusInscricao.PENDENTE,
        nullable=False
    )
