from __future__ import annotations
from typing import Dict, Any
from app import db

class Schedules(db.Model):
    __tablename__ = "schedules"

    id = db.Column(db.Integer, primary_key=True)
    time_departure = db.Column(db.Float, nullable=False)
    arrival_time = db.Column(db.Float, nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))
    bus_id = db.Column(db.Integer, db.ForeignKey('bus.id'))
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'))


    def __repr__(self) -> str:
        return f"Schedules(id={self.id}. time_departure={self.time_departure}, arrival_time={self.arrival_time})"\
        f"driver_id={self.driver_id}, bus_id={self.bus_id}, route_id={self.route_id}"
    

    def put_into_dto(self) ->Dict[str, Any]:
        return{
            "id": self.id,
            "time_departure":self.time_departure,
            "arrival_time":self.arrival_time,
            "driver_id":self.driver_id,
            "bus_id":self.bus_id,
            "route_id": self.route_id,
        }
    
    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Schedules:
        schedules =Schedules(
            time_departure=dto_dict.get("time_departure"),
            arrival_time=dto_dict.get("arrival_time"),
            driver_id=dto_dict.get("driver_id"),
            bus_id=dto_dict.get("bus_id"),
            route_id=dto_dict.get("route_id"),
        )
        return schedules