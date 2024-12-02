from .general_dao import GeneralDAO
from ..domain import Passanger


class PassangerDAO(GeneralDAO):
    _domain_type = Passanger
