from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class CandidateBase(BaseModel):
    name: str
    email: EmailStr
    experience: int
    skills: Optional[str] = None

class CandidateCreate(CandidateBase):
    pass


class CandidateUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    experience: Optional[int] = None
    skills: Optional[str] = None
    status: Optional[str] = None

class CandidateResponse(CandidateBase):
    id: int
    status: str
    resume_text: Optional[str] = None
    parsed_skills: Optional[str] = None
    education: Optional[str] = None
    work_summary: Optional[str] = None
    professional_summary: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 