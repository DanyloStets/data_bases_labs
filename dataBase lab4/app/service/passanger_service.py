from .general_service import GeneralService
from ..dao import passanger_dao


class PassangerService(GeneralService):
    _dao = passanger_dao
