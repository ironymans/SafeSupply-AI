def calculate_risk(typo_risks, metadata_risks, code_risks):
    reasons = []
    score = 0

    # --- Typosquatting (serious threat) ---
    if typo_risks:
        score += 40
        reasons.extend(typo_risks)

    # --- Metadata risks ---
    if "Unknown or missing author" in metadata_risks:
        score += 10
    if "Too many releases (suspicious activity)" in metadata_risks:
        score += 10

    reasons.extend(metadata_risks)

    # --- Malware keywords (very serious) ---
    if code_risks:
        score += 25
        reasons.extend(code_risks)

    # --- Normalize score ---
    if score < 20:
        level = "SAFE ✅"
    elif score < 50:
        level = "MEDIUM RISK ⚠️"
    else:
        level = "HIGH RISK 🚨"

    return score, level, reasons