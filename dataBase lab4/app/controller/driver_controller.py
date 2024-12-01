from .general_controller import GeneralController
from ..service import driver_service


class DriverController(GeneralController):
    _service = driver_service
