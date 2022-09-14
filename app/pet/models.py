from app import db


class Pet(db.Model):
    __tablename__ = 'PET'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('USER.id'), nullable=False)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'
