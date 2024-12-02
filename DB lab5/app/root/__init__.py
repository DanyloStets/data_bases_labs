from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)
    from .bus_routes_route import bus_routes_bp
    from .bus_route import bus_bp
    from .driver_buses_route import driver_buses_bp
    from .driver_route import driver_bp
    from .driver_routes_route import driver_routes_bp
    from .passanger_route import passanger_bp
    from .route_route import route_bp
    from .schedules_route import schedules_bp
    from .stops_route import stops_bp
    from .tickets_route import tickets_bp
    from .reviews_route import reviews_bp

    app.register_blueprint(bus_routes_bp)
    app.register_blueprint(bus_bp)
    app.register_blueprint(driver_buses_bp)
    app.register_blueprint(driver_bp)
    app.register_blueprint(driver_routes_bp)
    app.register_blueprint(passanger_bp)
    app.register_blueprint(route_bp)
    app.register_blueprint(schedules_bp)
    app.register_blueprint(stops_bp)
    app.register_blueprint(tickets_bp)
    app.register_blueprint(reviews_bp)
