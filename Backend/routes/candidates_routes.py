from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models.candidate import Candidate
from schemas.candidate_schema import CandidateCreate

router = APIRouter()

@router.post("/candidates")
def create_candidate(candidate: CandidateCreate, db: Session = Depends(get_db)):

    existing = db.query(Candidate).filter(Candidate.email == candidate.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_candidate = Candidate(**candidate.dict())
    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)

    return {
        "message": "Candidate created successfully",
        "data": new_candidate
    }

@router.get("/candidates")
def get_all_candidates(db: Session = Depends(get_db)):
    candidates = db.query(Candidate).all()
    return candidates

@router.get("/candidates/{candidate_id}")
def get_candidate(candidate_id: int, db: Session = Depends(get_db)):
    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    return candidate

@router.put("/candidates/{candidate_id}")
def update_candidate(candidate_id: int, updated_data: CandidateCreate, db: Session = Depends(get_db)):
    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    for key, value in updated_data.dict().items():
        setattr(candidate, key, value)

    db.commit()
    db.refresh(candidate)

    return {
        "message": "Candidate updated successfully",
        "data": candidate
    }

@router.delete("/candidates/{candidate_id}")
def delete_candidate(candidate_id: int, db: Session = Depends(get_db)):
    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    db.delete(candidate)
    db.commit()

    return {"message": "Candidate deleted successfully"}
