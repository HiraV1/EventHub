package com.eventhub.eventos.service;

import com.eventhub.eventos.dto.EventoRequestDTO;
import com.eventhub.eventos.dto.EventoResponseDTO;
import com.eventhub.eventos.exception.EventoNotFoundException;
import com.eventhub.eventos.model.Evento;
import com.eventhub.eventos.repository.EventoRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class EventoService {
    private final EventoRepository eventoRepository;

    public EventoService(EventoRepository eventoRepository) {
        this.eventoRepository = eventoRepository;
    }

    private void validarCapacidade(Integer capacidade) {
        if(capacidade == null || capacidade <= 0) {
            throw new IllegalArgumentException(
                    "A capacidade do evento deve ser maior que zero."
            );
        }
    }

    public EventoResponseDTO cadastrarEvento(EventoRequestDTO dados) {
        validarCapacidade(dados.getCapacidade());

        Evento evento = new Evento(
                dados.getNome(),
                dados.getDescricao(),
                dados.getDataHora(),
                dados.getLocal(),
                dados.getCapacidade(),
                dados.getStatus()
        );

        Evento eventoSalvo = eventoRepository.save(evento);

        return converterParaResponseDTO(eventoSalvo);
    }

    public List<EventoResponseDTO> listarEventos() {
        return eventoRepository.findAll()
                .stream()
                .map(this::converterParaResponseDTO)
                .toList();
    }

    private Evento buscarEntidadePorId(Long id) {
        return eventoRepository.findById(id)
                .orElseThrow(() -> new EventoNotFoundException(
                        "Evento não encontrado com o ID: " + id
                ));
    }

    public EventoResponseDTO buscarEventoPorId(Long id) {
        Evento evento = buscarEntidadePorId(id);

        return converterParaResponseDTO(evento);
    }

    public EventoResponseDTO atualizarEvento(Long id, EventoRequestDTO dados) {
        Evento eventoExistente = buscarEntidadePorId(id);

        validarCapacidade(dados.getCapacidade());

        eventoExistente.setNome(dados.getNome());
        eventoExistente.setDescricao(dados.getDescricao());
        eventoExistente.setDataHora(dados.getDataHora());
        eventoExistente.setLocal(dados.getLocal());
        eventoExistente.setCapacidade(dados.getCapacidade());
        eventoExistente.setStatus(dados.getStatus());

        Evento eventoAtualizado =  eventoRepository.save(eventoExistente);

        return converterParaResponseDTO(eventoAtualizado);
    }

    public void excluirEvento(Long id) {
        Evento evento = buscarEntidadePorId(id);

        eventoRepository.delete(evento);
    }

    private EventoResponseDTO converterParaResponseDTO(Evento evento) {
        return new EventoResponseDTO(
                evento.getId(),
                evento.getNome(),
                evento.getDescricao(),
                evento.getDataHora(),
                evento.getLocal(),
                evento.getCapacidade(),
                evento.getStatus()
        );
    }
}
