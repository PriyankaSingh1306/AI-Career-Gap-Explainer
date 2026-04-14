def skill_gap_analysis(skills,roles):

    role_skills={

    "Data Analyst":[
    "sql",
    "excel",
    "statistics",
    "python",
    "data visualization"
    ],

    "BI Analyst":[
    "power bi",
    "sql",
    "excel",
    "data modeling"
    ],

    "Web Developer":[
    "php",
    "javascript",
    "html",
    "css"
    ]

    }

    missing_skills={}

    technical=skills.get("technical",[])

    for role in roles:

        required=role_skills.get(role,[])

        missing=[]

        for skill in required:

            if skill not in technical:

                missing.append(skill)

        missing_skills[role]=missing

    return missing_skills