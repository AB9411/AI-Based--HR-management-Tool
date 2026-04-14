from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class JobBase(BaseModel):
    title: str
    department: Optional[str] = None
    skills_required: str
    min_experience: int
    description: Optional[str] = None
    location: Optional[str] = None
    employment_type: Optional[str] = None

class JobCreate(JobBase):
    pass

class JobUpdate(BaseModel):
    title: Optional[str] = None
    department: Optional[str] = None
    skills_required: Optional[str] = None
    min_experience: Optional[int] = None
    description: Optional[str] = None
    location: Optional[str] = None
    employment_type: Optional[str] = None
    status: Optional[str] = None

class JobResponse(JobBase):
    id: int
    status: str
    enhanced_description: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  
