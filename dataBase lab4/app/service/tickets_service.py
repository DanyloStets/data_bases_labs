from .general_service import GeneralService
from ..dao import tickets_dao


class TicketsService(GeneralService):
    _dao = tickets_dao
