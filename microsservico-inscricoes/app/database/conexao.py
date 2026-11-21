
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.engine import URL

caminho_env = Path(__file__).resolve().parents[3] / ".env"
load_dotenv(dotenv_path=caminho_env)

DB_USER = os.getenv("INSCRICOES_DB_USER")
DB_PASSWORD = os.getenv("INSCRICOES_DB_PASSWORD")
DB_NAME = os.getenv("INSCRICOES_DB_NAME")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5434"))

if not all([DB_USER, DB_PASSWORD, DB_NAME]):
    raise RuntimeError(
        "As variáveis de ambiente do banco de inscrições não foram configuradas."
    )

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False
)


class Base(DeclarativeBase):
    pass
