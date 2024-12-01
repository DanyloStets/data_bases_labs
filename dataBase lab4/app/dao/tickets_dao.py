from .general_dao import GeneralDAO
from ..domain import Tickets


class TicketsDAO(GeneralDAO):
    _domain_type = Tickets
