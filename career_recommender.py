def recommend_roles(skills):

    roles=[]

    if "sql" in skills["technical"] and "excel" in skills["technical"]:

        roles.append("Data Analyst")

    if "power bi" in skills["technical"]:

        roles.append("BI Analyst")

    if "php" in skills["technical"]:

        roles.append("Web Developer")

    return roles