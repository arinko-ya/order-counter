from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, login


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    last_seen = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'<User {self.name}>'

    @classmethod
    def create(cls, username: str, password: str):
        user = User(username)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

    def set_password(self, password: str):
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)

    @login.user_loader
    def load_user(id: str):
        return User.query.get(int(id))

    @classmethod
    def password_change(cls, username: str, password: str):
        user = cls.query.filter_by(name=username).first()
        user.set_password(password)
        db.session.commit()


class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)

    item = db.relationship('Item', backref=db.backref('genre', lazy=True))

    def __repr__(self):
        return f'<Genre {self.name}>'

    @classmethod
    def get_genre_list(cls):
        try:
            genre_list = [(str(g.id), g.name) for g in cls.query.all()]
        except:
            genre_list = [('no_genre_table', 'no_genre_table')]
        return genre_list


class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String(64), index=True,
                     unique=True, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    price = db.Column(db.Integer, nullable=False)
    is_sale = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Item {self.name}>'

    def __init__(self, name: str, genre_id: str, price: int, is_sale: bool):
        self.name = name
        self.genre_id = int(genre_id)
        self.price = price
        self.is_sale = is_sale

    @classmethod
    def update_item(cls, id: int, name: str, genre_id: str,
                    price: int, is_sale: bool):
        before_item = cls.query.filter_by(id=id).first()

        before_item.name = name
        before_item.genre_id = int(genre_id)
        before_item.price = price
        before_item.is_sale = is_sale

        db.session.commit()


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    date_sold = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return f'<Order {self.item_id}>'
