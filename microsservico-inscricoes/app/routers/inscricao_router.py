from fastapi import APIRouter, Depends, Path, Request, Response, status

from app.schemas.inscricao import (
    InscricaoCreate,
    InscricaoResponse,
    InscricaoUpdate
)

from app.services.inscricao_service import InscricaoService

router = APIRouter(
    prefix="/api/inscricoes",
    tags=["Inscrições"]
)

def obter_inscricao_service(request: Request) -> InscricaoService:
    return request.app.state.inscricao_service

@router.post(
    "",
    response_model=InscricaoResponse,
    status_code=status.HTTP_201_CREATED
)
def cadastrar_inscricao(
        dados: InscricaoCreate,
        service: InscricaoService = Depends(obter_inscricao_service)
):
    return service.cadastrar(dados)

@router.get(
    "",
    response_model=list[InscricaoResponse],
    status_code=status.HTTP_200_OK
)
def listar_inscricoes(
        service: InscricaoService = Depends(obter_inscricao_service)
):
    return service.listar_todos()

@router.get(
    "/{inscricao_id}",
    response_model=InscricaoResponse,
    status_code=status.HTTP_200_OK
)
def buscar_inscricao(
        inscricao_id: int = Path(gt=0),
        service: InscricaoService = Depends(obter_inscricao_service)
):
    return service.buscar_por_id(inscricao_id)

@router.put(
    "/{inscricao_id}",
    response_model=InscricaoResponse,
    status_code=status.HTTP_200_OK
)
def atualizar_inscricao(
        dados: InscricaoUpdate,
        inscricao_id: int = Path(gt=0),
        service: InscricaoService = Depends(obter_inscricao_service)
):
    return service.atualizar(inscricao_id, dados)

@router.delete(
    "/{inscricao_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def cancelar_inscricao(
        inscricao_id: int = Path(gt=0),
        service: InscricaoService = Depends(obter_inscricao_service)
) -> Response:
    service.cancelar(inscricao_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)