package com.eventhub.eventos.dto;

import com.eventhub.eventos.model.StatusEvento;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

import java.time.LocalDateTime;

public class EventoRequestDTO {
    @NotBlank(message = "O nome do evento é obrigatório.")
    @Size(max = 120, message = "O nome deve ter no máximo 120 caracteres.")
    private String nome;

    @Size(max = 1000, message = "A descrição deve ter no máximo 1000 caracteres.")
    private String descricao;

    @NotNull(message = "A data e hora do evento são obrigatórias.")
    private LocalDateTime dataHora;

    @NotBlank(message = "O local do evento é obrigatório.")
    @Size(max = 200, message = "O local deve ter no máximo 200 caracteres.")
    private String local;

    @NotNull(message = "A capacidade do evento é obrigatória.")
    @Min(value = 1, message = "A capacidade deve ser de pelo menos 1 participante.")
    private Integer capacidade;

    @NotNull(message = "O status do evento é obrigatório.")
    private StatusEvento status;

    public String getNome() {
        return nome;
    }

    public String getDescricao() {
        return descricao;
    }

    public LocalDateTime getDataHora() {
        return dataHora;
    }

    public String getLocal() {
        return local;
    }

    public Integer getCapacidade() {
        return capacidade;
    }

    public StatusEvento getStatus() {
        return status;
    }
}
