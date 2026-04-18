import requests

API_URL = "https://safesupply-ai.onrender.com/scan/"

def scan_multiple_packages(packages):
    results = []

    for pkg in packages:
        pkg = pkg.strip()
        if not pkg:
            continue

        try:
            r = requests.get(API_URL + pkg)
            results.append(r.json())
        except:
            results.append({
                "package": pkg,
                "risk_score": 0,
                "risk_level": "ERROR",
                "reasons": ["Failed to scan"]
            })

    return results