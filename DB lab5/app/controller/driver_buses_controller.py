from .general_controller import GeneralController
from ..service import driver_buses_service


class DriverBusesController(GeneralController):
    _service = driver_buses_service
