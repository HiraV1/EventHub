from app.models.inscricao import Inscricao
from app.repositories.inscricao_repository import InscricaoRepository
from app.schemas.inscricao import InscricaoCreate, InscricaoUpdate
from app.models.status_inscricao import StatusInscricao
from app.clients.evento_client import EventoClient

from app.exceptions.inscricao_exceptions import (
    InscricaoNaoEncontradaException,
    InscricaoDuplicadaException,
    InscricaoJaCanceladaException,
    EventoIndisponivelException
)

class InscricaoService:

    def __init__(
            self,
            repositorio: InscricaoRepository,
            evento_client: EventoClient
    ):
        self.repositorio = repositorio
        self.evento_client = evento_client

    def cadastrar(self, dados: InscricaoCreate) -> Inscricao:
        evento = self.evento_client.buscar_por_id(dados.evento_id)

        if evento["status"] != "ABERTO":
            raise EventoIndisponivelException(
                "O evento não está aberto para novas inscrições."
            )

        inscricoes = self.repositorio.listar_todos()

        for inscricao in inscricoes:
            mesma_inscricao_ativa = inscricao.status != StatusInscricao.CANCELADA
            mesmo_evento = inscricao.evento_id == dados.evento_id
            mesmo_email = (
                    inscricao.participante_email.casefold()
                    == dados.participante_email.casefold()
            )

            if mesma_inscricao_ativa and mesmo_evento and mesmo_email:
                raise InscricaoDuplicadaException(
                    "O participante já possui uma inscrição neste evento."
                )

        inscricoes_ativas = [
                    inscricao
                    for inscricao in inscricoes
                    if (
                            inscricao.evento_id == dados.evento_id
                            and inscricao.status in (
                                StatusInscricao.PENDENTE,
                                StatusInscricao.CONFIRMADA
                            )
                    )
                ]
        if len(inscricoes_ativas) >= evento["capacidade"]:
            raise EventoIndisponivelException(
                "O evento não possui vagas disponíveis."
            )

        nova_inscricao = Inscricao(**dados.model_dump())

        return self.repositorio.salvar(nova_inscricao)

    def buscar_por_id(self, inscricao_id: int) -> Inscricao:
        inscricao = self.repositorio.buscar_por_id(inscricao_id)

        if inscricao is None:
            raise InscricaoNaoEncontradaException(
                "Inscrição não encontrada."
            )

        return inscricao

    def listar_todos(self) -> list[Inscricao]:
        return self.repositorio.listar_todos()

    def atualizar(
            self,
            inscricao_id: int,
            dados: InscricaoUpdate
    ) -> Inscricao:
        inscricao = self.repositorio.buscar_por_id(inscricao_id)

        if inscricao is None:
            raise InscricaoNaoEncontradaException(
                "Inscrição não encontrada."
            )

        inscricoes = self.repositorio.listar_todos()

        for existente in inscricoes:
            mesma_inscricao_ativa = (
                existente.status != StatusInscricao.CANCELADA
            )
            mesmo_evento = existente.evento_id == inscricao.evento_id
            mesmo_email = (
                existente.participante_email.casefold()
                == dados.participante_email.casefold()
            )
            outra_inscricao = existente.id != inscricao_id

            if (
                    mesma_inscricao_ativa
                    and mesmo_evento
                    and mesmo_email
                    and outra_inscricao
            ):
                raise InscricaoDuplicadaException(
                    "O participante já possui uma inscrição neste evento."
                )

        inscricao.participante_nome = dados.participante_nome
        inscricao.participante_email = dados.participante_email

        return self.repositorio.salvar(inscricao)


    def cancelar(self, inscricao_id: int) -> Inscricao:
        inscricao = self.repositorio.buscar_por_id(inscricao_id)

        if inscricao is None:
            raise InscricaoNaoEncontradaException(
                "Inscrição não encontrada."
            )

        if inscricao.status == StatusInscricao.CANCELADA:
            raise InscricaoJaCanceladaException(
                "A inscrição já está cancelada."
            )

        inscricao.status = StatusInscricao.CANCELADA

        return self.repositorio.salvar(inscricao)