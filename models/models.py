from sqlalchemy import Column, Integer, String
from models.base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name_in_game = Column(String)
    api_token = Column(String)
    lang = Column(String, nullable=False)
