from app import db
from app.pet import models


class User(db.Model):
    __tablename__ = 'USER'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    city = db.Column(db.String(40), nullable=False)
    pets = db.relationship('PET', backref='USER', cascade='all, delete', lazy=True)

    def __init__(self, name, surname, age, city):
        self.city = city
        self.age = age
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} - {self.surname} - {self.age} - {self.city}'

    def __repr__(self):
        return str(self.__dict__)
