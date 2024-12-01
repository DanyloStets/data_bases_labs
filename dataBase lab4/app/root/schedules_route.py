from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import schedules_controller
from ..domain.schedules import Schedules

schedules_bp = Blueprint('schedules', __name__, url_prefix='/schedules')


@schedules_bp.route('', methods=['GET'])
def get_all_schedules() -> Response:
    return make_response(jsonify(schedules_controller.find_all()), HTTPStatus.OK)


@schedules_bp.route('', methods=['POST'])
def create_schedules() -> Response:
    content = request.get_json()
    schedules = Schedules.create_from_dto(content)
    schedules_controller.create(schedules)
    return make_response(jsonify(schedules.put_into_dto()), HTTPStatus.CREATED)


@schedules_bp.route('/<int:schedules_id>', methods=['GET'])
def get_schedules(schedules_id: int) -> Response:
    return make_response(jsonify(schedules_controller.find_by_id(schedules_id)), HTTPStatus.OK)


@schedules_bp.route('/<int:schedules_id>', methods=['PUT'])
def update_schedules(schedules_id: int) -> Response:
    content = request.get_json()
    schedules = Schedules.create_from_dto(content)
    schedules_controller.update(schedules_id, schedules)
    return make_response("schedules updated", HTTPStatus.OK)


@schedules_bp.route('/<int:schedules_id>', methods=['PATCH'])
def patch_schedules(schedules_id: int) -> Response:
    content = request.get_json()
    schedules_controller.patch(schedules_id, content)
    return make_response("schedules updated", HTTPStatus.OK)


@schedules_bp.route('/<int:schedules_id>', methods=['DELETE'])
def delete_schedules(schedules_id: int) -> Response:
    schedules_controller.delete(schedules_id)
    return make_response("schedules deleted", HTTPStatus.OK)
