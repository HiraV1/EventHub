
import asyncio
import json
import logging
import os

import aio_pika
from aio_pika import ExchangeType

from app.repositories.inscricao_repository import InscricaoRepository


logger = logging.getLogger(__name__)


class EventoConsumer:

    EXCHANGE = "eventhub.eventos"
    QUEUE = "eventhub.inscricoes.eventos"
    ROUTING_KEY = "evento.status.alterado"

    TIPOS_EVENTO = {
        "EVENTO_EXCLUIDO",
        "EVENTO_CANCELADO"
    }

    def __init__(self, repositorio: InscricaoRepository):
        self.repositorio = repositorio
        self.connection = None
        self.channel = None
        self.consumer_tag = None

    async def iniciar(self):
        self.connection = await aio_pika.connect_robust(
            host=os.getenv("RABBITMQ_HOST", "localhost"),
            port=int(os.getenv("RABBITMQ_PORT", "5672")),
            login=os.getenv("RABBITMQ_USER", "guest"),
            password=os.getenv("RABBITMQ_PASSWORD", "guest")
        )

        self.channel = await self.connection.channel()

        await self.channel.set_qos(prefetch_count=10)

        exchange = await self.channel.declare_exchange(
            self.EXCHANGE,
            ExchangeType.DIRECT,
            durable=True
        )

        queue = await self.channel.declare_queue(
            self.QUEUE,
            durable=True
        )

        await queue.bind(
            exchange,
            routing_key=self.ROUTING_KEY
        )

        self.consumer_tag = await queue.consume(
            self.processar_mensagem
        )

        logger.info("Consumidor RabbitMQ iniciado.")

    async def processar_mensagem(self, mensagem: aio_pika.IncomingMessage):
        async with mensagem.process(requeue=True):
            dados = json.loads(mensagem.body.decode("utf-8"))

            evento_id = dados.get("evento_id")
            tipo = dados.get("tipo")

            if (
                    not isinstance(evento_id, int)
                    or isinstance(evento_id, bool)
                    or evento_id <= 0
            ):
                raise ValueError("Identificador do evento inválido.")

            if tipo not in self.TIPOS_EVENTO:
                raise ValueError("Tipo de evento não reconhecido.")

            quantidade = await asyncio.to_thread(
                self.repositorio.cancelar_por_evento,
                evento_id
            )

            logger.info(
                "Evento %s recebido. Tipo: %s. "
                "Inscrições canceladas: %s.",
                evento_id,
                tipo,
                quantidade
            )

    async def parar(self):
        if self.channel and self.consumer_tag:
            await self.channel.cancel(self.consumer_tag)

        if self.connection and not self.connection.is_closed:
            await self.connection.close()

        logger.info("Consumidor RabbitMQ encerrado.")
