from .general_service import GeneralService
from ..dao import driver_routes_dao


class DriverRoutesService(GeneralService):
    _dao = driver_routes_dao
