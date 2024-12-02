from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import tickets_controller
from ..domain.tickets import Tickets
from app import db

tickets_bp = Blueprint('tickets', __name__, url_prefix='/tickets')


@tickets_bp.route('/param', methods=['POST'])
def add_ticket():
    content = request.get_json()

    if not all(key in content for key in ['price', 'passenger_id', 'route_id']):
        return make_response(jsonify({'error': 'Missing required fields'}), HTTPStatus.BAD_REQUEST)

    try:
        new_ticket = tickets_controller.insert_ticket(
            price=content['price'],
            passenger_id=content['passenger_id'],
            route_id=content['route_id']
        )
        return make_response(jsonify(new_ticket.put_into_dto()), HTTPStatus.CREATED)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)

@tickets_bp.route('', methods=['GET'])
def get_all_tickets() -> Response:
    return make_response(jsonify(tickets_controller.find_all()), HTTPStatus.OK)


@tickets_bp.route('', methods=['POST'])
def create_tickets() -> Response:
    content = request.get_json()
    tickets = Tickets.create_from_dto(content)
    tickets_controller.create(tickets)
    return make_response(jsonify(tickets.put_into_dto()), HTTPStatus.CREATED)


@tickets_bp.route('/<int:tickets_id>', methods=['GET'])
def get_tickets(tickets_id: int) -> Response:
    return make_response(jsonify(tickets_controller.find_by_id(tickets_id)), HTTPStatus.OK)


@tickets_bp.route('/<int:tickets_id>', methods=['PUT'])
def update_tickets(tickets_id: int) -> Response:
    content = request.get_json()
    tickets = Tickets.create_from_dto(content)
    tickets_controller.update(tickets_id, tickets)
    return make_response("tickets updated", HTTPStatus.OK)


@tickets_bp.route('/<int:tickets_id>', methods=['PATCH'])
def patch_tickets(tickets_id: int) -> Response:
    content = request.get_json()
    tickets_controller.patch(tickets_id, content)
    return make_response("tickets updated", HTTPStatus.OK)


@tickets_bp.route('/<int:tickets_id>', methods=['DELETE'])
def delete_tickets(tickets_id: int) -> Response:
    tickets_controller.delete(tickets_id)
    return make_response("tickets deleted", HTTPStatus.OK)
