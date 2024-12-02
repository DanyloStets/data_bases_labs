from __future__ import annotations
from typing import Dict, Any
from app import db

class DriverBuses(db.Model):
    __tablename__ = "drivers_buses"

    id = db.Column(db.Integer, primary_key=True)
    bus_id = db.Column(db.Integer, db.ForeignKey('bus.id'), nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)

    def __repr__(self) -> str:
        return f"DriverBuses(id={self.id}, bus_id={self.bus_id}, driver_id={self.driver_id})"
    
    def put_into_dto(self) -> Dict[str, Any]:
        return{
            "id": self.id,
            "bus_id": self.bus_id,
            "driver_id": self.driver_id,
        }
    
    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> DriverBuses:
        drivers_buses = DriverBuses(
            bud_id=dto_dict.get("bus_id"),
            driver_id=dto_dict.get("driver_id"),
        )
        return drivers_buses