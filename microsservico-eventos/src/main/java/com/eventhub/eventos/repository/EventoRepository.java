package com.eventhub.eventos.repository;

import com.eventhub.eventos.model.Evento;
import com.eventhub.eventos.model.StatusEvento;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface EventoRepository extends JpaRepository<Evento, Long> {
    List<Evento> findByStatusNot(StatusEvento status);
}
