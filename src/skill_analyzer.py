# SkillBridge AI
# Basic Skill Extractor

SKILLS = [
    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "data science",
    "pandas",
    "numpy",
    "tensorflow",
    "pytorch",
    "git",
    "cloud computing"
]


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills


# Test the function
resume_text = """
I know Python, SQL, Pandas and Machine Learning.
"""

result = extract_skills(resume_text)

print("Skills identified:", result)
