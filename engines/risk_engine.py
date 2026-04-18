def calculate_risk(typo_risks, metadata_risks, code_risks):
    score = 0
    reasons = []

    if typo_risks:
        score += 40
        reasons.extend(typo_risks)

    if metadata_risks:
        score += 25
        reasons.extend(metadata_risks)

    if code_risks:
        score += 50
        reasons.extend(code_risks)

    # cap score at 100
    score = min(score, 100)

    if score >= 70:
        level = "HIGH RISK 🚨"
    elif score >= 40:
        level = "MEDIUM RISK ⚠️"
    else:
        level = "LOW RISK ✅"

    return score, level, reasons