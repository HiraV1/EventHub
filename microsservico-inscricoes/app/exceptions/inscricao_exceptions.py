class InscricaoException(Exception):
    """Exceção base do microsserviço de inscrições."""


class InscricaoNaoEncontradaException(InscricaoException):
    """Lançada quando uma inscrição não é encontrada."""


class InscricaoDuplicadaException(InscricaoException):
    """Lançada quando já existe uma inscrição ativa no evento."""


class InscricaoJaCanceladaException(InscricaoException):
    """Lançada quando tentamos cancelar uma inscrição já cancelada."""

class EventoNaoEncontradoException(InscricaoException):
    """Lançada quando o evento informado não existe."""


class EventoIndisponivelException(InscricaoException):
    """Lançada quando o evento não aceita novas inscrições."""


class ServicoEventosIndisponivelException(InscricaoException):
    """Lançada quando não conseguimos consultar o microsserviço de Eventos."""