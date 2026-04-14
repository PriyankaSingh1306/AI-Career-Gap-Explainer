import re

def extract_skills_and_domain(text):

    skills_db = {

    "Tech":[
    "python","sql","excel","power bi","tableau",
    "php","javascript","html","css","mysql"
    ],

    "Data":[
    "data analysis","statistics","machine learning",
    "pandas","numpy","data visualization"
    ],

    "Teaching":[
    "teaching","mentoring","curriculum",
    "classroom","training","instructor"
    ],

    "Management":[
    "leadership","project management",
    "communication","team management",
    "scrum","agile"
    ],

    "Finance":[
    "accounting","tally","gst",
    "financial analysis","bookkeeping"
    ],

    "Marketing":[
    "digital marketing","seo","social media",
    "content writing","branding"
    ]

    }

    text = text.lower()

    found_skills = []
    domain_count = {}

    for domain, skills in skills_db.items():

        count = 0

        for skill in skills:

            pattern = r'\b' + re.escape(skill) + r'\b'

            if re.search(pattern, text):

                found_skills.append(skill)
                count += 1

        if count > 0:
            domain_count[domain] = count

    # DOMAIN LOGIC
    if domain_count:

        if "Data" in domain_count:
            main_domain = "Data"
        elif "Tech" in domain_count:
            main_domain = "Tech"
        else:
            main_domain = max(domain_count, key=domain_count.get)

    else:
        main_domain = "Unknown"

    return found_skills, main_domain