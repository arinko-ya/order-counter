from app.auth.models import User
from app.genre.models import Genre
from app import db


def main():
    User.create('admin', 'password')
    db.add_all([
        Genre('Alcohol'),
        Genre('Non Alcohol'),
        Genre('Food'),
        Genre('Other')
    ])
    db.commit()


if __name__ == '__main__':
    main()
