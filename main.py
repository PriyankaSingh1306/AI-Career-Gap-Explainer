from resume_parser import extract_text_from_pdf

from skill_extractor import extract_skills

from gap_detector import extract_years
from gap_detector import detect_gaps
from gap_detector import detect_current_gap


try:

    text = extract_text_from_pdf("resume.pdf")

    skills = extract_skills(text)

    years = extract_years(text)

    gaps = detect_gaps(years)

    current_gap = detect_current_gap(years)


    print("\n===== AI CAREER ANALYSIS =====\n")

    print("Extracted Skills:")
    print(skills)

    print("\nCareer Years Found:")
    print(years)

    print("\nInternal Gaps:")
    print(gaps if gaps else "No internal gaps")

    print("\nCurrent Gap:")
    print(current_gap,"years" if current_gap else "No current gap")


except Exception as e:

    print("Error:",e)