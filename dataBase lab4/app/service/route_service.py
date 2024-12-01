from .general_service import GeneralService
from ..dao import route_dao


class RouteService(GeneralService):
    _dao = route_dao
