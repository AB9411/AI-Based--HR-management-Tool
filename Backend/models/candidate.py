from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base

class Candidate(Base):
    __tablename__ = "candidates"


    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)

    experience = Column(Integer, nullable=False)  

    skills = Column(Text, nullable=True)
    
    resume_text = Column(Text, nullable=True)

    parsed_skills = Column(Text, nullable=True)
    education = Column(Text, nullable=True)
    work_summary = Column(Text, nullable=True)
    
    professional_summary = Column(Text, nullable=True)

    status = Column(String, default="New")  

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)