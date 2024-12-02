from __future__ import annotations
from typing import Dict, Any
from app import db

class Driver(db.Model):
    __tablename__ = "driver"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    numbers = db.Column(db.Integer, nullable=False)
    experience_years = db.Column(db.Integer, nullable=False)
    company = db.Column(db.String(50), nullable=False)

    buses = db.relationship('Bus', secondary='drivers_buses', 
                            back_populates='drivers')

    def __repr__(self) -> str:
        return f"driver(id={self.id}, name={self.name}, surname={self.surname}, numbers={self.numbers})"\
        f"experience={self.experience_years}, company={self.company}"
    
    def put_into_dto(self, visited: set=None ) -> Dict[str, Any]:
        if visited is None:
            visited = set()

        if self.id in visited:
            return {"id": self.id, "name": self.name, "surname": self.surname}  

        visited.add(self.id)
        buses = [bus.put_into_dto(visited) for bus in self.buses] if self.buses else None
        return {
            "id":self.id,
            "name":self.name,
            "surname":self.surname,
            "numbers":self.numbers,
            "experience_years":self.experience_years,
            "company":self.company,
            "buses": buses
        }
    

    @staticmethod
    def create_from_dto(dto_dict:Dict[str, Any]) -> Driver:
        driver = Driver(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            numbers=dto_dict.get("numbers"),
            experience_years=dto_dict.get("experience_years"),
            company=dto_dict.get("company"),
        )
        return driver
