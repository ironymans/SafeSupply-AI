from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from engines.name_detector import check_typosquatting
from engines.metadata_engine import analyze_metadata
from engines.code_scanner import scan_code_for_malware
from engines.risk_engine import calculate_risk
from engines.cve_engine import check_cve   # ⭐ NEW ENGINE
from utils.package_fetcher import fetch_pypi_package
from engines.github_engine import check_github_repo

app = FastAPI(title="SafeSupply AI API")

# --- CORS (for frontend access) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "SafeSupply AI is running"}


@app.get("/scan/{package_name}")
def scan_package(package_name: str):

    # Engine 1 — Typosquatting detection
    typo_risks = check_typosquatting(package_name)

    # Engine 2 — Fetch PyPI metadata
    data = fetch_pypi_package(package_name)
    if data:
        metadata_risks = analyze_metadata(data)
        # --- GitHub repo scan ---
        github_risks = []
        if data.get("github"):
            github_risks = check_github_repo(data["github"])
    else:
        metadata_risks = ["Package not found on PyPI"]

    # Engine 3 — Code malware scanner (demo simulation)
    demo_code = "import os; os.system('steal data')"
    code_risks = scan_code_for_malware(demo_code)

    # ⭐ Engine 4 — CVE vulnerability scanner (NEW BIG FEATURE)
    cve_risks = check_cve(package_name)

    # --- Combine all risks ---
    all_reasons = (
    typo_risks +
    metadata_risks +
    code_risks +
    github_risks +
    cve_risks
)

    # Calculate base risk score
    score, level, reasons = calculate_risk(
        typo_risks,
        metadata_risks,
        code_risks
    )

    # ⭐ Increase score if CVEs found
    if cve_risks:
        score += 30
        reasons.extend(cve_risks)

        if score > 100:
            score = 100
            if github_risks:
                score += 15
                reasons.extend(github_risks)

    return {
        "package": package_name,
        "risk_score": score,
        "risk_level": level,
        "reasons": reasons
    }