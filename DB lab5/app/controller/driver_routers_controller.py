from .general_controller import GeneralController
from ..service import driver_routes_service
from app import db
from sqlalchemy import text


class DriverRoutesController(GeneralController):
    _service = driver_routes_service

    @staticmethod
    def assign_driver_to_route(driver_name: str, driver_surname: str, route_id: int):
        # Виклик процедури для призначення водія маршруту
        db.session.execute(text("CALL many_to_many_relation(:driver_name, :driver_surname, :route_id)"),
                           {'driver_name': driver_name, 'driver_surname': driver_surname, 'route_id': route_id})
        db.session.commit()
