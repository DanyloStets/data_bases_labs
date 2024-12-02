from __future__ import annotations
from typing import Dict, Any
from app import db

class Reviews(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)  # Унікальний ідентифікатор відгуку
    driver_id = db.Column(db.Integer, nullable=False)  # Зв'язок із таблицею driver
    rating = db.Column(db.Integer, nullable=False)  # Оцінка водія (1-5)
    comment = db.Column(db.String(255), nullable=True)  # Текст відгуку
    created_at = db.Column(db.DateTime, server_default=db.func.now())  # Дата створення

    def __repr__(self) -> str:
        return f"Reviews(id={self.id}, driverId={self.driver_id}, rating={self.rating}, comment='{self.comment}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "driver_id": self.driver_id,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Reviews:
        review = Reviews(
            driver_id=dto_dict.get("driver_id"),
            rating=dto_dict.get("rating"),
            comment=dto_dict.get("comment"),
        )
        return review
