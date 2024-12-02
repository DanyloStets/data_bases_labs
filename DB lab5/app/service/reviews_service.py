from .general_service import GeneralService
from ..dao import reviews_dao


class ReviewsService(GeneralService):
    _dao = reviews_dao
