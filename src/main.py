# SkillBridge AI
# Main Program
from roadmap_generator import generate_roadmap

student_skills = [
      "Python",
      "SQL",
      "Git"
      ]

required_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Statistics",
    "Deep Learning",
    "Numpy",
    "Pandas",
    "scikit-learn",
    "streamlit"
    
]
matched, missed, roadmap=generate_roadmap(student_skills, required_skills)
print("Matched Skills:",matched)
print("Missing Skills:",missed)
print("\nYour Learning Roadmap:")
for step in roadmap:
      print("-",step)




    
