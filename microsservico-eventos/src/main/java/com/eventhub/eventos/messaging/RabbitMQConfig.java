package com.eventhub.eventos.messaging;

import org.springframework.amqp.core.DirectExchange;
import org.springframework.amqp.core.ExchangeBuilder;
import org.springframework.amqp.core.Queue;
import org.springframework.amqp.core.QueueBuilder;
import org.springframework.amqp.support.converter.JacksonJsonMessageConverter;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class RabbitMQConfig {

    public static final String EVENTOS_EXCHANGE = "eventhub.eventos";
    public static final String EVENTOS_QUEUE = "eventhub.inscricoes.eventos";
    public static final String EVENTOS_ROUTING_KEY = "evento.status.alterado";

    @Bean
    public DirectExchange eventosExchange() {
        return ExchangeBuilder
                .directExchange(EVENTOS_EXCHANGE)
                .durable(true)
                .build();
    }

    @Bean
    public Queue eventosQueue() {
        return QueueBuilder
                .durable(EVENTOS_QUEUE)
                .build();
    }

    @Bean
    public org.springframework.amqp.core.Binding eventosBinding(
            Queue eventosQueue,
            DirectExchange eventosExchange
    ) {
        return org.springframework.amqp.core.BindingBuilder
                .bind(eventosQueue)
                .to(eventosExchange)
                .with(EVENTOS_ROUTING_KEY);
    }

    @Bean
    public JacksonJsonMessageConverter messageConverter() {
        return new JacksonJsonMessageConverter();
    }
}
