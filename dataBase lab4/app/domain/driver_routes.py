from __future__ import annotations
from typing import Dict, Any
from app import db

class DriverRoutes(db.Model):
    __tablename__ = "driver_routes"

    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, nullable=False)
    route_id = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f" DriverRoutes(id={self.id}, driver_id={self.driver_id}, route_id={self.route_id})"
    
    def put_into_dto(self) ->Dict[str, Any]:
        return{
            "id": self.id,
            "driver_id": self.driver_id,
            "route_id": self.route_id,
        }
    
    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any])-> DriverRoutes:
        driver_routes = DriverRoutes(
            driver_id=dto_dict.get("driver_id"),
            route_id=dto_dict.get("route_id"),
        )
        return driver_routes