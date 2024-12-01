from .general_dao import GeneralDAO
from ..domain import DriverRoutes


class DriverRoutesDAO(GeneralDAO):
    _domain_type = DriverRoutes
