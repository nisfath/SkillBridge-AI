# SkillBridge AI
# Skill Gap Analyzer
from skill_analyzer import analyze_skills
def generate_roadmap(student_skills,required_skills):
    matched_skills, missed_skills=analyze_skills(student_skills, required_skills)
    roadmap=[]
    for skill in missed_skills:
        roadmap.append(f"Learn {skill} and practice with projects")
    return matched_skills, missed_skills, roadmap


