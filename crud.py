import app, models
from app import db

def add_url(data: dict) -> None:

    user = models.Url(**data)
    db.session.add(user)
    db.session.commit()
    db.session.flush()

def search(short_url: str) -> models.Url:
    return models.Url.query.filter_by(short_url=short_url).first()

