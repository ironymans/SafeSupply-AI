import requests

def check_cve(package):
    try:
        url = f"https://api.osv.dev/v1/query"
        data = {
            "package": {
                "name": package,
                "ecosystem": "PyPI"
            }
        }

        r = requests.post(url, json=data)
        vulns = r.json().get("vulns", [])

        if vulns:
            return [f"CVE Found: {v['id']}" for v in vulns]

        return []

    except:
        return []