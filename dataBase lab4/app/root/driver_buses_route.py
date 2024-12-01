from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import driver_buses_controller
from ..domain.driver_buses import DriverBuses

driver_buses_bp = Blueprint('drivers_buses', __name__, url_prefix='/drivers_buses')


@driver_buses_bp.route('', methods=['GET'])
def get_all_driver_buses() -> Response:
    return make_response(jsonify(driver_buses_controller.find_all()), HTTPStatus.OK)


@driver_buses_bp.route('', methods=['POST'])
def create_driver_buses() -> Response:
    content = request.get_json()
    drivers_buses = DriverBuses.create_from_dto(content)
    driver_buses_controller.create(drivers_buses)
    return make_response(jsonify(drivers_buses.put_into_dto()), HTTPStatus.CREATED)


@driver_buses_bp.route('/<int:driver_buses_id>', methods=['GET'])
def get_driver_buses(driver_buses_id: int) -> Response:
    return make_response(jsonify(driver_buses_controller.find_by_id(driver_buses_id)), HTTPStatus.OK)


@driver_buses_bp.route('/<int:driver_buses_id>', methods=['PUT'])
def update_driver_buses(driver_buses_id: int) -> Response:
    content = request.get_json()
    drivers_buses = DriverBuses.create_from_dto(content)
    driver_buses_controller.update(driver_buses_id, drivers_buses)
    return make_response("drivers_buses updated", HTTPStatus.OK)


@driver_buses_bp.route('/<int:driver_buses_id>', methods=['PATCH'])
def patch_driver_buses(driver_buses_id: int) -> Response:
    content = request.get_json()
    driver_buses_controller.patch(driver_buses_id, content)
    return make_response("drivers_buses updated", HTTPStatus.OK)


@driver_buses_bp.route('/<int:driver_buses_id>', methods=['DELETE'])
def delete_driver_buses(driver_buses_id: int) -> Response:
    driver_buses_controller.delete(driver_buses_id)
    return make_response("drivers_buses deleted", HTTPStatus.OK)
