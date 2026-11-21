package com.eventhub.eventos.controller;

import com.eventhub.eventos.dto.EventoRequestDTO;
import com.eventhub.eventos.dto.EventoResponseDTO;
import com.eventhub.eventos.service.EventoService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PatchMapping;

import java.util.List;

@RestController
@RequestMapping("/api/eventos")
public class EventoController {
    private final EventoService eventoService;

    public EventoController(EventoService eventoService) {
        this.eventoService = eventoService;
    }

    @PostMapping
    public ResponseEntity<EventoResponseDTO> cadastrarEvento(
            @Valid @RequestBody EventoRequestDTO dados
    ) {
        EventoResponseDTO evento = eventoService.cadastrarEvento(dados);

        return ResponseEntity.status(HttpStatus.CREATED).body(evento);
    }

    @GetMapping
    public ResponseEntity<List<EventoResponseDTO>> listarEventos() {
        return ResponseEntity.ok(eventoService.listarEventos());
    }

    @GetMapping("/{id}")
    public ResponseEntity<EventoResponseDTO> buscarEventoPorId(
            @PathVariable Long id
    ) {
        return ResponseEntity.ok(eventoService.buscarEventoPorId(id));
    }

    @PutMapping("/{id}")
    public ResponseEntity<EventoResponseDTO> atualizarEvento(
            @PathVariable Long id,
            @Valid @RequestBody EventoRequestDTO dados
    ) {
        EventoResponseDTO evento = eventoService.atualizarEvento(id, dados);

        return ResponseEntity.ok(evento);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> excluirEvento(@PathVariable Long id) {
        eventoService.excluirEvento(id);

        return ResponseEntity.noContent().build();
    }

    @PatchMapping("/{id}/encerrar")
    public ResponseEntity<Void> encerrarEvento(@PathVariable Long id) {
        eventoService.encerrarEvento(id);

        return ResponseEntity.noContent().build();
    }

    @PatchMapping("/{id}/cancelar")
    public ResponseEntity<Void> cancelarEvento(@PathVariable Long id) {
        eventoService.cancelarEvento(id);

        return ResponseEntity.noContent().build();
    }
}
