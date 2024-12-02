from __future__ import annotations
from typing import Dict, Any
from app import db

class Stops(db.Model):
    __tablename__ = "stops"

    id = db.Column(db.Integer, primary_key=True)
    stop_name = db.Column(db.String(50), nullable=False)
    distance_from_prev = db.Column(db.Integer, nullable=False)
    price_to_next = db.Column(db.Integer, nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)


    def __repr__(self) -> str:
        return f"Stops(id={self.id}, stop_name={self.stop_name}, distance_from_prev={self.distance_from_prev})"\
        f"orice_to_next={self.price_to_next}, route_id={self.route_id}"
    
    def put_into_dto(self) ->Dict[str, Any]:
        return{
            "id": self.id,
            "stop_name":self.stop_name,
            "distance_from_prev":self.distance_from_prev,
            "price_to_next": self.price_to_next,
            "route_id":self.route_id,
        }
    
    @staticmethod
    def create_from_to(dto_dict: Dict[str, Any]) -> Stops:
        stops = Stops(
            stops_name=dto_dict.get("stops_name"),
            distance_from_prev=dto_dict.get("distance_from_prev"),
            prive_to_next=dto_dict.get("prive_to_next"),
            route_id=dto_dict.get("prive_to_next"),
        )
        return stops