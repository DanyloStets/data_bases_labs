from .general_dao import GeneralDAO
from ..domain import Route


class RouteDAO(GeneralDAO):
    _domain_type = Route
