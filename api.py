from fastapi import FastAPI
from engines.name_detector import check_typosquatting
from engines.metadata_engine import analyze_metadata
from engines.code_scanner import scan_code_for_malware
from engines.risk_engine import calculate_risk
from utils.package_fetcher import fetch_pypi_package

app = FastAPI(title="SafeSupply AI API")

@app.get("/")
def home():
    return {"message": "SafeSupply AI is running"}

@app.get("/scan/{package_name}")
def scan_package(package_name: str):
    
    # Engine 1 — Typosquatting
    typo_risks = check_typosquatting(package_name)

    # Engine 2 — Metadata
    data = fetch_pypi_package(package_name)
    if data:
        metadata_risks = analyze_metadata(data)
    else:
        metadata_risks = ["Package not found on PyPI"]

    # Engine 3 — Code scanner (demo simulation)
    demo_code = "import os; os.system('steal data')"
    code_risks = scan_code_for_malware(demo_code)

    score, level, reasons = calculate_risk(
        typo_risks, metadata_risks, code_risks
    )

    return {
        "package": package_name,
        "risk_score": score,
        "risk_level": level,
        "reasons": reasons
    }

