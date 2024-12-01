from __future__ import annotations
from typing import Dict, Any
from app import db

class Route(db.Model):
    __tablename__ = "route"
    id = db.Column(db.Integer, primary_key=True)
    start_adress = db.Column(db.String(50), nullable=False)
    end_adress = db.Column(db.String(50), nullable=False)
    distance = db.Column(db.Integer, nullable=False)

    buses = db.relationship('Bus', secondary='bus_routes', back_populates='routes')

    def __repr__(self) -> str:
        return f"Route(id={self.id}, start_adress={self.start_adress}, )"\
        f"end_adress={self.end_adress}, distance={self.distance}"
    

    def put_into_dto(self) -> Dict[str, Any]:
        return{
            "id":self.id,
            "start_adress":self.start_adress,
            "end_adress":self.end_adress,
            "distance":self.distance,
            "buses": [bus.id for bus in self.buses],
        }
    
    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Route:
        route=Route(
            start_adress=dto_dict.get("start_adress"),
            end_adress=dto_dict.get("end_adress"),
            distance=dto_dict.get("distance"),
        )
        return route