from .general_dao import GeneralDAO
from ..domain import DriverBuses


class DriverBusesDAO(GeneralDAO):
    _domain_type = DriverBuses
