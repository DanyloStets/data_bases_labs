from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import bus_controller
from ..domain.bus import Bus

bus_bp = Blueprint('bus', __name__, url_prefix='/bus')


@bus_bp.route('', methods=['GET'])
def get_all_bus() -> Response:
    return make_response(jsonify(bus_controller.find_all()), HTTPStatus.OK)


@bus_bp.route('', methods=['POST'])
def create_bus() -> Response:
    content = request.get_json()
    bus = Bus.create_from_dto(content)
    bus_controller.create(bus)
    return make_response(jsonify(bus.put_into_dto()), HTTPStatus.CREATED)


@bus_bp.route('/<int:bus_id>', methods=['GET'])
def get_bus(bus_id: int) -> Response:
    return make_response(jsonify(bus_controller.find_by_id(bus_id)), HTTPStatus.OK)


@bus_bp.route('/<int:bus_id>', methods=['PUT'])
def update_bus(bus_id: int) -> Response:
    content = request.get_json()
    bus = Bus.create_from_dto(content)
    bus_controller.update(bus_id, bus)
    return make_response("BUS updated", HTTPStatus.OK)


@bus_bp.route('/<int:bus_id>', methods=['PATCH'])
def patch_busl(bus_id: int) -> Response:
    content = request.get_json()
    bus_controller.patch(bus_id, content)
    return make_response("BUS updated", HTTPStatus.OK)


@bus_bp.route('/<int:bus_id>', methods=['DELETE'])
def delete_bus(bus_id: int) -> Response:
    bus_controller.delete(bus_id)
    return make_response("Bus deleted", HTTPStatus.OK)
