import streamlit as st
from engines.name_detector import check_typosquatting
from engines.metadata_engine import analyze_metadata
from engines.code_scanner import scan_code_for_malware
from engines.risk_engine import calculate_risk
from utils.package_fetcher import fetch_pypi_package

st.set_page_config(page_title="SafeSupply AI", page_icon="🛡️")

st.title("🛡️ SafeSupply AI")
st.subheader("Malicious Open-Source Package Scanner")

package_name = st.text_input("Enter PyPI package name")

if st.button("Scan Package"):
    
    if package_name == "":
        st.warning("Please enter a package name")
    else:
        st.write("Scanning package... 🔍")

        # Engine 1 — Typosquatting
        typo_risks = check_typosquatting(package_name)

        # Engine 2 — Metadata
        data = fetch_pypi_package(package_name)
        if data:
            metadata_risks = analyze_metadata(data)
        else:
            metadata_risks = ["Package not found on PyPI"]

        # Engine 3 — Code Scanner (demo simulation)
        demo_code = "import os; os.system('steal data')"
        code_risks = scan_code_for_malware(demo_code)

        # Final risk score
        score, level, reasons = calculate_risk(
            typo_risks, metadata_risks, code_risks
        )

        st.metric("Risk Score", f"{score}%")
        st.subheader(level)

        st.write("### Reasons:")
        for r in reasons:
            st.write("•", r)