package com.eventhub.eventos.messaging;

import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.stereotype.Component;

import java.time.Instant;

@Component
public class EventoProducer {

    private final RabbitTemplate rabbitTemplate;

    public EventoProducer(RabbitTemplate rabbitTemplate) {
        this.rabbitTemplate = rabbitTemplate;
    }

    public void publicarEventoStatus(
            Long eventoId,
            String tipo
    ) {
        EventoStatusEvent evento = new EventoStatusEvent(
                eventoId,
                tipo,
                Instant.now()
        );

        rabbitTemplate.convertAndSend(
                RabbitMQConfig.EVENTOS_EXCHANGE,
                RabbitMQConfig.EVENTOS_ROUTING_KEY,
                evento
        );
    }
}
