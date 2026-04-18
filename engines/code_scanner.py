import ast

SUSPICIOUS_KEYWORDS = [
    "os.system",
    "subprocess",
    "socket",
    "eval",
    "exec",
    "requests.post"
]

def scan_code_for_malware(code_text):
    risks = []

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in code_text:
            risks.append(f"Suspicious keyword detected: {keyword}")

    return risks