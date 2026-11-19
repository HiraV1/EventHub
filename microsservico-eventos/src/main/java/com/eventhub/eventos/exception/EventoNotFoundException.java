package com.eventhub.eventos.exception;

public class EventoNotFoundException extends RuntimeException{

    public EventoNotFoundException(String mensagem) {
        super(mensagem);
    }
}
