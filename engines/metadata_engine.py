def analyze_metadata(package_data):
    risks = []

    info = package_data["info"]

    # 1️⃣ Author check (FIXED)
    author = info.get("author")
    if not author or str(author).lower() == "unknown":
        risks.append("Unknown or missing author")

    # 2️⃣ Description check
    summary = info.get("summary") or ""
    if len(summary) < 20:
        risks.append("Very short description")

    # 3️⃣ Version count check
    releases = package_data.get("releases", {})
    if len(releases) > 50:
        risks.append("Too many releases (suspicious activity)")

    return risks