from .general_service import GeneralService
from ..dao import bus_routes_dao


class BusRoutesService(GeneralService):
    _dao = bus_routes_dao
