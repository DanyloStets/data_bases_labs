from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import driver_controller
from ..domain.driver import Driver

driver_bp = Blueprint('driver', __name__, url_prefix='/driver')


@driver_bp.route('', methods=['GET'])
def get_all_driver() -> Response:
    return make_response(jsonify(driver_controller.find_all()), HTTPStatus.OK)


@driver_bp.route('', methods=['POST'])
def create_driver() -> Response:
    content = request.get_json()
    driver = Driver.create_from_dto(content)
    driver_controller.create(driver)
    return make_response(jsonify(driver.put_into_dto()), HTTPStatus.CREATED)


@driver_bp.route('/<int:driver_id>', methods=['GET'])
def get_driver(driver_id: int) -> Response:
    return make_response(jsonify(driver_controller.find_by_id(driver_id)), HTTPStatus.OK)


@driver_bp.route('/<int:driver_id>', methods=['PUT'])
def update_driver(driver_id: int) -> Response:
    content = request.get_json()
    driver = Driver.create_from_dto(content)
    driver_controller.update(driver_id, driver)
    return make_response("driver updated", HTTPStatus.OK)


@driver_bp.route('/<int:driver_id>', methods=['PATCH'])
def patch_driver(driver_id: int) -> Response:
    content = request.get_json()
    driver_controller.patch(driver_id, content)
    return make_response("driver updated", HTTPStatus.OK)


@driver_bp.route('/<int:driver_id>', methods=['DELETE'])
def delete_driver(driver_id: int) -> Response:
    driver_controller.delete(driver_id)
    return make_response("driver deleted", HTTPStatus.OK)
