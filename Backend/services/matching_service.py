from typing import Tuple

def parse_skills(skills: str):
    if not skills:
        return []
    return [skill.strip().lower() for skill in skills.split(",")]

def calculate_skill_match(candidate_skills: str, job_skills: str) -> float:
    candidate_list = parse_skills(candidate_skills)
    job_list = parse_skills(job_skills)

    if not job_list:
        return 0.0

    matched = set(candidate_list) & set(job_list)
    return (len(matched) / len(job_list)) * 100

def calculate_experience_match(candidate_exp: int, required_exp: int) -> float:
    if required_exp == 0:
        return 100.0

    return min(candidate_exp / required_exp, 1) * 100

def calculate_overall_score(skill_score: float, exp_score: float) -> float:
    return (0.7 * skill_score) + (0.3 * exp_score)

def calculate_match(
    candidate_skills: str,
    job_skills: str,
    candidate_exp: int,
    required_exp: int
) -> Tuple[float, float, float]:

    skill_score = calculate_skill_match(candidate_skills, job_skills)
    exp_score = calculate_experience_match(candidate_exp, required_exp)
    overall_score = calculate_overall_score(skill_score, exp_score)

    return skill_score, exp_score, overall_score