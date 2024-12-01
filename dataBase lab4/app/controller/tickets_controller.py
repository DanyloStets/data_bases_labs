from .general_controller import GeneralController
from ..service import tickets_service


class TicketsController(GeneralController):
    _service = tickets_service
