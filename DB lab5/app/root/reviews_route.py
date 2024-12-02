from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import reviews_controller
from ..domain.reviews import Reviews

reviews_bp = Blueprint('reviews', __name__, url_prefix='/reviews')


@reviews_bp.route('', methods=['GET'])
def get_all_reviews() -> Response:
    """Отримати всі відгуки."""
    return make_response(jsonify(reviews_controller.find_all()), HTTPStatus.OK)


@reviews_bp.route('', methods=['POST'])
def create_review() -> Response:
    """Створити новий відгук."""
    content = request.get_json()
    review = Reviews.create_from_dto(content)
    reviews_controller.create(review)
    return make_response(jsonify(review.put_into_dto()), HTTPStatus.CREATED)


@reviews_bp.route('/<int:review_id>', methods=['GET'])
def get_review(review_id: int) -> Response:
    """Отримати відгук за ID."""
    return make_response(jsonify(reviews_controller.find_by_id(review_id)), HTTPStatus.OK)


@reviews_bp.route('/<int:review_id>', methods=['PUT'])
def update_review(review_id: int) -> Response:
    """Оновити відгук за ID (повністю)."""
    content = request.get_json()
    review = Reviews.create_from_dto(content)
    reviews_controller.update(review_id, review)
    return make_response("Review updated", HTTPStatus.OK)


@reviews_bp.route('/<int:review_id>', methods=['PATCH'])
def patch_review(review_id: int) -> Response:
    """Оновити відгук за ID (частково)."""
    content = request.get_json()
    reviews_controller.patch(review_id, content)
    return make_response("Review updated", HTTPStatus.OK)


@reviews_bp.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id: int) -> Response:
    """Видалити відгук за ID."""
    reviews_controller.delete(review_id)
    return make_response("Review deleted", HTTPStatus.OK)
