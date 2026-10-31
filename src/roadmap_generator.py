# SkillBridge AI
# Skill Gap Analyzer

def analyze_skills(student_skills, required_skills):

    student_skills = [skill.lower() for skill in student_skills]
    required_skills = [skill.lower() for skill in required_skills]

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill in student_skills:
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills


# Example student profile

student_skills = ["Python", "SQL", "Git"]

required_skills = [
    "Python",
    "Machine Learning",
    "Statistics",
    "SQL",
    "Deep Learning"
]

matched, missing = analyze_skills(
    student_skills,
    required_skills
)

print("Matched Skills:", matched)
print("Missing Skills:", missing)
