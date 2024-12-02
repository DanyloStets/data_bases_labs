from .general_controller import GeneralController
from ..service import reviews_service


class ReviewsController(GeneralController):
    _service = reviews_service
