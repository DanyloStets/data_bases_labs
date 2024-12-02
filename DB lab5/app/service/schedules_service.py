from .general_service import GeneralService
from ..dao import schedules_dao


class SchedulesService(GeneralService):
    _dao = schedules_dao
