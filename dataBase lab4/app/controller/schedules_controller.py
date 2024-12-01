from .general_controller import GeneralController
from ..service import schedules_service


class SchedulesController(GeneralController):
    _service = schedules_service
