#SkillBridge AI
#Skill Gap Analyzer
def analyze_skills(student_skills,required_skills):
    student_skills=[skill.lower() for skill in student_skills]
    required_skills=[skill.lower() for skill in required_skills]
    matched_skills=[]
    missing_skills=[]
    for skill in required_skills:
        if skill in student_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)
    return matched_skills,missing_skills


    
