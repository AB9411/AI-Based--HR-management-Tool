from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base

from models import candidate, job, match

from routes import candidate_routes

app = FastAPI(
    title="AI Resume Evaluation API",
    description="Backend for AI-based Resume Screening System",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:4200", 
    "*",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(candidate_routes.router, prefix="/api", tags=["Candidates"])

@app.get("/")
def root():
    return {
        "message": "🚀 AI Resume Backend is running",
        "status": "success"
    }

@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "service": "Backend is healthy"
    }