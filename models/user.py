from db.base_db import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hash = Column(String)
    is_active = Column(Boolean, default=True)

    posts = relationship("Post", back_populates="owner")