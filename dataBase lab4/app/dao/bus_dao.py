from .general_dao import GeneralDAO
from ..domain import Bus


class BusDAO(GeneralDAO):
    _domain_type = Bus
