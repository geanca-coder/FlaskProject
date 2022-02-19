from market import db, login_manager
from market import  bcrypt
from flask_login import UserMixin
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    username = db.Column(db.String(length=30), unique=True, nullable=False)
    email = db.Column(db.String(length=50), unique=True, nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=True)
    budget = db.Column(db.Integer(), nullable=False,default=0)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self,password_text):
        self.password_hash = bcrypt.generate_password_hash(password_text).decode('utf-8')


    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
class Item(db.Model):
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    price = db.Column(db.Integer(), nullable=False)
    available = db.Column(db.Boolean(), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'
