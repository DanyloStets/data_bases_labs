from .bus_routes_service import BusRoutesService
from .bus_service import BusService
from .driver_buses_service import DriverBusesService
from .driver_routes_service import DriverRoutesService
from .driver_service import DriverService
from .passanger_service import PassangerService
from .route_service import RouteService
from .schedules_service import SchedulesService
from .stops_service import StopsService
from .tickets_service import TicketsService


bus_routes_service = BusRoutesService()
bus_service = BusService()
driver_buses_service = DriverBusesService()
driver_routes_service = DriverRoutesService()
driver_service = DriverService()
passanger_service = PassangerService()
route_service = RouteService()
schedules_service = SchedulesService()
stops_service = StopsService()
tickets_service = TicketsService()