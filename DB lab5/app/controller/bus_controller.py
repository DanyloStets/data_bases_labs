from .general_controller import GeneralController
from ..service import bus_service


class BusController(GeneralController):
    _service = bus_service
