def recommend_roles_and_skills(domain, skills):

    roles_db = {

    "Tech": {
        "roles": ["Software Developer", "Web Developer", "Backend Developer"],
        "required_skills": ["python", "javascript", "sql", "html", "css"]
    },

    "Data": {
        "roles": ["Data Analyst", "BI Analyst", "Reporting Analyst"],
        "required_skills": ["python", "sql", "excel", "power bi", "statistics"]
    },

    "Teaching": {
        "roles": ["Teacher", "Trainer", "Academic Coordinator"],
        "required_skills": ["teaching", "communication", "curriculum"]
    },

    "Management": {
        "roles": ["Project Manager", "Operations Manager", "Team Lead"],
        "required_skills": ["leadership", "communication", "project management"]
    },

    "Finance": {
        "roles": ["Accountant", "Financial Analyst"],
        "required_skills": ["accounting", "excel", "gst"]
    },

    "Marketing": {
        "roles": ["Digital Marketer", "SEO Specialist", "Content Creator"],
        "required_skills": ["seo", "social media", "content writing"]
    }

    }

    if domain not in roles_db:
        return [], []

    role_info = roles_db[domain]

    roles = role_info["roles"]
    required_skills = role_info["required_skills"]

    missing_skills = []

    for skill in required_skills:
        if skill not in skills:
            missing_skills.append(skill)

    return roles, missing_skills

def generate_gap_explanation(domain, skills, gap_years):

    skills_text = ", ".join(skills[:5])  # limit for clean output

    if domain == "Data":

        explanation = f"""
During this period, I focused on building my expertise in data analytics and business intelligence. 
I worked on developing skills such as {skills_text}, and applied them through practical projects 
to strengthen my analytical and problem-solving abilities. This phase helped me transition 
towards a data-driven career path.
"""

    elif domain == "Tech":

        explanation = f"""
During this period, I focused on enhancing my technical skills in software development. 
I gained hands-on experience in technologies like {skills_text}, and worked on personal 
projects to improve my coding and problem-solving skills.
"""

    else:

        explanation = f"""
During this period, I focused on building my expertise in data analytics and business intelligence.

I developed skills such as {skills_text} and applied them through practical projects to strengthen my analytical and problem-solving abilities.

This phase helped me transition towards a data-driven career path.
"""

    return explanation