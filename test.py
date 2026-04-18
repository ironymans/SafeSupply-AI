from engines.name_detector import check_typosquatting
from engines.metadata_engine import analyze_metadata
from engines.code_scanner import scan_code_for_malware
from engines.risk_engine import calculate_risk
from utils.package_fetcher import fetch_pypi_package

package_name = "requsets"   # fake package

# typosquat check
typo = check_typosquatting(package_name)

# metadata (simulate if package not found)
data = fetch_pypi_package("requests")
meta = analyze_metadata(data)

# simulate malicious code
fake_code = "import os; os.system('steal data')"
code = scan_code_for_malware(fake_code)

score, level, reasons = calculate_risk(typo, meta, code)

print("Risk Score:", score)
print("Risk Level:", level)
print("Reasons:")
for r in reasons:
    print("-", r)