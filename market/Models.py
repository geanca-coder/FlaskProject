class Item(db.Model):
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    id = db.Column(db.String(length=30), nullable=False, primary_key=True)
    price = db.Column(db.Integer(), nullable=False)
    available = db.Column(db.Boolean(), nullable=False)

    def __repr__(self):
        return f'Item {self.name}'
