from .general_dao import GeneralDAO
from ..domain import Driver


class DriverDAO(GeneralDAO):
    _domain_type = Driver
