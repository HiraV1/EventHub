
import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException

from app.exceptions.inscricao_exceptions import (
    InscricaoException,
    InscricaoNaoEncontradaException,
    InscricaoDuplicadaException,
    InscricaoJaCanceladaException,
    EventoNaoEncontradoException,
    EventoIndisponivelException,
    ServicoEventosIndisponivelException
)


logger = logging.getLogger(__name__)


async def tratar_erro_inscricao(
        request: Request,
        exc: InscricaoException
):
    if isinstance(exc, InscricaoNaoEncontradaException):
        status = 404
        mensagem = "Inscrição não encontrada."

    elif isinstance(exc, EventoNaoEncontradoException):
        status = 404
        mensagem = "Evento não encontrado."

    elif isinstance(exc, EventoIndisponivelException):
        status = 409
        mensagem = "Não foi possível realizar a inscrição."

    elif isinstance(exc, ServicoEventosIndisponivelException):
        status = 503
        mensagem = "Serviço de eventos temporariamente indisponível."

    elif isinstance(exc, InscricaoDuplicadaException):
        status = 409
        mensagem = "Não foi possível realizar a operação."

    elif isinstance(exc, InscricaoJaCanceladaException):
        status = 409
        mensagem = "Não foi possível cancelar a inscrição."

    else:
        status = 400
        mensagem = "Ocorreu um erro na operação."

    return JSONResponse(
        status_code=status,
        content={
            "erros": [str(exc)],
            "mensagem": mensagem,
            "status": status
        }
    )


async def tratar_erro_validacao(
        request: Request,
        exc: RequestValidationError
):
    erros_validacao = exc.errors()

    json_invalido = any(
        erro["type"] == "json_invalid"
        for erro in erros_validacao
    )

    if json_invalido:
        erros = [
            "O corpo da requisição contém um JSON malformado."
        ]
        mensagem = (
            "Um ou mais campos possuem valores em formato inválido."
        )
    else:
        erros = [
            erro["msg"] for erro in erros_validacao
        ]
        mensagem = "Existem erros de validação na requisição."

    return JSONResponse(
        status_code=400,
        content={
            "erros": erros,
            "mensagem": mensagem,
            "status": 400
        }
    )


async def tratar_erro_http(
        request: Request,
        exc: HTTPException
):
    detalhe = exc.detail

    if isinstance(detalhe, list):
        erros = [str(item) for item in detalhe]
    else:
        erros = [str(detalhe)]

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "erros": erros,
            "mensagem": "Não foi possível processar a requisição.",
            "status": exc.status_code
        },
        headers=exc.headers
    )


async def tratar_erro_inesperado(
        request: Request,
        exc: Exception
):
    logger.exception(
        "Erro inesperado no microsserviço de inscrições.",
        exc_info=exc
    )

    return JSONResponse(
        status_code=500,
        content={
            "erros": [
                "Ocorreu um erro interno no servidor."
            ],
            "mensagem": "Não foi possível concluir a operação.",
            "status": 500
        }
    )


def registrar_exception_handlers(app: FastAPI):

    app.add_exception_handler(
        InscricaoException,
        tratar_erro_inscricao
    )

    app.add_exception_handler(
        RequestValidationError,
        tratar_erro_validacao
    )

    app.add_exception_handler(
        HTTPException,
        tratar_erro_http
    )

    app.add_exception_handler(
        Exception,
        tratar_erro_inesperado
    )
