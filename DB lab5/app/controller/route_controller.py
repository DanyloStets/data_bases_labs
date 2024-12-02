from .general_controller import GeneralController
from ..service import route_service
from ..connection import create_connection


class RouteController(GeneralController):
    _service = route_service

    @staticmethod
    def get_through_capacity(stat_type):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.callproc('info_about_route', (stat_type,))
            connection.commit()
            cursor.execute("SELECT @result;")
            return cursor.fetchone()[0]

        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cursor.close()
            connection.close()
