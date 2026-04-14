import re
from datetime import datetime

def extract_experience_section(text):

    text = text.lower()

    if "experience" in text:
        parts = text.split("experience")
        return parts[1]

    return text


def extract_date_ranges(text):

    text = extract_experience_section(text)

    years = re.findall(r'\b(19\d{2}|20\d{2})\b', text)

    years = [int(y) for y in years]

    years = sorted(list(set(years)))

    date_ranges = []

    if len(years) >= 2:
        date_ranges.append((years[0], years[-1]))

    return date_ranges


def detect_gaps(date_ranges):

    gaps = []

    current_year = datetime.now().year

    if len(date_ranges) == 1:

        last_end = date_ranges[0][1]

        gap = current_year - last_end

        if gap > 0:
            gaps.append(gap)

    return gaps