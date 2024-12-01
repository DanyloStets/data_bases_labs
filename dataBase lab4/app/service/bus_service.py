from .general_service import GeneralService
from ..dao import bus_dao


class BusService(GeneralService):
    _dao = bus_dao
