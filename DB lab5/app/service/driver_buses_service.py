from .general_service import GeneralService
from ..dao import driver_buses_dao


class DriverBusesService(GeneralService):
    _dao = driver_buses_dao
