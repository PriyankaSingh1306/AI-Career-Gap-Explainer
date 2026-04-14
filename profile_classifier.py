def classify_profile(skills):

    if len(skills["technical"])>=2:
        return "Technical Professional"

    if len(skills["business"])>=2:
        return "Business Professional"

    if len(skills["teaching"])>=1:
        return "Education Professional"

    return "General Professional"