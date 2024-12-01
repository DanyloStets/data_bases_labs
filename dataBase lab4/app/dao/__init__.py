from .bus_routes_dao import BusRoutesDAO
from .bus_dao import BusDAO
from .driver_buses_dao import DriverBusesDAO
from .driver_dao import DriverDAO
from .driver_routes_dao import DriverRoutesDAO
from .passanger_dao import PassangerDAO
from .route_dao import RouteDAO
from .schedules_dao import SchedulesDAO
from .stops_dao import StopsDAO
from .tickets_dao import TicketsDAO

bus_routes_dao = BusRoutesDAO()
bus_dao = BusDAO()
driver_buses_dao = DriverBusesDAO()
driver_dao = DriverDAO()
driver_routes_dao = DriverRoutesDAO()
passanger_dao = PassangerDAO()
route_dao = RouteDAO()
schedules_dao = SchedulesDAO()
stops_dao = StopsDAO()
tickets_dao = TicketsDAO()