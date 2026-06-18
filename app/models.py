from app.database import Base
from sqlalchemy import Column, String, Integer, Boolean

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    is_admin = Column(Boolean, default=False)