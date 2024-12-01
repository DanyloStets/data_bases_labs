from __future__ import annotations
from typing import Dict, Any
from app import db

class Bus(db.Model):
    __tablename__ = "bus"

    id = db.Column(db.Integer, primary_key=True)
    types = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    manufactur = db.Column(db.String(50), nullable=False)
    vin = db.Column(db.String(50), nullable=False)

    drivers = db.relationship('Driver', secondary='drivers_buses', back_populates='buses')
    routes = db.relationship('Route', secondary='bus_routes', back_populates='buses')

    def __repr__(self) -> str:
        return f"Bus (id = {self.id}, types={self.types}, age={self.age}, capacity={self.capacity})"\
                f" manufacture={self.manufactur}, vin={self.vin}"
    
    def put_into_dto(self,  visited: set = None) -> Dict[str, Any]:
        if visited is None:
            visited = set()

        if self.id in visited:
            return {"id": self.id}

        visited.add(self.id)

        return {
            "id":self.id,
            "types": self.types,
            "age":self.age,
            "capacity":self.capacity,
            "mileage":self.mileage,
            "manufacture":self.manufactur,
            "vin":self.vin,
            "drivers": [driver.put_into_dto(visited) for driver in self.drivers],
            "routes": [route.put_into_dto() for route in self.routes] if self.routes else None
            }
    
    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Bus:
        bus = Bus(
            types = dto_dict.get("types"),
            age = dto_dict.get("age"),
            capacity = dto_dict.get("capacity"),
            mileage = dto_dict.get("mileage"),
            manufacture = dto_dict.get("manufacture"),
            vin = dto_dict.get("vin")
        ) 
        return bus
