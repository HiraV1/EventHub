package com.eventhub.eventos.dto;

import java.util.List;

public class ErroResponseDTO {
    private int status;
    private String mensagem;
    private List<String> erros;

    public ErroResponseDTO(int status, String mensagem) {
        this(status, mensagem, List.of());
    }

    public ErroResponseDTO(
            int status,
            String mensagem,
            List<String> erros
    ) {
        this.status = status;
        this.mensagem = mensagem;
        this.erros = erros;
    }

    public int getStatus() {
        return status;
    }

    public String getMensagem() {
        return mensagem;
    }

    public List<String> getErros() {
        return erros;
    }
}
