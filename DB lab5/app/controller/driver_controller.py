from .general_controller import GeneralController
from ..service import driver_service
from app import db
from sqlalchemy import text


class DriverController(GeneralController):
    _service = driver_service

    @staticmethod
    def insert_multiple_drivers():
        try:
            # Викликаємо збережену процедуру
            db.session.execute(text("CALL insert_multiple_drivers()"))
            db.session.commit()
            return {"message": "10 drivers inserted successfully."}
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def create_dynamic_tables_from_drivers():
        try:
            # Викликаємо збережену процедуру
            db.session.execute(text("CALL create_dynamic_tables_from_drivers()"))
            db.session.commit()
            return {"message": "Dynamic tables created successfully"}
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}

