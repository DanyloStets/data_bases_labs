from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import driver_routers_controller
from ..domain.driver_routes import DriverRoutes

driver_routes_bp = Blueprint('driver_routes', __name__, url_prefix='/driver_routes')


@driver_routes_bp.route('', methods=['GET'])
def get_all_driver_routes() -> Response:
    return make_response(jsonify(driver_routers_controller.find_all()), HTTPStatus.OK)


@driver_routes_bp.route('', methods=['POST'])
def create_driver_routes() -> Response:
    content = request.get_json()
    driver_routes = DriverRoutes.create_from_dto(content)
    driver_routers_controller.create(driver_routes)
    return make_response(jsonify(driver_routes.put_into_dto()), HTTPStatus.CREATED)


@driver_routes_bp.route('/inf', methods=['POST'])
def create_driver_routes_inf() -> Response:
    content = request.get_json()

    if not all(key in content for key in ['driver_name', 'driver_surname', 'route_id']):
        return make_response(jsonify({'error': 'Missing required fields'}), HTTPStatus.BAD_REQUEST)

    try:
        driver_routers_controller.assign_driver_to_route(
            driver_name=content['driver_name'],
            driver_surname=content['driver_surname'],
            route_id=content['route_id']
        )

        return make_response(jsonify({'message': 'Driver assigned to route successfully'}), HTTPStatus.CREATED)

    except Exception as e:
        return make_response(jsonify({'error': str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@driver_routes_bp.route('/<int:driver_routes_id>', methods=['GET'])
def get_driver_routes(driver_routes_id: int) -> Response:
    return make_response(jsonify(driver_routers_controller.find_by_id(driver_routes_id)), HTTPStatus.OK)


@driver_routes_bp.route('/<int:driver_routes_id>', methods=['PUT'])
def update_driver_routes(driver_routes_id: int) -> Response:
    content = request.get_json()
    driver_routes = DriverRoutes.create_from_dto(content)
    driver_routers_controller.update(driver_routes_id, driver_routes)
    return make_response("driver_routes updated", HTTPStatus.OK)


@driver_routes_bp.route('/<int:driver_routes_id>', methods=['PATCH'])
def patch_driver_routes(driver_routes_id: int) -> Response:
    content = request.get_json()
    driver_routers_controller.patch(driver_routes_id, content)
    return make_response("driver_routes updated", HTTPStatus.OK)


@driver_routes_bp.route('/<int:driver_routes_id>', methods=['DELETE'])
def delete_driver_routes(driver_routes_id: int) -> Response:
    driver_routers_controller.delete(driver_routes_id)
    return make_response("driver_routes deleted", HTTPStatus.OK)
