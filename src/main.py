# SkillBridge AI
# Main Program

from skill_extractor import extract_skills
from skill_analyzer import analyze_skills
from roadmap_generator import generate_roadmap


print("Welcome to SkillBridge AI!")

resume_text = input("\nEnter your skills: ")

# Extract skills
student_skills = extract_skills(resume_text)

# Required skills for AI Engineer
required_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Statistics",
    "Deep Learning",
    "Pandas",
    "NumPy"
]

# Analyze skill gaps
matched, missing = analyze_skills(
    student_skills,
    required_skills
)

print("\nYour Skills:", student_skills)
print("\nMatched Skills:", matched)
print("\nMissing Skills:", missing)

# Generate roadmap
roadmap = generate_roadmap(missing)

print("\nYour Personalised Learning Roadmap:")

for step in roadmap:
    print("-", step["skill"], ":", step["task"])
