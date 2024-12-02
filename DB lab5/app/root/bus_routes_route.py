from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import bus_routes_controller
from ..domain.bus_routes import BusRoutes

bus_routes_bp = Blueprint('bus_routes', __name__, url_prefix='/bus_routes')


@bus_routes_bp.route('', methods=['GET'])
def get_all_bus_routes() -> Response:
    return make_response(jsonify(bus_routes_controller.find_all()), HTTPStatus.OK)


@bus_routes_bp.route('', methods=['POST'])
def create_bus_routes() -> Response:
    content = request.get_json()
    bus_routes = BusRoutes.create_from_dto(content)
    bus_routes_controller.create(bus_routes)
    return make_response(jsonify(bus_routes.put_into_dto()), HTTPStatus.CREATED)


@bus_routes_bp.route('/<int:bus_routes_id>', methods=['GET'])
def get_bus_routes(bus_routes_id: int) -> Response:
    return make_response(jsonify(bus_routes_controller.find_by_id(bus_routes_id)), HTTPStatus.OK)


@bus_routes_bp.route('/<int:bus_routes_id>', methods=['PUT'])
def update_bus_routes(bus_routes_id: int) -> Response:
    content = request.get_json()
    bus_routes = BusRoutes.create_from_dto(content)
    bus_routes_controller.update(bus_routes_id, bus_routes)
    return make_response("bus_routes updated", HTTPStatus.OK)


@bus_routes_bp.route('/<int:bus_routes_id>', methods=['PATCH'])
def patch_bus_routes(bus_routes_id: int) -> Response:
    content = request.get_json()
    bus_routes_controller.patch(bus_routes_id, content)
    return make_response("bus_routes updated", HTTPStatus.OK)


@bus_routes_bp.route('/<int:bus_routes_id>', methods=['DELETE'])
def delete_bus_routes(bus_routes_id: int) -> Response:
    bus_routes_controller.delete(bus_routes_id)
    return make_response("bus_routes deleted", HTTPStatus.OK)
