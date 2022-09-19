from app import db


class PetModel(db.Model):
    __tablename__ = 'PET'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    animal_type = db.Column(db.String(30), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('OWNER.id'), nullable=False)

    def __init__(self, name, age, animal_type):
        self.animal_type = animal_type
        self.age = age
        self.name = name

    def __str__(self):
        return f'{self.name} - {self.animal_type}'

    @classmethod
    def find_pets_by_owner_id(cls, owner_id):
        return cls.query.filter_by(owner_id=owner_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class OwnerModel(db.Model):
    __tablename__ = 'OWNER'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(30), nullable=False)
    pets = db.relationship('PetModel', backref='OWNER', cascade='all, delete', lazy=True)

    def __init__(self, name, age, city):
        self.city = city
        self.age = age
        self.name = name

    def __str__(self):
        return f'{self.name} - {self.age} - {self.city}'

    def __repr__(self):
        return self.__str__()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
