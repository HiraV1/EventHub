from fastapi import FastAPI

from app.repositories.inscricao_repository import InscricaoRepository
from app.services.inscricao_service import InscricaoService
from app.routers.inscricao_router import router as inscricao_router
from app.exceptions.global_exception_handler import registrar_exception_handlers
from app.clients.evento_client import EventoClient

from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title="EventHub - Microsserviço de Inscrições",
    description="API responsável pelo gerenciamento de inscrições em eventos.",
    version="1.0.0"
)


# Inicialização do Repository e Service
repositorio = InscricaoRepository()
evento_client = EventoClient()

app.state.inscricao_service = InscricaoService(
    repositorio,
    evento_client
)


# Registro das rotas
app.include_router(inscricao_router)


# Registro dos tratamentos globais de exceções
registrar_exception_handlers(app)

# Configuração de métricas para o Prometheus
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

@app.get("/")
def inicio():
    return {
        "mensagem": "Microsserviço de Inscrições do EventHub está funcionando!"
    }
