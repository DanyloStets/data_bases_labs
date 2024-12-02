from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import passanger_controller
from ..domain.passanger import Passanger

passanger_bp = Blueprint('passenger', __name__, url_prefix='/passenger')


@passanger_bp.route('', methods=['GET'])
def get_all_passanger() -> Response:
    return make_response(jsonify(passanger_controller.find_all()), HTTPStatus.OK)


@passanger_bp.route('', methods=['POST'])
def create_stops() -> Response:
    content = request.get_json()
    passenger = Passanger.create_from_dto(content)
    passanger_controller.create(passenger)
    return make_response(jsonify(passenger.put_into_dto()), HTTPStatus.CREATED)


@passanger_bp.route('/<int:passanger_id>', methods=['GET'])
def get_passanger(passanger_id: int) -> Response:
    return make_response(jsonify(passanger_controller.find_by_id(passanger_id)), HTTPStatus.OK)


@passanger_bp.route('/<int:passanger_id>', methods=['PUT'])
def update_passanger(passanger_id: int) -> Response:
    content = request.get_json()
    passenger = Passanger.create_from_dto(content)
    passanger_controller.update(passanger_id, passenger)
    return make_response("passenger updated", HTTPStatus.OK)


@passanger_bp.route('/<int:passanger_id>', methods=['PATCH'])
def patch_passanger(passanger_id: int) -> Response:
    content = request.get_json()
    passanger_controller.patch(passanger_id, content)
    return make_response("passenger updated", HTTPStatus.OK)


@passanger_bp.route('/<int:passanger_id>', methods=['DELETE'])
def delete_passanger(passanger_id: int) -> Response:
    passanger_controller.delete(passanger_id)
    return make_response("passenger deleted", HTTPStatus.OK)
