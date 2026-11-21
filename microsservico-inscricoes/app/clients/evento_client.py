import os

import httpx

from app.exceptions.inscricao_exceptions import (
    EventoNaoEncontradoException,
    ServicoEventosIndisponivelException
)


class EventoClient:

    def __init__(self):
        self._base_url = os.getenv(
            "EVENTOS_API_URL",
            "http://localhost:8080"
        )

        self._timeout = 5.0

    def buscar_por_id(self, evento_id: int) -> dict:
        url = f"{self._base_url}/api/eventos/{evento_id}"

        try:
            with httpx.Client(timeout=self._timeout) as client:
                resposta = client.get(url)
                resposta.raise_for_status()

                return resposta.json()

        except httpx.HTTPStatusError as erro:

            if erro.response.status_code == 404:
                raise EventoNaoEncontradoException(
                    "O evento informado não existe."
                ) from erro

            raise ServicoEventosIndisponivelException(
                "O serviço de eventos retornou um erro."
            ) from erro

        except httpx.RequestError as erro:
            raise ServicoEventosIndisponivelException(
                "Não foi possível conectar ao serviço de eventos."
            ) from erro