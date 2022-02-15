from market import db


class User(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    username = db.Column(db.String(length=30), unique=True, nullable=False)
    email = db.Column(db.String(length=50), unique=True, nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=True)
    budget = db.Column(db.Integer(), nullable=False,default=0)
    items = db.relationship('Item', backref='owned_user', lazy=True)



class Item(db.Model):
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    price = db.Column(db.Integer(), nullable=False)
    available = db.Column(db.Boolean(), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'
