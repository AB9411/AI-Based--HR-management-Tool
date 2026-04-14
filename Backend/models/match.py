from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from datetime import datetime
from database import Base


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)

    candidate_id = Column(Integer, ForeignKey("candidates.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)

    skill_score = Column(Float, nullable=False)
    experience_score = Column(Float, nullable=False)
    overall_score = Column(Float, nullable=False)

    explanation = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)