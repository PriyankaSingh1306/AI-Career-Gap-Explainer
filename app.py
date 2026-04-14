import streamlit as st
import PyPDF2

from gap_detector import extract_date_ranges, detect_gaps
from skill_extractor import extract_skills_and_domain
from career_advisor import recommend_roles_and_skills, generate_gap_explanation

st.title("AI Career Gap Explainer")


uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")


def extract_text(pdf_file):

    reader = PyPDF2.PdfReader(pdf_file)

    text=""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text+=page_text

    text=text.replace("\n"," ")

    return text


if uploaded_file is not None:

    resume_text = extract_text(uploaded_file)

    # GAP DETECTION
    dates = extract_date_ranges(resume_text)
    gaps = detect_gaps(dates)

    st.subheader("Career Gap Analysis")

    if gaps:
        for gap in gaps:
            st.write(f"Current career gap: {gap} years")
    else:
        st.write("No major gaps detected")


    # SKILLS + DOMAIN
    skills, domain = extract_skills_and_domain(resume_text)

    st.subheader("Detected Domain")
    st.write(f"👉 {domain}")

    st.subheader("Detected Skills")

    if skills:
        for skill in skills:
            st.write(f"✔ {skill.title()}")


    # ROLE RECOMMENDATION
    roles, missing_skills = recommend_roles_and_skills(domain, skills)

    st.subheader("Recommended Career Roles")

    for role in roles:
        st.write(f"👉 {role}")


    st.subheader("Missing Skills (to improve)")

    for skill in missing_skills:
        st.write(f"❗ {skill.title()}")


    # ✅ AI GAP EXPLANATION (FIXED POSITION)
    if gaps:

        gap_years = gaps[0]

        explanation = generate_gap_explanation(domain, skills, gap_years)

        st.subheader("AI Career Gap Explanation")

        st.write(explanation)