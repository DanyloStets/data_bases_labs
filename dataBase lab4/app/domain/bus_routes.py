from __future__ import annotations
from typing import Dict, Any
from app import db

class BusRoutes(db.Model):
    __tablemane__ = "bus_routes"
    id = db.Column(db.Integer, primary_key=True)
    bus_id = db.Column(db.Integer, db.ForeignKey('bus.id'), nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)


    def __repr__(self) -> str:
        return f"BusRoutes(id={self.id}, busId={self.bus_id}, routeId={self.route_id})"
    
    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id":self.id,
            "bus_id":self.bus_id,
            "route_id":self.route_id,
        }
    

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> BusRoutes:
        bus_routes = BusRoutes(
            bus_id=dto_dict.get("bus_id"),
            route_id=dto_dict.get("route_id"),
        )
        return bus_routes