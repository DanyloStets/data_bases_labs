from .general_dao import GeneralDAO
from ..domain import Schedules


class SchedulesDAO(GeneralDAO):
    _domain_type = Schedules
