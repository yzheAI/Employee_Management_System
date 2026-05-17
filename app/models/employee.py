from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.db.session import Base
from datetime import datetime


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    gender = Column(String(10))
    is_deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime, nullable=True)

    department_id = Column(Integer, ForeignKey('departments.id'))

    role = Column(String(20), default='staff')
    created_at = Column(DateTime, default=datetime.utcnow)

    department = relationship('Department', back_populates='employees')
