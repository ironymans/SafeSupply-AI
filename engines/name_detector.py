from Levenshtein import distance

POPULAR_PACKAGES = [
    "requests", "numpy", "pandas", "flask",
    "django", "tensorflow", "pytorch"
]

def check_typosquatting(package_name):
    risks = []
    
    for legit in POPULAR_PACKAGES:
        dist = distance(package_name.lower(), legit.lower())
        
        if 0 < dist <= 2:
            risks.append(f"Similar to popular package '{legit}'")

    return risks