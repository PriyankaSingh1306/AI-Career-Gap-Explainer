def explain_gap(gaps):

    if not gaps:

        return "No career gap detected"

    max_gap=max(gaps)

    if max_gap<=1:

        return "Short gap"

    if max_gap<=3:

        return "Possible upskilling period"

    return "Long gap – highlight learning activities"