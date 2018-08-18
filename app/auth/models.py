from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, login


class User(UserMixin, db.Model):
    __tablename__ = 'users'

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

    def password_change(self, password: str):
        self.set_password(password)
        db.session.commit()
