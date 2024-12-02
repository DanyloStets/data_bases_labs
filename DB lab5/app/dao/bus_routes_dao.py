from .general_dao import GeneralDAO
from ..domain import BusRoutes


class BusRoutesDAO(GeneralDAO):
    _domain_type = BusRoutes
