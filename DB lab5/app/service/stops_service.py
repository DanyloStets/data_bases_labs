from .general_service import GeneralService
from ..dao import stops_dao


class StopsService(GeneralService):
    _dao = stops_dao
