package com.eventhub.eventos.messaging;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.time.Instant;

public record EventoStatusEvent (
        @JsonProperty("evento_id")
        Long eventoId,

        String tipo,

        @JsonProperty("ocorrido_em")
        Instant ocorridoEm
) {
    public static final String EVENTO_EXCLUIDO = "EVENTO_EXCLUIDO";
    public static final String EVENTO_CANCELADO = "EVENTO_CANCELADO";
}
