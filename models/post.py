from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_db import Base


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    attachment_url = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    is_deleted = Column(Boolean, default=False)

    owner = relationship("User", back_populates="posts")
