from .general_controller import GeneralController
from ..service import driver_routes_service


class DriverRoutesController(GeneralController):
    _service = driver_routes_service
