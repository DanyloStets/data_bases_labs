from __future__ import annotations
from typing import Dict, Any
from app import db

class Tickets(db.Model):
    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    passenger_id = db.Column(db.Integer, db.ForeignKey('passenger.id'), nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)

    def __repr__(self) ->str:
        return f"Tickets(id={self.id}, price={self.price}, passanger_id={self.passenger_id}, route_id={self.route_id})"
    

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "price" : self.price,
            "passanger_id": self.passenger_id, 
            "route_id": self.route_id,
        }
    
    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Tickets:
        tickets=Tickets(
            price=dto_dict.get("price"),
            passanger_id=dto_dict.get("passanger_id"),
            route_id=dto_dict.get("route_id"),
        )
        return tickets