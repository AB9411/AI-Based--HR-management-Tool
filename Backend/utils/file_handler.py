import os
from fastapi import UploadFile
import shutil

UPLOAD_DIR = "uploads/resumes"

os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_resume(file: UploadFile) -> str:
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path

def extract_text_from_txt(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""

def extract_text_from_pdf(file_path: str) -> str:
    try:
        import PyPDF2

        text = ""
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""

        return text
    except Exception:
        return ""

def extract_resume_text(file_path: str) -> str:
    if file_path.endswith(".txt"):
        return extract_text_from_txt(file_path)

    elif file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)

    else:
        return ""