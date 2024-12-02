from .general_controller import GeneralController
from ..service import tickets_service
from app import db
from sqlalchemy import text
from ..domain import Tickets


class TicketsController(GeneralController):
    _service = tickets_service

    @staticmethod
    def insert_ticket(price: int, passenger_id: int, route_id: int) -> Tickets:
        try:
            # Use SQLAlchemy's session to execute the stored procedure with parameters
            db.session.execute(
                text('CALL parametrized_insertion_tickets(:p_price, :p_passenger_id, :p_route_id)'),
            {'p_price': price, 'p_passenger_id': passenger_id, 'p_route_id': route_id}
            )
            db.session.commit()  # Commit the transaction after executing the procedure

            # Create and return Ticket object after insertion
            new_ticket = Tickets(price=price, passenger_id=passenger_id, route_id=route_id)
            return new_ticket
        except Exception as e:
            db.session.rollback()  # Rollback if an error occurs
            raise e
