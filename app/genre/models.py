from sqlalchemy.exc import OperationalError

from app import db
from app.utils.log_util import Result, Status


class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)

    item = db.relationship('Item', backref=db.backref('genre', lazy=True))

    def __repr__(self):
        return f'<Genre {self.name}>'

    @classmethod
    def check_duplicate(cls, genre_name: str) -> bool:
        return bool(cls.query.filter_by(name=genre_name).first())

    @classmethod
    def add_genre(cls, genre_name: str) -> Result:
        if cls.check_duplicate(genre_name):
            return Result(Status.FAILED, f'{genre_name} exists.')

        db.session.add(cls(name=genre_name))
        db.session.commit()

        return Result(Status.SUCCEEDED, 'Successfully added genre.')

    @classmethod
    def get_genre_list(cls) -> list:
        try:
            genre_list = cls.query.all()
        except OperationalError:
            return [('no_genre_table', 'no_genre_table')]

        if genre_list:
            return [(str(g.id), g.name) for g in genre_list]
        return [('no_genre_table', 'no_genre_table')]

    @classmethod
    def update(cls, genre_id: str, genre_name: str) -> Result:
        if cls.check_duplicate(genre_name):
            return Result(Status.FAILED, f'{genre_name} exists.')

        genre = cls.query.filter_by(id=genre_id).first()
        if not genre:
            return Result(Status.FAILED, 'Genre update is failed.')

        genre.name = genre_name
        db.session.commit()

        return Result(Status.SUCCEEDED, 'Genre update is complete!')
