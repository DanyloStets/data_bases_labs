from .general_controller import GeneralController
from ..service import passanger_service


class PassangerController(GeneralController):
    _service = passanger_service
