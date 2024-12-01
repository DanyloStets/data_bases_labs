from .general_controller import GeneralController
from ..service import bus_routes_service


class BusRoutesController(GeneralController):
    _service = bus_routes_service
