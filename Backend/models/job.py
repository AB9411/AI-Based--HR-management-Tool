from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    department = Column(String, nullable=True)

    skills_required = Column(Text, nullable=False)  
    min_experience = Column(Integer, nullable=False)

    description = Column(Text, nullable=True)
    location = Column(String, nullable=True)
    employment_type = Column(String, nullable=True)  

    status = Column(String, default="Open")  

    enhanced_description = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)