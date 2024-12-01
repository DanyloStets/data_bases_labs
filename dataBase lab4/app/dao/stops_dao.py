from .general_dao import GeneralDAO
from ..domain import Stops


class StopsDAO(GeneralDAO):
    _domain_type = Stops
