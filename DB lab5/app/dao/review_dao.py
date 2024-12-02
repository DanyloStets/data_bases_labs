from .general_dao import GeneralDAO
from ..domain import Reviews


class ReviewsDAO(GeneralDAO):
    _domain_type = Reviews
