from datetime import datetime
from sqlalchemy.orm import relationship
from app.db.session import Base
from sqlalchemy import Column, Integer, String, DateTime


class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    employees = relationship('Employee', back_populates='department')

