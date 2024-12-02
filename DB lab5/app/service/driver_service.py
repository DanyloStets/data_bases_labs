from .general_service import GeneralService
from ..dao import driver_dao


class DriverService(GeneralService):
    _dao = driver_dao
