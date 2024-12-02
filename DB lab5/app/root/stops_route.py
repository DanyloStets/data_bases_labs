from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import stops_controller
from ..domain.stops import Stops

stops_bp = Blueprint('stops', __name__, url_prefix='/stops')


@stops_bp.route('', methods=['GET'])
def get_all_stops() -> Response:
    return make_response(jsonify(stops_controller.find_all()), HTTPStatus.OK)


@stops_bp.route('', methods=['POST'])
def create_stops() -> Response:
    content = request.get_json()
    stops = Stops.create_from_dto(content)
    stops_controller.create(stops)
    return make_response(jsonify(stops.put_into_dto()), HTTPStatus.CREATED)


@stops_bp.route('/<int:stops_id>', methods=['GET'])
def get_stops(stops_id: int) -> Response:
    return make_response(jsonify(stops_controller.find_by_id(stops_id)), HTTPStatus.OK)


@stops_bp.route('/<int:stops_id>', methods=['PUT'])
def update_stops(stops_id: int) -> Response:
    content = request.get_json()
    stops = Stops.create_from_dto(content)
    stops_controller.update(stops_id, stops)
    return make_response("stops updated", HTTPStatus.OK)


@stops_bp.route('/<int:stops_id>', methods=['PATCH'])
def patch_stops(stops_id: int) -> Response:
    content = request.get_json()
    stops_controller.patch(stops_id, content)
    return make_response("stops updated", HTTPStatus.OK)


@stops_bp.route('/<int:stops_id>', methods=['DELETE'])
def delete_stops(stops_id: int) -> Response:
    stops_controller.delete(stops_id)
    return make_response("stops deleted", HTTPStatus.OK)
