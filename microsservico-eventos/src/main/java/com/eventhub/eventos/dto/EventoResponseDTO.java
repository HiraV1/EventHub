package com.eventhub.eventos.dto;

import com.eventhub.eventos.model.StatusEvento;

import java.time.LocalDateTime;

public class EventoResponseDTO {
    private Long id;
    private String nome;
    private String descricao;
    private LocalDateTime dataHora;
    private String local;
    private Integer capacidade;
    private StatusEvento status;

    public EventoResponseDTO() {}
    public EventoResponseDTO(
            Long id,
            String nome,
            String descricao,
            LocalDateTime dataHora,
            String local,
            Integer capacidade,
            StatusEvento status
    ) {
        this.id = id;
        this.nome = nome;
        this.descricao = descricao;
        this.dataHora = dataHora;
        this.local = local;
        this.capacidade = capacidade;
        this.status = status;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public LocalDateTime getDataHora() {
        return dataHora;
    }

    public void setDataHora(LocalDateTime dataHora) {
        this.dataHora = dataHora;
    }

    public String getLocal() {
        return local;
    }

    public void setLocal(String local) {
        this.local = local;
    }

    public Integer getCapacidade() {
        return capacidade;
    }

    public void setCapacidade(Integer capacidade) {
        this.capacidade = capacidade;
    }

    public StatusEvento getStatus() {
        return status;
    }

    public void setStatus(StatusEvento status) {
        this.status = status;
    }
}
