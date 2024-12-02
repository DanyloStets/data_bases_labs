from .general_controller import GeneralController
from ..service import stops_service


class StopsController(GeneralController):
    _service = stops_service



