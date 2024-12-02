from .bus_controller import BusController
from .bus_routes_controller import BusRoutesController
from .driver_buses_controller import DriverBusesController
from .driver_controller import DriverController
from .driver_routers_controller import DriverRoutesController
from .passanger_controller import PassangerController
from .route_controller import RouteController
from .schedules_controller import SchedulesController
from .stops_controller import StopsController
from .tickets_controller import TicketsController
from .reviews_controller import ReviewsController

bus_controller = BusController()
bus_routes_controller = BusRoutesController()
driver_buses_controller = DriverBusesController()
driver_controller = DriverController()
driver_routers_controller = DriverRoutesController()
passanger_controller = PassangerController()
route_controller = RouteController()
schedules_controller = SchedulesController()
stops_controller = StopsController()
tickets_controller = TicketsController()
reviews_controller = ReviewsController()
