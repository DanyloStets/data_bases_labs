from __future__ import annotations
from typing import Dict, Any
from app import db

class Passanger(db.Model):
    __tablename__ = "passenger"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    numbers = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Passanger(id={self.id}, name={self.name}, surname={self.surname}, numbers={self.numbers})"
    
    def put_into_dto(self) -> Dict[str, Any]:
        return{
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "numbers": self.numbers,
        }
    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Passanger:
        passenger = Passanger(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            numbers=dto_dict.get("numbers"),
        )
        return passenger