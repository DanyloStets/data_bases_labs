from .general_controller import GeneralController
from ..service import route_service


class RouteController(GeneralController):
    _service = route_service
