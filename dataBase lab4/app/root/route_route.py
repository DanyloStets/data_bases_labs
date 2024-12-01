from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import route_controller
from ..domain.route import Route

route_bp = Blueprint('route', __name__, url_prefix='/route')


@route_bp.route('', methods=['GET'])
def get_all_route() -> Response:
    return make_response(jsonify(route_controller.find_all()), HTTPStatus.OK)


@route_bp.route('', methods=['POST'])
def create_route() -> Response:
    content = request.get_json()
    route = Route.create_from_dto(content)
    route_controller.create(route)
    return make_response(jsonify(route.put_into_dto()), HTTPStatus.CREATED)


@route_bp.route('/<int:route_id>', methods=['GET'])
def get_route(route_id: int) -> Response:
    return make_response(jsonify(route_controller.find_by_id(route_id)), HTTPStatus.OK)


@route_bp.route('/<int:route_id>', methods=['PUT'])
def update_route(route_id: int) -> Response:
    content = request.get_json()
    route = Route.create_from_dto(content)
    route_controller.update(route_id, route)
    return make_response("route updated", HTTPStatus.OK)


@route_bp.route('/<int:route_id>', methods=['PATCH'])
def patch_route(route_id: int) -> Response:
    content = request.get_json()
    route_controller.patch(route_id, content)
    return make_response("route updated", HTTPStatus.OK)


@route_bp.route('/<int:route_id>', methods=['DELETE'])
def delete_route(route_id: int) -> Response:
    route_controller.delete(route_id)
    return make_response("route deleted", HTTPStatus.OK)
