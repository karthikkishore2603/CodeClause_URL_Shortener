from app import db
from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Date,
    ForeignKey,
    Integer,
    String,
    TIMESTAMP,
)
from sqlalchemy.orm import relationship


class Url(db.Model):
    __tablename__ = "url"
    id = Column(Integer, primary_key=True, autoincrement=True)
    original_url = Column(String(1000), nullable=False)
    short_url = Column(String(1000), nullable=False)

db.create_all()