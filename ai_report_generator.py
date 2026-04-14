def generate_ai_insights(skills,current_gap):

    insights=[]

    if current_gap>3:

        insights.append("Career break detected after last employment")

        insights.append("Candidate may have been improving skills")

        insights.append("Recommend adding projects and certifications")

    if "python" in skills["technical"]:

        insights.append("Technical background detected")

    if "excel" in skills["technical"]:

        insights.append("Data analysis potential detected")

    return insights